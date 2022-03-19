# 前端子路由文件
from django.urls import path, include

from web.views import index, main

urlpatterns = [
    path('', index.index, name="index"),
    path('login', index.login, name="web_login"),  # 加载登陆表单
    path('dologin', index.dologin, name="web_dologin"),  # 执行登陆
    path('logout', index.logout, name="web_logout"),  # 退出登陆
    path('web/', include([
        path('<int:pIndex>', index.webindex, name="web_index"),
        path('', index.index2, name='index2'),
        path('plance', index.place, name="web_place"),  # 排名
        path('info', main.index, name='main_index')  # 表单提交
    ]))
]
