from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login

from models import Group, User, Course

# Create your views here.
@login_required
def groups(request):
    groups = Group.objects.all()
    context = {'groups': groups}
    return render(request, 'class_discuss_site/groups.html', context)


@login_required
def group_detail(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    return render(request, 'class_discuss_site/group.html', {'group': group})


@login_required
def users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'class_discuss_site/users.html', context)


@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'class_discuss_site/user.html', {'user': user})


@login_required
def courses(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'class_discuss_site/courses.html', context)


@login_required
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
            return courses(request)
        # else:
            # Return a 'disabled account' error message
    # else:
        # Return an 'invalid login' error message.
    return render(request, 'http://queenofsubtle.com/404/')