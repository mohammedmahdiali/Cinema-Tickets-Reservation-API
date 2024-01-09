from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('guests', views.GuestViewSet)
router.register('movies', views.MovieViewSet)
router.register('reservations', views.ReservationViewSet)

urlpatterns = [
    path('without_rest', view=views.without_rest),
    path('cbv', view=views.GuestView.as_view()),
    path('cbv/<int:pk>', view=views.GuestView_pk.as_view()),
    path('fbv', view=views.fbv),
    path('fbv/<int:pk>', view=views.fbv_pk),
    path('mixin', view=views.MixinsList.as_view()),
    path('mixin/<int:pk>', view=views.Mixins_pk.as_view()),
    path('generic', view=views.GenericList.as_view()),
    path('generic/<int:pk>', view=views.GenericList_pk.as_view()),
    path('viewset/', include(router.urls)),
    path('find_movie', view=views.find_movie),
    path('create_reservation', view=views.create_reservation),
]
