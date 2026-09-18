"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ps2.views import games_view, favorite_view, game_details_view, NewGameCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('games/', games_view, name='games_list'),
    path('favorite/',favorite_view, name='favorite_list'),
    path('<int:game_id>/', game_details_view, name= 'game_detail'),
    path('new_game/', NewGameCreateView.as_view(), name= 'new_game'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
