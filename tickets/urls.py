from django.urls import path, include
from . import views


urlpatterns = [
    path('without_rest', view=views.without_rest),
    path('with_rest', view=views.fbv_list),
]
