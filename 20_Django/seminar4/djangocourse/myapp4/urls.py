from django.urls import path

from .views import image_upload, product_upload

urlpatterns = [
    path("img/", image_upload, name="image_upload"),
    path("product/", product_upload, name="product_upload"),
]
