from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 20


def formatNumber(num):
    if num % 1 == 0:
        return int(num)
    return num


def percentage(percent, whole):
    return formatNumber((percent * whole / 100))
