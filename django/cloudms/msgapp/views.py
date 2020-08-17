from django.shortcuts import render
from django.http import HttpResponse, FileResponse
import os
from django.views.decorators.csrf import csrf_exempt
import time


# Create your views here.


def app_help(request):
    return HttpResponse("No help!!!")


def downloads(request):
    cwd = os.path.dirname(__file__)
    response = FileResponse(open('liuyan.txt', 'rb'))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="liuyan.txt"'
    return response


@csrf_exempt
def my_post(request):
    ly = request.POST.get('message', None)
    with open('liuyan.txt', 'a+', encoding='utf-8') as f:
        if ly not in (None, ''):
            f.write(ly + "\t" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n')
    f.close()

    ly_date = []
    for e in open('liuyan.txt', encoding='utf-8'):
        ly_date.append([e.split('\t')[0], e.split('\t')[1]])

    return render(request, "留言板.html", {'ly_date': ly_date[-6::]})


def my_get(request):
    ly_date = []
    for e in open('liuyan.txt', encoding='utf-8'):
        ly_date.append([e.split('\t')[0], e.split('\t')[1]])
    return render(request, "showliuyan.html", {'ly_date': ly_date})

