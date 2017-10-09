from django.conf.urls import url
from declarations.views import OfficeDetailView

urlpatterns = [
    url(r'^office/(?P<pk>\d+)', OfficeDetailView.as_view()),
]