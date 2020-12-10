
from django.urls import path, re_path
from .views import projectCreate, project

# url patterns under ('p/')
urlpatterns = [

    # project urls
    path('create/', projectCreate, name='project-create'),
    path('project/<str:slug>', project, name='project'),

    # api urls (projects)
    # path('api/common/', updateVal_AJAX, name='common-update'),
]
