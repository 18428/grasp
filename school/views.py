from django.core import serializers
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


# 递归树
from django.views.decorators.csrf import csrf_exempt

from school import models
from school.models import User


def tree_data(pid, tree_list):
    tree = []
    for t in tree_list:
        if pid == str(t['pid']):
            children_map = {}
            domain_id = str(t['num'])
            pid = str(t['pid'])
            name = t['text']
            url = t['url']
            children_map['id'] = domain_id
            children_map['text'] = name
            children_map['url'] = url
            children_map['state'] = 'open'
            tree.append(children_map)
            if len(tree_data(domain_id, tree_list)) > 0:
                children_map['state'] = 'closed'
                children_map['children'] = tree_data(domain_id, tree_list)
    return tree


@csrf_exempt
def getMenu(request):
    row = serializers.serialize("json", models.Menu.objects.all())
    rows = []
    for r in json.loads(row):
        ra = r['fields']
        rows.append(ra)
    tree = tree_data('0', rows)
    return HttpResponse(json.dumps(tree), content_type="application/json")


def login(request):
    errors = []
    return render(request, 'login.html', {'errors': errors})


@csrf_exempt
def sign_in(request):
    errors = []
    user_name = None
    user_password = None
    if request.method == "POST":
        if not request.POST.get('user_name') or not request.POST.get('user_password'):
            errors.append('用户名或着密码不能为空！')
        else:
            user_name = request.POST.get('user_name')
            user_password = request.POST.get('user_password')
        if user_name is not None and user_password is not None:
            # 如果后续需要用user中的数据可以使用get获取，QuerySet不知道怎么得到里面的值
            user = User.objects.filter(user_name=user_name, user_password=user_password)
            if len(user) != 0:
                # if user.is_active:
                # 数据库相比其他存储session的方式慢一点，所以可以配置django来存储session到文件系统或者缓存中
                request.session['user_name'] = user_name
                # 单位秒
                request.session.set_expiry(1)
                return render(request, 'main.html', {'user_name': user_name})
                # else:
                #     errors.append('用户名错误')
            else:
                errors.append('用户名活着密码错误！')
    return render(request, 'login.html', {'errors': errors})


def main(request):
    if request.session.get('user_name', None) == None:
        errors = ['小老弟你有想法呀,想直接进系统是不存在的！老老实实Login去吧！']
        return render(request, 'login.html', {'errors': errors})
    else:
        return render(request, 'main.html')


def xsgl(request):
    return render(request, 'xsgl.html')


def yhgl(request):
    return render(request, 'yhgl.html')
