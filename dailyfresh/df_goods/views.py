from django.shortcuts import render

# Create your views here.


def index(request):             #主页
    return render(request, 'df_goods/index.html')