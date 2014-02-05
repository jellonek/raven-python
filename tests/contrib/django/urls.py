from __future__ import absolute_import

from django.conf import settings
try:
    from django.conf.urls import url, patterns
except ImportError:
    # for Django version less then 1.4
    from django.conf.urls.defaults import url, patterns  # NOQA

from django.http import HttpResponse


def handler404(request):
    return HttpResponse('', status=404)


def handler500(request):
    if getattr(settings, 'BREAK_THAT_500', False):
        raise ValueError('handler500')
    return HttpResponse('', status=500)


urlpatterns = patterns('tests.contrib.django.views',
    url(r'^no-error$', 'no_error', name='sentry-no-error'),
    url(r'^fake-login$', 'fake_login', name='sentry-fake-login'),
    url(r'^trigger-500$', 'raise_exc', name='sentry-raise-exc'),
    url(r'^trigger-500-ioerror$', 'raise_ioerror', name='sentry-raise-ioerror'),
    url(r'^trigger-500-decorated$', 'decorated_raise_exc', name='sentry-raise-exc-decor'),
    url(r'^trigger-500-django$', 'django_exc', name='sentry-django-exc'),
    url(r'^trigger-500-template$', 'template_exc', name='sentry-template-exc'),
    url(r'^trigger-500-log-request$', 'logging_request_exc', name='sentry-log-request-exc'),
    url(r'^trigger-500-string-template', 'string_template_exc', name='sentry-string-template-exc'),
)
