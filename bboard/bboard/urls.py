from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.views.decorators.cache import never_cache
from django.views.static import serve
from .views import BBLoginView
from .views import BBLogoutView

urlpatterns = [
   path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
   path('admin/', admin.site.urls),
   path('', include('main.urls', namespace='')),
   path('accounts/login', BBLoginView.as_view(), name='login'),
]

if settings.DEBUG:
   urlpatterns.append(path('static/<path:path>', never_cache(serve)))
