from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('music/', views.music, name='music'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('merch/', views.merch, name='merch'),
    path('checkout/', views.checkout, name='checkout'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
