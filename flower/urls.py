from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()

router.register('color_cat',views.ColorCategoryViewSet)
router.register('flower_cat',views.FlowerCategoryViewSet)
router.register('flower',views.FlowerViewSet)
router.register('review',views.ReviewViewSet)

urlpatterns = [
    path('',include(router.urls)),
    # path('flower/',views.FlowerViewSet.as_view()),
]