# 后台管理子路由文件
from django.urls import path

from myadmin.views import index, user, subject, adminuser, time, log

urlpatterns = [
    path('', index.index, name="myadmin_index"),  # 后台首页

    # 后台页面的登陆与退出
    path('login', index.login, name="myadmin_login"),  # 加载登陆表单
    path('dologin', index.dologin, name="myadmin_dologin"),  # 执行登陆
    path('logout', index.logout, name="myadmin_logout"),  # 退出登陆
    # 错题分析，待开发
    path('dissection', index.dissection, name="myadmin_dissection"),
    # 用户信息管理路由
    path('user/msg/<int:uid>', user.msg, name="myadmin_user_msg"),  # 查看用户详细
    path('user/<int:pIndex>', user.index, name="myadmin_user_index"),  # 浏览
    path('user/add', user.add, name="myadmin_user_add"),  # 添加表单
    path('user/insert', user.insert, name="myadmin_user_insert"),  # 执行添加
    path('user/del/<int:uid>', user.delete, name="myadmin_user_delete"),  # 执行删除
    path('user/edit/<int:uid>', user.edit, name="myadmin_user_edit"),  # 加载编辑表单
    path('user/update/<int:uid>', user.update, name="myadmin_user_update"),  # 执行编辑
    path('user/reset', user.reset, name="myadmin_score_reset"),  # 分数重置
    # 题库管理系统
    path('subject/<int:pIndex>', subject.index, name="myadmin_subject_index"),  # 题库首页
    path('subject/add', subject.add, name="myadmin_subject_add"),  # 题库增加
    path('subject/insert', subject.insert, name="myadmin_subject_insert"),  # 执行添加
    path('subject/del/<int:sid>', subject.delete, name="myadmin_subject_delete"),  # 执行删除
    path('subject/edit/<int:sid>', subject.edit, name="myadmin_subject_edit"),  # 加载编辑表单
    path('subject/update/<int:sid>', subject.update, name="myadmin_subject_update"),  # 执行编辑

    # 管理员账号路由
    path('adminuser/<int:pIndex>', adminuser.index, name="myadmin_adminuser_index"),  # 浏览
    path('adminuser/add', adminuser.add, name="myadmin_adminuser_add"),  # 添加表单
    path('adminuser/insert', adminuser.insert, name="myadmin_adminuser_insert"),  # 执行添加
    path('adminuser/del/<int:uid>', adminuser.delete, name="myadmin_adminuser_delete"),  # 执行删除
    path('adminuser/edit/<int:uid>', adminuser.edit, name="myadmin_adminuser_edit"),  # 加载编辑表单
    path('adminuser/update/<int:uid>', adminuser.update, name="myadmin_adminuser_update"),  # 执行编辑

    # 时间管理
    path('time/', time.index, name="myadmin_time_index"),
    path('time/edit/<int:tid>', time.edit, name="myadmin_time_edit"),
    path('time/update/<int:tid>', time.update, name="myadmin_time_update"),
    # 日志管理
    path('log/<int:pIndex>', log.index, name="myadmin_log_index"),
    path('log/del/<int:uid>', log.delete, name="myadmin_log_delete"),  # 执行删除
    path('log/reset', log.reset, name="myadmin_log_reset"),  # 清空日志
]
