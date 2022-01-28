
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from todoapp.views import PlanList, GetList, UpdateList, DestroyList
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', PlanList.as_view()),
    path('todo/<int:pk>/', GetList.as_view()),
    # path('get-token/', obtain_auth_token),
    path('get-token/', TokenObtainPairView.as_view()),
    path('refresh-token/', TokenRefreshView.as_view()),
    path('todo/<int:pk>/', UpdateList.as_view()),
    path('todo/<int:pk>/', DestroyList.as_view()),
    # path('todoadd/', CreateList.as_view(), name='todoadd'),
]
