from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from account import views

#app_name="django_app"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    #account app
    path('account/', include('account.urls')),
    #images app
    path('images/', include(('images.urls', 'images'), namespace='images')),
    #python social auth
    path('social-auth/', include('social_django.urls', namespace='social'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
	urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
