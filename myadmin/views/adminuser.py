# 用户信息管理的视图文件
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q  # Q或条件封装
from datetime import datetime
from myadmin.models import AdminUser

'''
QQ:1504257947
微信：AsNIT5
website:https://asnit.top
'''


# 信息浏览
def index(request, pIndex=1):
    umod = AdminUser.objects
    ulist = umod.all()
    mywhere = []  # 持续关键字
    # 获取并判断搜索条件，获取get方式提交的关键子Keyword，若无则为none
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
    page = Paginator(ulist, 5)  # 5条数据分页
    maxpages = page.num_pages  # 最大页数
    # 判断当前页是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  # 当前页
    plist = page.page_range  # 获取页面列表
    context = {"userlist": list2, "plist": plist, 'pIndex': pIndex, 'maxpages': maxpages, "mywhere": mywhere}
    return render(request, "myadmin/adminuser/index.html", context)


def add(request):
    return render(request, "myadmin/adminuser/add.html")


def insert(request):
    import hashlib, random

    ob = AdminUser()
    ob.username = request.POST['username']
    ob.nickname = request.POST['nickname']
    # 将密码做md5处理
    md5 = hashlib.md5()
    n = random.randint(100000, 999999)
    fpassword = request.POST['password']
    spassword = request.POST['repassword']
    if fpassword == spassword and len(ob.username) > 2:
        s = request.POST['password'] + str(n)  # 从表单中获取密码并添加干扰值
        md5.update(s.encode('utf-8'))  # 将要产生md5的子串放进去
        ob.password_hash = md5.hexdigest()  # 获取md5值
        ob.password_salt = n
        ob.status = 6
        ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "添加成功！"}
    else:
        context = {'info': "添加失败"}
    return render(request, "myadmin/info.html", context)


def delete(request, uid=0):
    try:
        adm_info = AdminUser.objects.get(id=uid)
        if adm_info != 1:
            AdminUser.objects.get(id=uid).delete()
            context = {'info': "当前管理员不可删！"}
    except Exception as err:
        print(err)
        context = {'info': "删除失败！"}
    return render(request, "myadmin/info.html", context)


def edit(request, uid=0):
    try:
        ob = AdminUser.objects.get(id=uid)
        context = {'user': ob}
        return render(request, "myadmin/adminuser/edit.html", context)
    except Exception as err:
        print(err)
        context = {'info': "没有找到要修改的信息！"}
        return render(request, "myadmin/info.html", context)


def msg(request, uid=0):
    ob = AdminUser.objects.get(id=uid)
    context = {'user': ob}
    return render(request, "myadmin/adminuser/msg.html", context)


def update(request, uid):
    try:
        ob = AdminUser.objects.get(id=uid)
        ob.nickname = request.POST['nickname']
        ob.status = request.POST['status']
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "修改成功！"}
    except Exception as err:
        print(err)
        context = {'info': "修改失败！"}
    return render(request, "myadmin/info.html", context)
