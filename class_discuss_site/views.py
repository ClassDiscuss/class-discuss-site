from django.shortcuts import render, get_object_or_404

from models import Group, User, Course

# Create your views here.
def groups(request):
    groups = Group.objects.all()
    context = {'groups': groups}
    return render(request, 'class_discuss_site/groups.html', context)

def group_detail(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    return render(request, 'class_discuss_site/group.html', {'group': group})

def users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'class_discuss_site/users.html', context)

def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'class_discuss_site/user.html', {'user': user})

def courses(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'class_discuss_site/courses.html', context)

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'class_discuss_site/course.html', {'course': course})