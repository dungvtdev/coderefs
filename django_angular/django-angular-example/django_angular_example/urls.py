# .. Imports
from django.conf.urls import url, include, patterns

from rest_framework import routers

from authentication.views import AccountViewSet
from authentication.views import LoginView, LogoutView

from .views import IndexView

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)


urlpatterns = patterns(
    '',
    url(r'^api/v1/', include(router.urls)),
    url(r'api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),

    url('^.*$', IndexView.as_view(), name='index'),
)
