from django.urls import path
from .views import (
    CourseView
)

app_name = 'course'
urlpatterns = [
    path('', CourseView.as_view(), name='course-list'),
    # path('create/', CreateView, name='course-create'),
    # path('<int:id>/', courseDetailView.as_view(), name='course-detail'),
    # path('<int:id>/update/', UpdateView, name='course-update'),
    # path('<int:id>/delete/', DeleteView, name='course-delete'),
]