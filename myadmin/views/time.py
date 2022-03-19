
from django.shortcuts import render
from django.core.paginator import Paginator
from myadmin.models import Time

'''
QQ:1504257947
微信：AsNIT5
website:https://asnit.top
'''


# 时间管理
def index(request):
    tmod = Time.objects
    tlist = tmod.all()
    context = {"tlist": tlist}
    return render(request, "myadmin/time/index.html", context)


def edit(request, tid=0):
    try:
        ob = Time.objects.get(id=tid)
        context = {'time': ob}
        return render(request, "myadmin/time/edit.html", context)
    except Exception as err:
        print(err)
        context = {'info': "没有找到要修改的信息！"}
        return render(request, "myadmin/info.html", context)


# 更新时间
def update(request, tid):
    try:
        ob = Time.objects.get(id=tid)
        ob.time = request.POST['time']
        ob.save()
        context = {'info': "修改成功！"}
    except Exception as err:
        print(err)
        context = {'info': "修改失败！"}
    return render(request, "myadmin/info.html", context)  # 用户信息管理的视图文件
