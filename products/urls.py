from products import views, api_views
from django.urls import path


urlpatterns = [
    path('product/<int:num>/<slug:slug>/', views.product_detail,
         name="product"),
    path('homepage/<int:number>/', views.CategoryView.as_view(),
         name="category"),
    path('product/add/', views.CreateNewProduct.as_view(),
         name="add_product"),
    path('product/change/<slug:slug>/', views.UpdateProductData.as_view(),
         name="change_product_info"),


    path('api/product-list/', api_views.ProductListAPIView.as_view(),
         name="api-product-list"),
    path('api/category-list/<int:num>/', api_views.CategoryAPIView.as_view(),
         name="api-category-view"),
    path('api/detail-update-product/<int:pk>/', api_views.ProductRetrieveUpdateAPIView.as_view(),
         name="detail-update-product")
]
