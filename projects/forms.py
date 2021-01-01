from django.forms import ModelForm, HiddenInput
from .models import Project
from django.forms import ValidationError


class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'doc_type']