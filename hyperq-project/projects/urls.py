
from django.urls import path, re_path
from .views import projectCreate, project, projectUpdateView, projectPropertyUpdateView

# url patterns under ('p/')
urlpatterns = [

    # project urls
    path('create/', projectCreate, name='project-create'),
    path('u/<str:slug>', project, name='project'),

    # project update urls
    path('u/<str:slug>/<str:attr>', projectUpdateView, name='project-update'),
    path('u/<str:slug>/prop/<str:propname>', projectPropertyUpdateView, name='project-prop-update'),

    # api urls (projects)
    # path('api/common/', updateVal_AJAX, name='common-update'),
]