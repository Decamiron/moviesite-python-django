from django.urls import path
from users.views import LoginUser, logout_user, RegisterUser, ProfileInfo, published_list

app_name = 'users'
urlpatterns = [
    path('<int:id>/', ProfileInfo.as_view(), name='profile'),
    path('published_list/', published_list, name='published_list'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
]
