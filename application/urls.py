from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^sign-in$', views.SignIn.as_view(), name='sign_in'),
    url(r'^sign-up$', views.SignUp.as_view(), name='sign_up'),
    url(r'^sign-out$', views.SignOut.as_view(), name='sign_out'),

    url(r'^about$', views.About.as_view(), name='about'),
    url(r'^contacts$', views.Contact.as_view(), name='contacts'),

    url(r'^account$', views.Account.as_view(), name='account'),
]
