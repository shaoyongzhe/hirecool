# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from oauth2_provider.views.generic import ProtectedResourceView


class ApiEndpoint(ProtectedResourceView):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponse(
                'Hello there! you are acting on behalf of "%s"\n'
                % request.user
            )
        return HttpResponse("Hello, OAuth2!")


def index(request):
    return HttpResponse("Hello, world. You're at the polls index")

# Create your views here.
