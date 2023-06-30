from django.shortcuts import render
from django.http import HttpResponse  # import 需要的套件
from django.template import loader


# Create your views here.
# def index(request):
#     return HttpResponse("Hello World!")  # 回傳字串到前端


def index(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())  # 回傳template


def test(request):
    return HttpResponse("hello Osper")

