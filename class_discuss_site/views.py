from django.shortcuts import render, get_object_or_404

from models import Group

# Create your views here.
def groups(request):
    groups = Group.objects.all()
    context = {'groups': groups}
    return render(request, 'class_discuss_site/groups.html', context)


def group_detail(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    return render(request, 'class_discuss_site/group.html', {'group': group})