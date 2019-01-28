from django.core import serializers
import json
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# 递归树
from django.views.decorators.csrf import csrf_exempt

from school import models


def tree_data(pid, tree_list):
    tree = []
    for t in tree_list:
        if pid == str(t['pid']):
            children_map = {}
            domain_id = str(t['num'])
            pid = str(t['pid'])
            name = t['text']
            children_map['id'] = domain_id
            children_map['text'] = name
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


def main(request):
    return render(request, 'main.html')


def demo(request):
    return render(request, 'demo.html')
