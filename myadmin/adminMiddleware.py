# 自定义中间类（执行是否登录判断）
from django.shortcuts import redirect
from django.urls import reverse
import re


class AdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        # 判断管理后台是否登录
        # 定义后台不登录也可直接访问的url列表
        urllist = ['/myadmin/login', '/myadmin/logout', '/myadmin/dologin']
        # 判断当前请求url地址是否是以/myadmin开头,并且不在urllist中，才做是否登录判断
        if re.match(r'^/myadmin', path) and (path not in urllist):
            # 判断是否登录(在于session中没有adminuser)
            if 'adminuser' not in request.session:
                # 重定向到登录页
                return redirect(reverse("myadmin_login"))
        # 拦截视图是否登陆
        if re.match(r'^/web', path):
            if 'user' not in request.session:
                return redirect(reverse("web_login"))

        response = self.get_response(request)
        return response
