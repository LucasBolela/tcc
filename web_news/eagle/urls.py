from django.urls import path

from eagle.views import TrackerViewSet, ReaderViewSet, SiteDeNoticiasList

urlpatterns = [
    path("tracker/", TrackerViewSet.as_view()),
    path("reader/", ReaderViewSet.as_view()),
    path("web-site/", SiteDeNoticiasList.as_view()),
]
