
from django.urls import path, re_path
from .views import (projectCreate, project, projectUpdateView, projectPropertyUpdateView, 
                    projectPropertyUpdate_AJAX, projectPropertyExpUpdate_AJAX,
                    projectSubquestions, projectTopics)

# url patterns under ('p/')
urlpatterns = [

    # project urls
    path('create/', projectCreate, name='project-create'),
    path('u/<str:slug>', project, name='project'),

    # project update urls
    path('u/<str:slug>/<str:attr>', projectUpdateView, name='project-update'),
    path('u/<str:slug>/prop/<str:propname>', projectPropertyUpdateView, name='project-prop-update'),

    # temp frontend urls
    path("u/<str:slug>/subquestions/", projectSubquestions, name="project-subq"),
    path("u/<str:slug>/topics/", projectTopics, name="project-topics"),

    # api urls (projects)
    path('api/update/prop', projectPropertyUpdate_AJAX, name='api-project-prop-update'),
    path('api/update/prop/exp', projectPropertyExpUpdate_AJAX, name='api-project-prop-exp-update'),
]