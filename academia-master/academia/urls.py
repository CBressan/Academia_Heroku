from alunos.views import user_login
from django.conf import settings
from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^alunos/', include('alunos.urls')),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]

# Redirects
urlpatterns += [
    url(r'^$', RedirectView.as_view(url='login/', permanent=False)),
    url(r'^alunos/$', RedirectView.as_view(url='/alunos/register', permanent=False)),
    url(r'^alunos/$', RedirectView.as_view(url='/alunos/user', permanent=False)),
    url(r'^home/$', user_login,  name='user_login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)