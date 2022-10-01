from django.urls import path
from .views import index_page, CreateItemView, DetailItemView

urlpatterns = [
    path("", index_page, name="index"),
    path("create/", CreateItemView.as_view(), name='create'),
    path("details/<int:pk>/", DetailItemView.as_view(), name='details')
]