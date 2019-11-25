from django.conf.urls import url, include
from todo import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets ith it.
router = DefaultRouter(trailing_slash=False)
router.register(r'todos', views.TodoItemViewSet)

# The API URLs are not determinated automatically ny the router
urlpatterns = [
	url(r'^', include(router.urls)),
]
