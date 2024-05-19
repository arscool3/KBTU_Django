from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookingListView.as_view(), name='booking_list'),
    path('booking/create/', views.BookingCreateView.as_view(), name='booking_create'),
    path('booking/<int:pk>/', views.BookingDetailView.as_view(), name='booking_detail'),
    path('booking/<int:pk>/update/', views.BookingUpdateView.as_view(), name='booking_update'),
    path('booking/<int:pk>/delete/', views.BookingDeleteView.as_view(), name='booking_delete'),
    path('review/create/', views.ReviewCreateView.as_view(), name='review_create'),
    path('payment/create/', views.PaymentCreateView.as_view(), name='payment_create'),
    path('notification/create/', views.NotificationCreateView.as_view(), name='notification_create'),
]