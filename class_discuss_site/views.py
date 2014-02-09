from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from models import Group, User, Course, ForumMessage

# Create your views here.
@login_required
def groups(request):
    user = request.user
    all_groups = Group.objects.all()

    # Todo filter in the query
    groups = list()
    for group in all_groups:
        if group.organizer.id == user.id:
            groups.append(group)
        else:
            for attendee in group.attendees.all():
                if user.id == attendee.id:
                    groups.append(group)

    context = {'groups': groups}
    return render(request, 'class_discuss_site/groups.html', context)


@login_required
def group_detail(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    messages = ForumMessage.objects.all().filter(group_id=group.id)
    context = {'group': group, 'messages': messages}
    return render(request, 'class_discuss_site/group.html', context)


@login_required
def group_post_message(request, group_id):
    sender = request.user
    message = request.POST['message']
    group = get_object_or_404(Group, pk=group_id)
    post = ForumMessage(message=message, sender=sender, group=group)  # time inserted automatically
    post.save()
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
def course_create_page(request):
    return render(request, 'class_discuss_site/course_create.html', {})


@login_required
def course_insert(request):
    name = request.POST['name']
    size = request.POST['size']
    # TODO respect user selected time
    date = request.POST['date']
    time = request.POST['time']
    organizer = request.user
    event_datetime = datetime.now()

    # skip location, attendees
    # TODO get course name too!
    course = Course.objects.get(pk=1)
    group = Group(name=name, size=size, organizer=organizer, time=event_datetime, course=course)
    group.save()

    return group_detail(request, group.id)


@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    groups = Group.objects.all().filter(course=course_id)
    context = {'course': course, 'groups': groups}
    return render(request, 'class_discuss_site/course.html', context)


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