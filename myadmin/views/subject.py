
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q  # Q或条件封装
from datetime import datetime
from myadmin.models import Subject, Standard

'''
QQ:1504257947
微信：AsNIT5
website:https://asnit.top
'''


# 信息浏览
def index(request, pIndex=0):
    smod = Subject.objects
    slist = smod.all()
    # standard_list = list(Standard.objects.all().values())
    # print(standard_list)
    # # 关系对应
    # test_standard = []  # 检测标准
    # test_weight = []  # 权重
    # for standard in standard_list:
    #     if standard['s_id'] == pIndex:
    #         test_standard.append(standard['standard'])
    #         test_weight.append(standard['weight'])
    mywhere = []

    kw = request.GET.get("keyword", None)
    if kw:
        slist = slist.filter(title__contains=kw)
        mywhere.append("keyword=" + kw)
    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(slist, 5)  # 5条数据分页
    maxpages = page.num_pages  # 最大页数
    # 判断当前页是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    slist2 = page.page(pIndex)  # 当前页
    plist = page.page_range  # 获取页面列表
    context = {"testlist": slist2, "plist": plist, 'pIndex': pIndex, 'maxpages': maxpages, "mywhere": mywhere, }
    # "test_weight": test_weight, "test_standard": test_standard}
    return render(request, "myadmin/subject/index.html", context)


'''加载题库添加表单'''


def add(request):
    return render(request, "myadmin/subject/add.html")


'''执行题库添加'''


def insert(request):
    try:
        ob = Subject()
        ob.title = request.POST['title']  # 标题
        ob.content = request.POST['content']  # 内容
        ob.score = request.POST["score"]  # 分数
        ob.command = request.POST['command']  # 命令

        ob.result1 = request.POST['result1']
        ob.result2 = request.POST['result2']
        ob.result3 = request.POST['result3']
        ob.result4 = request.POST['result4']
        ob.result5 = request.POST['result5']
        ob.result6 = request.POST['result6']
        ob.result7 = request.POST['result7']
        ob.result8 = request.POST['result8']
        ob.result9 = request.POST['result9']
        ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 格式转换
        ob.save()
        context = {'info': "添加成功！"}
    except Exception as err:
        print(err)
        context = {'info': "添加失败!"}
    return render(request, "myadmin/subject/info.html", context)





def delete(request, sid=0):
    try:
        Subject.objects.get(id=sid).delete()  # 直接删除信息
        context = {'info': "删除成功！"}
    except Exception as err:
        print(err)
        context = {'info': "删除成功，若未消失请联系管理员!"}
    return render(request, "myadmin/subject/info.html", context)


'''加载题库编辑表单'''


def edit(request, sid=0):
    try:
        ob = Subject.objects.get(id=sid)
        context = {'subject': ob}
        return render(request, "myadmin/subject/edit.html", context)
    except Exception as err:
        print(err)
        context = {'info': "没有找到要修改的信息！"}
        return render(request, "myadmin/subject/info.html", context)


'''执行题库编辑'''


def update(request, sid):
    try:
        ob = Subject.objects.get(id=sid)
        ob.title = request.POST['title']
        ob.content = request.POST['content']
        ob.score = request.POST["score"]
        ob.command = request.POST['command']
        ob.result1 = request.POST['result1']
        ob.result2 = request.POST['result2']
        ob.result3 = request.POST['result3']
        ob.result4 = request.POST['result4']
        ob.result5 = request.POST['result5']
        ob.result6 = request.POST['result6']
        ob.result7 = request.POST['result7']
        ob.result8 = request.POST['result8']
        ob.result9 = request.POST['result9']
        ob.save()
        context = {'info': "修改成功！"}
    except Exception as err:
        print(err)
        context = {'info': "修改失败！"}
    return render(request, "myadmin/subject/info.html", context)  # 用户信息管理的视图文件

# def detail(request, sid):
#     ob = Subject.objects.get(id=sid)
#     st_list = Standard.objects.get(s_id=sid)
#     ob.title = request.POST['title']  # 标题
#     ob.content = request.POST['content']  # 内容
#     ob.score = request.POST["score"]  # 分数
#     ob.command = request.POST['command']  # 命令
#     weight = st_list.weight
#     standard = st_list.standard
#     context = {'weight': weight, "standard": standard}
#     return render(request, "myadmin/subject/detail.html", context)  # 题库详细标准
