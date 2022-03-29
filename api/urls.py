from django.urls import path
from . import views

urlpatterns = [
    path('product/new', views.ProductCreateAPIView.as_view()),
    path('product/<int:pk>', views.ProductDetailAPIView.as_view()),
    path('product/<int:pk>/delete', views.ProductDeleteAPIView.as_view()),
    path('product/<int:pk>/update', views.ProductUpdateAPIView.as_view()),
    path('product/', views.ProductListAPIView.as_view()),
]
