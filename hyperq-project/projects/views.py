from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, JsonResponse
from django.core.exceptions import SuspiciousOperation, PermissionDenied
from .notifications import *
from .forms import ProjectCreationForm
from common.views import notificationView
from .vars import ( PROJ_STAGE_STARTED, PROJ_STAGE_INIT_QUESTIONS, PROJ_STAGE_BASECAMP, PROJ_STAGE_STRUCTURING, 
                    PROJ_INIT_QUESTIONS_FLOW, 
                    INIT_Q_TITLE, INIT_Q_TYPE, INIT_Q_SUBTYPE, INIT_Q_DOC_LEN, INIT_Q_DOC_TOPIC, INIT_Q_PROP,
                    PROJ_TYPE_CHOICES, PROJ_SUBTYPE_CHOICES_SEL, PROJ_TOPIC_CHOICES, PROJ_DOCSIZE_CHOICES )
from .content import (  PROJ_SUBTYPE_DESCRIPTIONS, PROJ_TYPE_LIST, PROJ_SUBTYPE_CHOICES_SEL_LIST,
                        PROJ_TOPIC_DESCRIPTIONS, PROJ_DOCSIZE_DESCRIPTIONS,
                        PROJ_TYPE_SVGS, PROJ_TYPE_SUBTYPES, PROJ_TYPE_DESCRIPTIONS, PROJ_TYPE_OUTPUT_DETAILS,
                        getChoiceHeading_doc_subtype, getChoiceHeading_doc_topic, getChoiceHeading_doc_len,
                        getPropQuestionText, getPropQuestionLeadIn,
                        getDocBasecampTopText, getDocBasecampSubText, getDocBasecampResponsesList,
                        getFlowBackUrlAttr, getFlowNextUrlAttr, getAttrName)
from .utils import defaultProjectSubtype
from .models import Project, Property

@login_required
def projectCreate(request):
    # test user email verification
    if not request.user.email_verified:
        return notificationView(request, NOTIF__EMAIL_UNVERIFIED)

    if request.method == 'POST':
        form = ProjectCreationForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.creator = request.user
            project.save()
            return redirect('project', project.slug)
        return notificationView(request, NOTIF__INVALID_DATA)
    else:
        # 'GET': return to home:project-create
        return redirect(f"/?action=create")

@login_required
def project(request, slug):
    try:
        project = Project.objects.get(slug=slug)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")

    # test if user has access to project (currently only the creator has access)
    if project.creator != request.user:
        raise PermissionDenied

    # test user email verification
    if not request.user.email_verified:
        return notificationView(request, NOTIF__EMAIL_UNVERIFIED)

    # test project stage
    if project.stage == PROJ_STAGE_STARTED:
        # do initial project setup
        project.setupBaseProperties(update_stage=True)
        # send doc subtype page
        return projectSubTypeView(request, project)
    elif project.stage == PROJ_STAGE_INIT_QUESTIONS:
        return projectInitialQuestionsView(request, project)
    elif project.stage == PROJ_STAGE_BASECAMP:
        return projectBasecampView(request, project)

    return notificationView(request, NOTIF__FAILED_LOAD, getProjectPageExtraContext(project))

def projectInitialQuestionsView(request, project):
    if project.stage == PROJ_STAGE_BASECAMP:
        project.stage = PROJ_STAGE_INIT_QUESTIONS
        project.save()

    for n, q in PROJ_INIT_QUESTIONS_FLOW.items():
        if q['ID'] == INIT_Q_TITLE and not project.title:
            return projectTitleView(request, project)
        elif q['ID'] == INIT_Q_TYPE and not project.doc_type:
            return projectTypeView(request, project)
        elif q['ID'] == INIT_Q_SUBTYPE and not project.doc_subtype:
            return projectSubTypeView(request, project)
        elif q['ID'] == INIT_Q_DOC_LEN and not project.doc_len:
            return projectDocLenView(request, project)
        elif q['ID'] == INIT_Q_DOC_TOPIC and not project.doc_topic:
            return projectDocTopicView(request, project)
        elif q['ID'] == INIT_Q_PROP:
            for p in q['STEPS']:
                try:
                    prop = project.props.get(name=p)
                except Property.DoesNotExist:
                    return notificationView(request, NOTIF__FAILED_LOAD, getProjectPageExtraContext(project))
                if not prop.response:
                    return projectPropertyView(request, project, prop)

    # if all questions done, set project stage to basecamp
    # if here, all initial questions have been answered, update project stage, return document basecamp
    if project.stage == PROJ_STAGE_INIT_QUESTIONS:
        project.stage = PROJ_STAGE_BASECAMP
        project.save()
        return projectBasecampView(request, project)

    # some error has occurred
    return notificationView(request, NOTIF__FAILED_LOAD, getProjectPageExtraContext(project))

def projectTitleView(request, project, additional_context=None):
    burl, battr = getFlowBackUrlAttr(INIT_Q_TITLE)
    context = {
        'project': project,
        'page_project': True,
        'sidebar_initial_collapsed': True,
        'QUESTION_TEXT': "What would you like to call your new project?",
        'QUESTION_LEADIN': "The name of my document is...",
        'CONTENT_PAGE_PATH': "common/home.pages/content.html",
        'PROJ_TYPE_CHOICES': PROJ_TYPE_CHOICES,
        'PROJ_TYPE_SVGS': PROJ_TYPE_SVGS,
        'PROJ_TYPE_SUBTYPES': PROJ_TYPE_SUBTYPES,
        'PROJ_TYPE_DESCRIPTIONS': PROJ_TYPE_DESCRIPTIONS,
        'PROJ_TYPE_OUTPUT_DETAILS': PROJ_TYPE_OUTPUT_DETAILS,
        'FORM_INPUT_NAME': 'title',
        'FORM_URL_NAME': 'project-update',
        'FORM_URL_ATTR': 'title',
        'BACK_URL': burl,
        'BACK_URL_ATTR': battr,
        'curr_value': project.title,
    }
    if additional_context: context.update(additional_context)
    return render (request, "projects/initial.pages/question.html", context)

def projectTypeView(request, project, additional_context=None):
    burl, battr = getFlowBackUrlAttr(INIT_Q_TYPE)
    context = {
        'project': project,
        'page_project': True,
        'sidebar_initial_collapsed': True,
        'CHOICE_HEADING': "Select your document type",
        'CHOICES': PROJ_TYPE_CHOICES,
        'CHOICE_SVGS': PROJ_TYPE_SVGS,
        'CONTENT_PAGE_PATH': "common/home.pages/content.html",
        'PROJ_TYPE_CHOICES': PROJ_TYPE_CHOICES,
        'PROJ_TYPE_SVGS': PROJ_TYPE_SVGS,
        'PROJ_TYPE_SUBTYPES': PROJ_TYPE_SUBTYPES,
        'PROJ_TYPE_DESCRIPTIONS': PROJ_TYPE_DESCRIPTIONS,
        'PROJ_TYPE_OUTPUT_DETAILS': PROJ_TYPE_OUTPUT_DETAILS,
        'FORM_INPUT_NAME': 'doc_type',
        'FORM_URL_NAME': 'project-update',
        'FORM_URL_ATTR': 'doc_type',
        'BACK_URL': burl,
        'BACK_URL_ATTR': battr,
        'curr_value': project.doc_type,
    }
    if additional_context: context.update(additional_context)
    return render (request, "projects/initial.pages/choice.html", context)

def projectSubTypeView(request, project, additional_context=None):
    burl, battr = getFlowBackUrlAttr(INIT_Q_SUBTYPE)
    context = {
        'project': project,
        'page_project': True,
        'sidebar_initial_collapsed': True,
        'CHOICE_HEADING': getChoiceHeading_doc_subtype(project),
        'CHOICES': PROJ_SUBTYPE_CHOICES_SEL[project.doc_type],
        'PROJECT_TYPE': PROJ_TYPE_LIST[project.doc_type],
        'PROJECT_SVG': PROJ_TYPE_SVGS[project.doc_type],
        'CONTENT_PAGE_PATH': "projects/initial.pages/content.subtype.html",
        'SIDEBAR_TYPE': 'CATEGORY',
        'SIDEBAR_DESCRPTION_HEADING': 'Document Subtype Description:',
        'SIDEBAR_DESCRPTIONS': PROJ_SUBTYPE_DESCRIPTIONS[project.doc_type],
        'FORM_INPUT_NAME': 'doc_subtype',
        'FORM_URL_NAME': 'project-update',
        'FORM_URL_ATTR': 'doc_subtype',
        'BACK_URL': burl,
        'BACK_URL_ATTR': battr,
        'curr_value': project.doc_subtype,
    }
    if additional_context: context.update(additional_context)
    return render (request, "projects/initial.pages/choice.html", context)

def projectDocTopicView(request, project, additional_context=None):
    burl, battr = getFlowBackUrlAttr(INIT_Q_DOC_TOPIC)
    context = {
        'project': project,
        'page_project': True,
        'sidebar_initial_collapsed': True,
        'CHOICE_HEADING': getChoiceHeading_doc_topic(project),
        'CHOICES': PROJ_TOPIC_CHOICES,
        'PROJECT_TYPE': PROJ_TYPE_LIST[project.doc_type],
        'PROJECT_SUBTYPE': PROJ_SUBTYPE_CHOICES_SEL_LIST[project.doc_type][project.doc_subtype],
        'PROJECT_SVG': PROJ_TYPE_SVGS[project.doc_type],
        'CONTENT_PAGE_PATH': "projects/initial.pages/content.topic.html",
        'SIDEBAR_DESCRPTIONS': PROJ_TOPIC_DESCRIPTIONS,
        'FORM_INPUT_NAME': 'doc_topic',
        'FORM_URL_NAME': 'project-update',
        'FORM_URL_ATTR': 'doc_topic',
        'BACK_URL': burl,
        'BACK_URL_ATTR': battr,
        'curr_value': project.doc_topic,
    }
    if additional_context: context.update(additional_context)
    return render (request, "projects/initial.pages/choice.html", context)

def projectDocLenView(request, project, additional_context=None):
    burl, battr = getFlowBackUrlAttr(INIT_Q_DOC_LEN)
    context = {
        'project': project,
        'page_project': True,
        'sidebar_initial_collapsed': True,
        'CHOICE_HEADING': getChoiceHeading_doc_len(project),
        'CHOICES': PROJ_DOCSIZE_CHOICES,
        'PROJECT_TYPE': PROJ_TYPE_LIST[project.doc_type],
        'PROJECT_SUBTYPE': PROJ_SUBTYPE_CHOICES_SEL_LIST[project.doc_type][project.doc_subtype],
        'PROJECT_SVG': PROJ_TYPE_SVGS[project.doc_type],
        'CONTENT_PAGE_PATH': "projects/initial.pages/content.len.html",
        'SIDEBAR_DESCRPTIONS': PROJ_DOCSIZE_DESCRIPTIONS,
        'FORM_INPUT_NAME': 'doc_len',
        'FORM_URL_NAME': 'project-update',
        'FORM_URL_ATTR': 'doc_len',
        'BACK_URL': burl,
        'BACK_URL_ATTR': battr,
        'curr_value': project.doc_len,
    }
    if additional_context: context.update(additional_context)
    return render (request, "projects/initial.pages/choice.html", context)

def projectPropertyView(request, project, prop, additional_context=None):
    burl, battr = getFlowBackUrlAttr(INIT_Q_PROP, prop.name)
    context = {
        'project': project,
        'page_project': True,
        'sidebar_initial_collapsed': True,
        'QUESTION_TEXT': getPropQuestionText(project, prop.name),
        'QUESTION_LEADIN': getPropQuestionLeadIn(project, prop.name),
        'PROJECT_TYPE': PROJ_TYPE_LIST[project.doc_type],
        'PROJECT_SUBTYPE': PROJ_SUBTYPE_CHOICES_SEL_LIST[project.doc_type][project.doc_subtype],
        'PROJECT_SVG': PROJ_TYPE_SVGS[project.doc_type],
        'CONTENT_PAGE_PATH': "projects/initial.pages/content.prop.html",
        'PROP_NAME': prop.name,
        'FORM_INPUT_NAME': prop.name,
        'FORM_URL_NAME': 'project-prop-update',
        'FORM_URL_ATTR': prop.name,
        'BACK_URL': burl,
        'BACK_URL_ATTR': battr,
        'curr_value': prop.response,
    }
    if additional_context: context.update(additional_context)
    return render (request, "projects/initial.pages/question.html", context)

def projectBasecampView(request, project, additional_context=None):
    burl, battr = getFlowBackUrlAttr(None)
    context = {
        'project': project,
        'page_project': True,
        'sidebar_initial_collapsed': True,
        'TOP_TEXT': getDocBasecampTopText(project),
        'SUB_TEXT': getDocBasecampSubText(project),
        'RESPONSES_LIST': getDocBasecampResponsesList(project),
        'PROJECT_TYPE': PROJ_TYPE_LIST[project.doc_type],
        'PROJECT_SUBTYPE': PROJ_SUBTYPE_CHOICES_SEL_LIST[project.doc_type][project.doc_subtype],
        'PROJECT_SVG': PROJ_TYPE_SVGS[project.doc_type],
        'FORM_INPUT_NAME': 'stage',
        'FORM_INPUT_VAL': PROJ_STAGE_STRUCTURING,
        'FORM_URL_NAME': 'project-update',
        'FORM_URL_ATTR': 'stage',
        'BACK_URL': burl,
        'BACK_URL_ATTR': battr,
    }
    if additional_context: context.update(additional_context)
    return render (request, "projects/initial.pages/basecamp.html", context)


def projectPropertyUpdateView(request, slug, propname):
    try:
        project = Project.objects.get(slug=slug)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    
    # test if user has access to project (currently only the creator has access)
    if project.creator != request.user:
        raise PermissionDenied

    # test user email verification
    if not request.user.email_verified:
        return notificationView(request, NOTIF__EMAIL_UNVERIFIED)

    try:
        prop = project.props.get(name=propname)
    except Property.DoesNotExist:
        raise SuspiciousOperation

    if request.method == 'POST':
        prop_val = request.POST.get(propname, None)
        force_next = request.POST.get('force_next', None)
        if prop_val:
            prop.response = prop_val
            prop.save()
            if force_next:
                nurl, nattr = getFlowNextUrlAttr(INIT_Q_PROP, prop.name)
                return redirect(nurl, project.slug, nattr) if nattr else redirect(nurl, project.slug) 
            return redirect('project', project.slug)
        return notificationView(request, NOTIF__INVALID_DATA)
    else:
        if project.stage == PROJ_STAGE_BASECAMP:
            project.stage = PROJ_STAGE_INIT_QUESTIONS
            project.save()
        return getFlowRender(request, project, INIT_Q_PROP, prop.name)

    raise SuspiciousOperation

def projectUpdateView(request, slug, attr):
    try:
        project = Project.objects.get(slug=slug)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    
    # test if user has access to project (currently only the creator has access)
    if project.creator != request.user:
        raise PermissionDenied

    # test user email verification
    if not request.user.email_verified:
        return notificationView(request, NOTIF__EMAIL_UNVERIFIED)

    if request.method == 'POST':
        attr_val = request.POST.get(attr, None)
        force_next = request.POST.get('force_next', None)
        if attr_val:
            updated = False
            if attr == 'title': 
                if attr_val != project.title:
                    project.title = attr_val
                    updated = True
            elif attr == 'doc_type': 
                if attr_val != project.doc_type:
                    project.doc_type = attr_val
                    project.doc_subtype = None
                    updated = True
            elif attr == 'doc_subtype':
                if attr_val != project.doc_subtype:
                    project.doc_subtype = attr_val
                    updated = True
            elif attr == 'doc_topic':
                if attr_val != project.doc_topic:
                    project.doc_topic = attr_val
                    updated = True
            elif attr == 'doc_len':
                if attr_val != project.doc_len:
                    project.doc_len = attr_val
                    updated = True
            elif attr == 'stage':
                if attr_val != project.stage:
                    project.stage = attr_val
                    updated = True
            else:
                return notificationView(request, NOTIF__INVALID_DATA)
            if updated: project.save()
            if force_next:
                nurl, nattr = getFlowNextUrlAttr(getAttrName(attr))
                return redirect(nurl, project.slug, nattr) if nattr else redirect(nurl, project.slug) 
            return redirect('project', project.slug)
        return notificationView(request, NOTIF__INVALID_DATA)
    else:
        if project.stage == PROJ_STAGE_BASECAMP:
            project.stage = PROJ_STAGE_INIT_QUESTIONS
            project.save()
        return getFlowRender(request, project, getAttrName(attr))

    raise SuspiciousOperation

def getProjectPageExtraContext(project, additional=None):
    extra = {
        'project': project,
        'page_project': True,
    }
    if additional: extra.update(additional)
    return extra

def getFlowRender(request, project, curr, step=None):
    additional = {   
        'FORCE_NEXT': True,
    }
    for n, q in PROJ_INIT_QUESTIONS_FLOW.items():
        if q['ID'] == curr:
            if q['ID'] == INIT_Q_TITLE:
                return projectTitleView(request, project, additional)
            elif q['ID'] == INIT_Q_TYPE:
                return projectTypeView(request, project, additional)
            elif q['ID'] == INIT_Q_SUBTYPE:
                return projectSubTypeView(request, project, additional)
            elif q['ID'] == INIT_Q_DOC_LEN:
                return projectDocLenView(request, project, additional)
            elif q['ID'] == INIT_Q_DOC_TOPIC:
                return projectDocTopicView(request, project, additional)
            elif q['ID'] == INIT_Q_PROP:
                for p in q['STEPS']:
                    if p == step:
                        try:
                            prop = project.props.get(name=p)
                        except Property.DoesNotExist:
                            return notificationView(request, NOTIF__FAILED_LOAD, getProjectPageExtraContext(project, additional))
                        return projectPropertyView(request, project, prop, additional)
    # if here, will probably be forwarded to basecamp
    return redirect('project', project.slug)