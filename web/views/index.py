from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse  # 重定向
from django.shortcuts import redirect
from myadmin.models import User, Time, Subject
from django.core.paginator import Paginator


'''
QQ:1504257947
微信：AsNIT5
website:https://asnit.top
'''


# Create your views here.
# 首页视图
def index(request):
    return redirect(reverse('index2'))


def index2(request):
    return render(request, 'web/index2.html')


def webindex(request, pIndex=1):
    time = Time.objects.all()  # 考试时间
    umod = Subject.objects
    slist = umod.all().order_by('id')  # 获取全部的试题
    # 执行分页处理
    # print(page_subject)
    pIndex = int(pIndex)
    page = Paginator(slist, 1)  # 1条数据分页
    maxpages = page.num_pages  # 最大页数
    # 判断当前页是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  # 当前页
    request.session.set_expiry(0)  # 用户关闭浏览器自动退出登陆
    content = {'pIndex': pIndex, 'maxpages': maxpages, 'time': time, "content": list2}
    return render(request, 'web/index.html', content)


def login(request):
    return render(request, "web/login.html")


# 执行用户登录
def dologin(request):
    try:
        # 根据登录账号获取登录者信息
        user = User.objects.get(username=request.POST['u'])
        # 判断当前用户是否被禁用
        if user.status == 1:
            # 判断登录密码是否相同
            import hashlib
            md5 = hashlib.md5()
            s = request.POST['p'] + user.password_salt  # 从表单中获取密码并添加干扰值
            md5.update(s.encode('utf-8'))  # 将要产生md5的子串放进去
            if user.password_hash == md5.hexdigest():  # 获取md5值
                # 将当前登录成功的用户信息以user为key写入到session中
                print("登陆成功！")
                request.session['user'] = user.toDict()
                # 重定向到管理首页
                return redirect(reverse("index2"))
            else:
                context = {"info": "登录密码错误！"}
        else:
            context = {"info": "无效的登录账号！"}
    except Exception as err:
        print(err)
        context = {"info": "登录账号不存在"}
    return render(request, "web/login.html", context)


def logout(request):
    del request.session['user']  # 清除session值
    return redirect(reverse("web_login"))


# 排行榜
def place(request):
    umod = User.objects
    ulist = umod.filter(status__lt=9).order_by('-score')
    context = {"userlist": ulist}
    return render(request, "web/place.html", context)
