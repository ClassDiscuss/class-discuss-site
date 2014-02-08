from django.shortcuts import render
from django.http import HttpResponse

from models import Group

# Create your views here.
def groups(request):
    groups = Group.objects.all()
    context = {'groups': groups}
    return render(request, 'class_discuss_site/groups.html', context)

def group_detail(request, group_id):
    return HttpResponse("You're looking at group %s." % group_id)