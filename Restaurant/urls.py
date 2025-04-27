#define URL route for index() view
from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('menu', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    path('api-token-auth/', obtain_auth_token)
]
