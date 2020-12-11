import logging
from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.core.validators import validate_email
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm
from .models import Profile
from .tokens import emailVerificationToken
from common.utils import send_html_email_async, validator_name, validator_username

def sendAccountVerificationEmail(username=None):
    user = None
    # get user from db
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        # cannot find user, TODO throw some error
        return
    username = user.username
    email = user.email
    mail_subject = 'Hyper Questions signup: Verify Your EMAIL Account'
    message = render_to_string('users/email_verify.html', {
        'user': user,
        'domain': Site.objects.get_current().domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':emailVerificationToken.make_token(user),
    }) 
    send_html_email_async(mail_subject, message, [email])

def profile(request, username):
    user = get_object_or_404(User, username=username)    
    req_page = request.GET.get('page')
    req_sort = request.GET.get('sort')

    page = "posts"
    sort = "top"

    if req_page is not None and req_page != "":
        if req_page == "comments":
            page = req_page
        elif request.user.is_authenticated:
            if req_page == 'upvoted' or req_page == "downvoted":
                page = req_page
            elif request.user == user:
                if req_page == 'saved':
                    page = req_page
                elif req_page == "editprofile":
                    return redirect('settings')
                elif user.administered_communities and req_page == "modpanel":
                    return redirect('modpanel')

    if req_sort is not None and req_sort != "":
        if req_sort == "latest":
            sort = req_sort

    context = {
        'profile_user': user,
        'profile': user.profile,
        'page': page,
        'sort': sort,
        'show_comm_info': True, # feed-view
    }
    
    # extra (sidebar) stuff
    if request.user == user:
        rec_memb = Membership.objects.filter(user=user).order_by('-dt_join')[:5]
        context['rec_memb'] = rec_memb
    return render(request, 'users/profile.html', context)


@login_required
def settings(request):
    # warn user to verify email
    if not request.user.profile.email_verified:
        messages.warning(request, f'Please verify your email address.')
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile', request.user.username)
        else:
            context = {
                'form': p_form,
                'profile_user': request.user,
                'profile': request.user.profile,
                'page': 'editprofile',
            }
            return render(request, 'users/profile.html', context)
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'form': p_form,
            'profile_user': request.user,
            'profile': request.user.profile,
            'page': 'editprofile',
        }
        return render(request, 'users/profile.html', context)



def login(request):
    if request.method == 'POST' and request.is_ajax():
        if request.user.is_authenticated:
            data = {'message': 'already logged in'}
            return JsonResponse(data)
        else:
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            data = {}
            if user is None:
                data = {'message': 'failure'}
                return JsonResponse(data)
            else:
                auth_login(request, user)
                data = {'message': 'success'}
                return JsonResponse(data)
    else:
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return render(request, 'users/login.html', {'redirect_path': request.path})


def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST' and request.is_ajax():
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        data = {
            'message':'',
            'error_message':'',
            'error_field':'',
            'account':{},
        }
        # test name validity
        invalid_name_chars = set('`~!@#$%^&*()+=,/.@_ ')
        try:
            validator_name(first_name)
        except ValidationError as e:
            data['message'] = 'failure'
            data['error_message'] = ' '.join(e.messages)
            data['error_field'] = 'first_name'
            return JsonResponse(data)
        if any((c in invalid_name_chars) for c in username):
            data['message'] = 'failure'
            data['error_message'] = "Name may contain only letters, numbers, and '-' character."
            data['error_field'] = 'first_name'
            return JsonResponse(data)
        try:
            validator_name(last_name)
        except ValidationError as e:
            data['message'] = 'failure'
            data['error_message'] = ' '.join(e.messages)
            data['error_field'] = 'last_name'
            return JsonResponse(data)
        if any((c in invalid_name_chars) for c in username):
            data['message'] = 'failure'
            data['error_message'] = "Name may contain only letters, numbers, and '-' character."
            data['error_field'] = 'last_name'
            return JsonResponse(data)
        # test email validity
        try:
            validate_email(email)
        except ValidationError as e:
            # email invalid
            data['message'] = 'failure'
            data['error_message'] = ' '.join(e.messages)
            data['error_field'] = 'email'
            return JsonResponse(data)
        # test email availability
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            # email available, hence test username
            # test username validity
            try:
                validator_username(username)
            except ValidationError as e:
                data['message'] = 'failure'
                data['error_message'] = ' '.join(e.messages)
                data['error_field'] = 'username'
                return JsonResponse(data)
            invalid_username_chars = set('`~!@#$%^&*()+=, ')
            if any((c in invalid_username_chars) for c in username):
                data['message'] = 'failure'
                data['error_message'] = 'Username may contain only letters, numbers, and ./-/_ characters.'
                data['error_field'] = 'username'
                return JsonResponse(data)
            # test username availability
            try:
                match = User.objects.get(username=username)
            except User.DoesNotExist:
                # username available, hence test password
                # test password validity
                try:
                    validate_password(password1)
                except ValidationError as e:
                    # password invalid
                    data['message'] = 'failure'
                    data['error_message'] = ' '.join(e.messages)
                    data['error_field'] = 'password1'
                    return JsonResponse(data)
                # password valid, test password1 & password2 match
                if password1 == password2:
                    # passwords match
                    # all seems good, attempt account creation
                    user = get_user_model().objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                    user.save()
                    # check if user's been created
                    try:
                        user = User.objects.get(username=username, email=email)
                    except User.DoesNotExist:
                        # account not created, unknown error
                        data['message'] = 'failure'
                        data['error_message'] = 'Unknown error. User account not created.'
                        return JsonResponse(data)
                    # user created successfully and stored in 'user' var
                    # send verification email to new user
                    sendAccountVerificationEmail(username=username)
                    # return user credentials and success message
                    data['message'] = 'created'
                    data['account'] = {'username':user.username, 'email':user.email}
                    return JsonResponse(data) # user expected to be redirected by sign-up webpage
                else:
                    # passwords mismatch
                    data['message'] = 'failure'
                    data['error_message'] = 'Passwords do not match'
                    data['error_field'] = 'password2'
                    return JsonResponse(data)
            # username in use
            data['message'] = 'failure'
            data['error_message'] = 'Username already in use'
            data['error_field'] = 'username'
            return JsonResponse(data)
        data['message'] = 'failure'
        data['error_message'] = 'This EMAIL address is already in use'
        data['error_field'] = 'email'
        return JsonResponse(data)
    else:
        return render(request, 'users/register.html', {'redirect_path': request.path})


def emailVerify(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user2 = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user2 = None
    if user2 is not None and emailVerificationToken.check_token(user2, token):
        if user2.profile.email_verified:
            return render(request, 'common/notification.html', {'message': "Email already verified."})
        user2.profile.email_verified = True
        user2.profile.save()
        return render(request, 'common/notification.html', {'message': "Your email has been verified."})
    else:
        return render(request, 'common/notification.html', {'message': "Email verification failed!"})


@login_required
def deleteAccount_AJAX(request):
    if request.method == 'POST' and request.is_ajax():
        if not request.user.is_authenticated:
            data = {'deleted': False, 'message': 'not logged in'}
            return JsonResponse(data)
        else:
            user_pass = request.user.password
            entered_pass = request.POST["password"]
            if check_password(user_pass, entered_pass):
                request.user.delete()
                data = {'deleted': True, 'message': 'failure'}
                return JsonResponse(data)
            data = {'deleted': False, 'message': 'failure'}
            return JsonResponse(data)


from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import PasswordResetView
from .forms import MyPasswordResetForm

class MyPasswordResetView(UserPassesTestMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    form_class = MyPasswordResetForm

    def test_func(self):
        return self.request.user.is_anonymous