from django.urls import path

from MBTIWeb.views import Index

urlpatterns = [
    path('', Index.as_view(), name='mainIndex'),
    path('<str:webUrl>', Index.as_view(), name='mainIndex'),
]
