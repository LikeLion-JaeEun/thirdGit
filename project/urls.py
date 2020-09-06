#기본 import
from django.contrib import admin
from django.urls import path
#include import
from django.conf.urls import include
#앱 import
import app.views
import accounts.views
import blog.views
#staic import
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.views.home, name="home"),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
]
