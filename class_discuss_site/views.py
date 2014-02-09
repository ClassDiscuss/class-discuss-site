from django.shortcuts import render, get_object_or_404

from models import Group, User, Course
from django.contrib.auth import authenticate, login

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


def user_detail(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'class_discuss_site/user.html', {'user': user})


def courses(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'class_discuss_site/courses.html', context)


def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'class_discuss_site/course.html', {'course': course})


def login_request(request):
    context = {}
    return render(request, 'class_discuss_site/login.html', context)

def authenticate_request(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.

        # else:
            # Return a 'disabled account' error message
    # else:
        # Return an 'invalid login' error message.
    return courses(request)