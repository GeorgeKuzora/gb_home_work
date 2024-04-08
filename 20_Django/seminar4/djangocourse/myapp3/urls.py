from django.urls import include, path

from .views import OrderList

urlpatterns = [
    path(
        "orders/<int:user_id>/<int:timespan_in_days>/",
        OrderList.as_view(),
        name="order_list",
    ),
]
