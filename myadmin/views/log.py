from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q  # Q或条件封装
from datetime import datetime
from myadmin.models import Log

'''
QQ:1504257947
微信：AsNIT5
website:https://asnit.top
'''


def index(request, pIndex=1):
    umod = Log.objects
    ulist = umod.filter(status__lt=9)
    mywhere = []
    kw = request.GET.get("keyword", None)
    if kw:
        ulist = ulist.filter(Q(username__contains=kw) | Q(nickname__contains=kw))
        mywhere.append("keyword=" + kw)
    # 状态判断
    status = request.GET.get("status", "")
    if status != '':
        ulist = ulist.filter(status=status)
        mywhere.append("status" + status)
    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(ulist, 10)
    maxpages = page.num_pages

    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)
    plist = page.page_range
    context = {"loglist": list2, "plist": plist, 'pIndex': pIndex, 'maxpages': maxpages, "mywhere": mywhere}
    return render(request, "myadmin/log/index.html", context)


def delete(request, uid=0):
    try:
        Log.objects.get(id=uid).delete()  # 直接执行删除
        context = {'info': "删除成功！"}
    except Exception as err:
        print(err)
        context = {'info': "删除失败！"}
    return render(request, "myadmin/info.html", context)


def reset(request):
    try:
        ob = Log.objects.filter(status__lte=1)
        ob.update(status=9)
        context = {'info': "清空成功！"}
    except Exception as err:
        print(err)
        context = {'info': "清空失败！"}
    return render(request, "myadmin/info.html", context)
