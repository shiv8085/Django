
# urls.py
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", views.home_page),
    path("api/v1/", include('api.urls')),
    path('email/', views.send_email_view, name='send_email_view'),
    path('email_sent/', views.email_sent_view, name='email_sent_view'),
]



# from django.contrib import admin
# from django.urls import path, include
# from .views import home_page, send_email_view  # Import the send_email_view here

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("home/", home_page),
#     path("api/v1/", include('api.urls')),
#     path('email/', send_email_view, name='send_email'),  # Use the correct view function here
# ]
