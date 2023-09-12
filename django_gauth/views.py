from django.http.response import HttpResponseRedirect
from . import constants
from django.contrib.auth import authenticate, login
from .backends import GoogleAuthBackend
# Create your views here.

def google_login(request):
    return HttpResponseRedirect(constants.GOOGLE_LOGIN_REDIRECT_URI)


def google_callback(request):
    if 'error' in request.GET:
        return HttpResponseRedirect('/admin')

    if 'code' in request.GET:
        user = authenticate(request, code=request.GET.get('code'), backend=GoogleAuthBackend)
        if user:
            login(request, user=user)

        return HttpResponseRedirect('/admin')






