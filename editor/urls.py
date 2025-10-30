# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.editor, name='editor'), 
# ]


# editor/urls.py
from django.urls import path
from . import views

app_name = "editor"

urlpatterns = [
    path("auth/", views.auth_page, name="auth"),
    path("api/login/", views.api_login, name="api_login"),
    path("api/signup/", views.api_signup, name="api_signup"),
    path("api/logout/", views.api_logout, name="api_logout"),
    path("", views.editor_page, name="editor"),  # /editor/
    path("<str:room_name>/", views.editor_page, name="editor_room"),
]
