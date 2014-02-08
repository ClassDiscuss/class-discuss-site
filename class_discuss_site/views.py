from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def groups(request):
    return HttpResponse("Hello, world. You're at the groups index.")

def group_detail(request, group_id):
    return HttpResponse("You're looking at group %s." % group_id)