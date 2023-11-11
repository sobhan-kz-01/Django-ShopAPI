from django.contrib import messages
from django.core.paginator import Paginator
from django.http.response import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.views import View
from services.models import Service
from user.forms import  CustomConfigForm, UserUpdateForm,CustomPasswordRestForm
from user.models import UserService,NotifictionUser
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
import time
class UserServiceView(LoginRequiredMixin,View):
    def post(self,request):
        if request.user.advance:

            form = CustomConfigForm(request.POST)
            if form.is_valid():
                service_id = request.POST.get('service_id')
                config_name = form.cleaned_data.get('config_name')
                service_obj = get_object_or_404(UserService,id=service_id)
                service_obj.name_config = config_name
                service_obj.config = None
                service_obj.save()
                messages.success(request,"با موفقیت ذخیره شد")
                time.sleep(4)
        return redirect(f"{request.META.get('HTTP_REFERER')}")
    def get(self,request):
        q = request.GET.get('q')
        if q:
            services = UserService.objects.filter(Q(owner=request.user)& Q(code__icontains=q) ).distinct().all()

        else:
            
            services = UserService.objects.filter(owner=request.user).all()
        paginator = Paginator(services,20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context = {
            'page_obj':page_obj,
           
        }
        if request.user.advance:

            form = CustomConfigForm()
            
            context['form'] = form
        return render(request,'user/user-services.html',context)

def turn_service(request,code):
    url = request.META.get('HTTP_REFERER')
    service = get_object_or_404(UserService,code=code)
    if request.method == 'POST':
        if service.status:
            service.status = False
        else:
            service.status = True
        service.save()
    return redirect(f'{url}')


def remove_notif(request,id):
    if request.method == 'POST':
        obj = get_object_or_404(NotifictionUser,id=id)
        obj.users.remove(request.user)
    return redirect(f"{request.META.get('HTTP_REFERER')}")


class Dashboard(LoginRequiredMixin,View):
    http_method_names = ['get']

    def get(self,request):
        service_count = UserService.objects.filter(owner=request.user,expired=False).count()
        notif = NotifictionUser.objects.all().filter(users=request.user)
        context = {
            "notif":notif,
            'service_count':service_count
        }
        return render(request,'user/dashboard.html',context)

@login_required(login_url='accounts:auth')
def update_profile(request):
    form = UserUpdateForm(request.POST or None,request.FILES or None,instance=request.user)
    if form.is_valid():
        form.save()
    
    context = {
        'form':form
    }
    return render(request,'user/editprofile.html',context)
    


@login_required(login_url='accounts:auth')
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordRestForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'پسورد شما با موفقیت تغییر کرد')
            return redirect('home')
        else:
            messages.error(request, 'خطایی رخ داده است')
    else:
        form = CustomPasswordRestForm(request.user)
    return render(request, 'user/change-password.html', {
        'form': form
    })
    
