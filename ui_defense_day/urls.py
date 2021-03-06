from rest_framework import routers
from . import views
from django.urls import path, include,re_path

router = routers.DefaultRouter()

router.register(r'register/students', views.Students_account)
router.register(r'register/professor', views.Professor_account)
router.register(r'register/presenter', views.Presenter_account)
router.register(r'register/industry', views.Industry_account)
router.register(r'my_documents', views.MyDocument)
router.register(r'score', views.ScoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("documents/", views.DocumentListView.as_view()),
    path("my_presenters/", views.ProfessorPresenters.as_view()),
    path("my_presenters/documents",views.ProfessorStudentsDocumentListView.as_view()),
    path("presenter_scores/", views.ScoreListview.as_view()),
    path("my_presenters/averages/", views.ProfessorStudentsAverageListView.as_view()),
    path("averages/", views.AverageScoreListView.as_view()),
]