from django.urls import path
from .views import orderList, orderDetail

urlpatterns = [
    path('', orderList.as_view(), name = 'order_list'),
    path('<int:pk>/',orderDetail.as_view(), name = 'order_detail')

]