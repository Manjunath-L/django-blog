from django.urls import path
from . import views

app_name = 'dashboards'

urlpatterns = [
    path('',views.dashboard_home , name='dashboard'),
    path("categories/", views.categories, name="categories"),
    path("categories/add/", views.add_category, name="add_category"),
    path("categories/edit/<int:pk>/", views.edit_category, name="edit_category"),
    path("categories/delete/<int:pk>/", views.delete_category, name="delete_category"),
]
