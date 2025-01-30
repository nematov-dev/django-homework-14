from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('contact/',views.ContactCreateView.as_view(),name='contact'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('home/',views.home_page_view,name='home'),
    path('',views.main_page_view,name='main')
]