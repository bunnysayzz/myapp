from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This handles the base URL of the app
    path('<int:book_id>/', views.book_detail, name='book_detail'),  
    path('category/<str:category>/', views.category_detail, name='category_detail'),
] 


