from rest_framework import routers
from . import views
from django.urls import path, include,re_path


router = routers.DefaultRouter()

router.register(r'register/students', views.Students_account)
router.register(r'register/professor', views.Professor_account)

urlpatterns = [
    path('', include(router.urls)),
    path('register/presenter', views.CreatePresenter.as_view()),

]