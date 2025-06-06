from django.urls import path
from .views import index, MenuItemView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path(route='',view=index,name='home'),
    path(route='menu/', view=MenuItemView.as_view()),
    path(route='menu/<int:pk>', view=SingleMenuItemView.as_view()),
    path(route='api-token-auth/',view=obtain_auth_token)
]
