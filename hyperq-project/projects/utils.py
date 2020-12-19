from django.db import transaction
from .vars import PROJ_BASE_PROPS, PROJ_SUBTYPE_CHOICES_SEL, PROJ_STAGE_INIT_QUESTIONS
import projects.models

def setupProjectBaseProperties(project, update_stage=True):
    try:
        with transaction.atomic():
            for _prop in PROJ_BASE_PROPS:
                prop = projects.models.Property(project=project, name=_prop)
                prop.save()
    except (KeyboardInterrupt, SystemExit):
        # rollback changes
        project.props.all().delete()
        raise
    except Exception as e:
        print(e)
        # rollback changes
        project.props.all().delete()

    if update_stage:
        project.stage = PROJ_STAGE_INIT_QUESTIONS
        project.save()

def defaultProjectSubtype(doc_type):
    return PROJ_SUBTYPE_CHOICES_SEL[doc_type][0][0]