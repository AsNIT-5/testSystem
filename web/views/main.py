from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse  # 重定向
from django.shortcuts import redirect
from django.utils import timezone as datetime
from myadmin.models import Subject, User, Log, Standard
import paramiko
import socket


def index(request):
    user_id = request.POST.get('user_id')  # 提交表单的用户id,是一个QueryDict,使用get方法获取
    ui = User.objects.get(id=user_id)  # 获取到所有用户列表数据，
    subject_all = list(Subject.objects.all().values().order_by('id'))  # 题库的全部信息
    index_page = request.POST["page_index"]  # 当前页id,str
    all_command = []  # 检测命令列表
    standards = []  # 检测标准
    title_name = []
    in_subject_score = {}
    for command in subject_all:
        if command['id'] == int(index_page):
            title_name.append(command['title'])
            all_command.append(command['command'])
            standards.append(command['result1'])
            standards.append(command['result2'])
            standards.append(command['result3'])
            standards.append(command['result4'])
            standards.append(command['result5'])
            standards.append(command['result6'])
            standards.append(command['result7'])
            standards.append(command['result8'])
            standards.append(command['result9'])
            in_subject_score['score'] = command['score']
    if "y" in standards:
        for i in range(1, standards.count('y') + 1):
            standards.remove('y')
    ip = request.POST['ip']
    host_user = request.POST['host_user']
    host_pass = request.POST['host_pass']
    # 取消校验
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 实例化检测标准
    try:
        client.connect(hostname=ip, username=host_user, password=host_pass, timeout=2)
        for cmd in all_command:
            x, y, z = client.exec_command(cmd)
            outcome = y.read().decode("utf-8")
            # 执行整个判分过程
            # ----------------------------------------------
            num = len(standards)
            print(in_subject_score['score'])
            for standard in standards:
                if standard in outcome:
                    new_command = in_subject_score['score'] / num
                    new_score = ui.score + new_command
                    ui.score = new_score  # 加分
            # ------------------------------------------------------
            ui.save()
            client.close()
        # 写入日志
        ts = Log()
        ts.t_user = ui.username
        ts.t_subject = title_name[0]
        ts.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ts.save()
        data = "提交成功!"
        request.session['data'] = data
    except paramiko.ssh_exception.AuthenticationException:
        data = "链接失败<请核对后再提交>"
        request.session['data'] = data
    except socket.timeout:
        data = "无法链接<请核对后再提交>"
        request.session['data'] = data
    except Exception as err:
        print(err)
        data = '未知错误<请联系管理员>'
        request.session['data'] = data
    return redirect(reverse('web_index', args=index_page))
