
from django.urls import path
from . import views

app_name = "editor"

urlpatterns = [
    path("auth/", views.auth_page, name="auth"),
    path("api/login/", views.api_login, name="api_login"),
    path("api/signup/", views.api_signup, name="api_signup"),
    path("api/logout/", views.api_logout, name="api_logout"),
      # New
    path("api/save_code/", views.save_code, name="save_code"),
    path("api/load_code/", views.load_code, name="load_code"),    

    path("account/", views.account_page, name="account"),
    path("api/update_email/", views.update_email, name="update_email"),

    path("", views.editor_page, name="editor"),  # /editor/
    path("<str:room_name>/", views.editor_page, name="editor_room"),
]
