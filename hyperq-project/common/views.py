from django.shortcuts import render
from django.contrib.auth.decorators import login_required

TEXT_ENG__ERR_404 = "Page Not Found"
TEXT_ENG__ERR_400 = "Bad Request"
TEXT_ENG__ERR_403 = "Permission Denied"
TEXT_ENG__ERR_500 = "Server Error"

@login_required
def home(request):
    context = {}
    return render(request, 'common/home.html', context)

def about(request):
    context = {}
    return render(request, 'meta/about.html', context)

def faq(request):
    context = {}
    return render(request, 'meta/faq.html', context)

def support(request):
    context = {}
    return render(request, 'meta/support.html', context)

def policy(request):
    context = {}
    return render(request, 'meta/policy.html', context)

def handler404(request, exception):
    context = {
        'error' : TEXT_ENG__ERR_404,
    }
    return render(request, 'common/error.html', context)

def handler400(request, exception):
    context = {
        'error' : TEXT_ENG__ERR_400,
    }
    return render(request, 'common/error.html', context)

def handler403(request, exception):
    context = {
        'error' : TEXT_ENG__ERR_403,
    }
    return render(request, 'common/error.html', context)

def handler500(request):
    context = {
        'error' : TEXT_ENG__ERR_500,
    }
    return render(request, 'common/error.html', context)
