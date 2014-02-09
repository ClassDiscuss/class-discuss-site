from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from models import Discussion, User, Course, ForumMessage


# Create your views here.
@login_required
def user_discussions(request):
    """
    Displays all discussions for the given user.
    The user must be an organizer or attendee of this discussion.
    """
    user = request.user
    unfiltered_discussions = Discussion.objects.all()

    # Todo filter in the query
    discussions = list()
    for discussion in unfiltered_discussions:
        if discussion.organizer.id == user.id:
            discussions.append(discussion)
        else:
            for attendee in discussion.members.all():
                if user.id == attendee.id:
                    discussions.append(discussion)

    context = {'discussions': discussions}
    return render(request, 'class_discuss_site/user_discussions.html', context)


@login_required
def discussion_detail(request, discussion_id):
    """
    Display a single discussion in detail.
    This includes the messages for it as well.
    If the request is post, insert a message into the discussion as well.
    """
    if request.method == 'POST':
        sender = request.user
        text = request.POST['text']
        discussion = get_object_or_404(Discussion, pk=discussion_id)
        message = ForumMessage(text=text, sender=sender, discussion=discussion)  # time inserted automatically
        message.save()

    discussion = get_object_or_404(Discussion, pk=discussion_id)

    if request.user.id not in discussion.members.all() and request.user.id != discussion.organizer.id:
        discussion.members.add(request.user)

    messages = ForumMessage.objects.all().filter(discussion_id=discussion_id)
    context = {'discussion': discussion, 'messages': messages}
    return render(request, 'class_discuss_site/discussion_detail.html', context)

@login_required
def discussion_detail_logout(request, discussion_id):
    """
    Let the user leave from the given discussion.
    """
    discussion = get_object_or_404(Discussion, pk=discussion_id)
    discussion.members.remove(request.user)
    discussion.save()
    return HttpResponseRedirect('../../../discussions')

@login_required
def discussion_create(request):
    """
    Page to create a discussion.
    """
    if request.method == "POST":
        # todo use from form
        # course_name = request.POST['course_name']
        # course = Course.objects.all().filter(name=course_name)
        course = get_object_or_404(Course, pk=1)
        name = request.POST['name']
        size = request.POST['size']
        organizer = request.user
        # TODO respect user selected time
        event_datetime = datetime.now()
        # no information for location or attendees yet
        discussion = Discussion(course=course, organizer=organizer, name=name, size=size, datetime=event_datetime)
        discussion.save()
        return HttpResponseRedirect(discussion.id)
    else:  # Get page here
        return render(request, 'class_discuss_site/discussions_create.html', {})


@login_required
def user_detail(request, username):
    """
    Display a user's profile in detail.
    This is restricted to only the user's own profile, accessing another user's profile
    will give an unauthorized exception.
    """
    user = get_object_or_404(User, username=username)
    if request.user.id == user.id:
        return render(request, 'class_discuss_site/user_detail.html', {'user': user})
        # todo
        # else:
        #   Unauthorized!


@login_required
def courses(request):
    """
    Show all courses in our database.
    """
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'class_discuss_site/courses.html', context)


@login_required
def course_detail(request, course_id):
    """
    Show a detailed page for a course.
    """
    course = get_object_or_404(Course, pk=course_id)
    discussions = Discussion.objects.all().filter(course=course_id)
    context = {'course': course, 'discussions': discussions}
    return render(request, 'class_discuss_site/course_detail.html', context)


def index_view(request):
    """
    Displays the index page (or homepage)
    """
    return login_view(request)


def login_view(request):
    """
    Show a login page for a user, or login if this is a post request.
    """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                # Redirect to a success page.
                login(request, user)
                return HttpResponseRedirect('../courses')
                # else:
                # Return a 'disabled account' error message
                # else:
                # Return an 'invalid login' error message.
                #return render(request, 'http://queenofsubtle.com/404/')
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect('../courses')
        return render(request, 'class_discuss_site/index.html', {})


def logout_view(request):
    """
    Logout the user!
    """
    logout(request)
    return HttpResponseRedirect('../')
