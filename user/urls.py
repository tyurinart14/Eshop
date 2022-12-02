from user import views, api_views
from django.urls import path

app_name = "user"

urlpatterns = [
    path('login/', views.LoginPageView.as_view(),
         name="login"),
    path('logout', views.logout_view,
         name="logout"),
    path('register', views.RegisterPageView.as_view(),
         name="register"),
    path('client_page/<slug:slug>', views.ClientPage.as_view(),
         name="client_page"),
    path('<slug:slug>/edit_data/', views.ClientUpdateView.as_view(),
         name="update_page"),


    path('api/user-list/', api_views.UserListCreateAPIView.as_view(),
         name="list-create-user"),
    path('api/detail-update-user/<username>/', api_views.UserDetailUpdateAPIView.as_view(),
         name="detail-update-user")
]
