from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .serializers import ChangePasswordSerializer, ProfileSerializer


class UpdateProfileAPIView(generics.UpdateAPIView):
    serializer_class = ProfileSerializer


class ChangePasswordAPIView(generics.GenericAPIView):
    """
    Change Current Password API
    """

    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        obj = self.request.user
        return obj

    def put(self, request):
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        self.object = self.get_object()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            if not self.object.check_password(old_password):
                return Response(
                    {"error": "Current password is wrong"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            self.object.set_password(new_password)
            self.object.save()
            return Response(
                {"message": "Password has been change"}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
