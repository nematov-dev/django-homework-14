from django.urls import path


from blogs import views


app_name = 'blogs'

urlpatterns = [
    path('',views.BlogListView.as_view(),name='blog'),
    path('blog/<int:pk>/',views.BlogDetailView.as_view(),name='blog_detail'),
]
