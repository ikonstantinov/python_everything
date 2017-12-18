from django.conf.urls import url


urlpatterns = [
    url(
        r'^login/$', "django.contrib.auth.views.login",
        {
            'template_name': 'login.html'
        }
    ),
    url(
        r'^logout/$', "django.contrib.auth.views.logout",
        {
            'next_page': '/'
        }
    ),
    url(r'^registration/$', "accounts.views.register_user"),
]
