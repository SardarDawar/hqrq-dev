import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, JsonResponse
from django.core.exceptions import SuspiciousOperation, PermissionDenied
from .notifications import *
from .forms import ProjectCreationForm
from common.views import notificationView
from .vars import *
from .content import (  PROJ_SUBTYPE_DESCRIPTIONS, PROJ_TYPE_LIST, PROJ_SUBTYPE_CHOICES_SEL_LIST,
                        PROJ_TOPIC_DESCRIPTIONS, PROJ_DOCSIZE_DESCRIPTIONS,
                        PROJ_TYPE_SVGS, PROJ_TYPE_SUBTYPES, PROJ_TYPE_DESCRIPTIONS, PROJ_TYPE_OUTPUT_DETAILS,
                        getChoiceHeading_doc_subtype, getChoiceHeading_doc_topic, getChoiceHeading_doc_len,
                        getPropQuestionText, getPropQuestionLeadIn,
                        getDocBasecampTopText, getDocBasecampSubText, getDocBasecampResponsesList,
                        getFlowBackUrlAttr, getFlowNextUrlAttr, getAttrName,
                        getTip_title, getTip_doc_type, getTip_doc_sutype, getTip_doc_topic, getTip_doc_len,
                        getTip_basecamp, getTip_prop,
                        getQuestionsDict, getChoiceHeading_topics, getTopicsChoiceList)
from .utils import defaultProjectSubtype
from .models import Project, Property
import json
from django.db import transaction
from .questions import *
from .scripts import heirarchydummy
# from  .scripts import variableLibrary as vl


# Past, Present, Future
verbForm = [
    "",
    "past",
    'present',
    'future'
]

pwoListsViews = [
    '',
    'positive',
    'negative',
    'neutral'
]

def display_print(msg):
    print("="*70)
    print(msg)
    print("="*70)


def breakSentence(q):
    q = q.split(" ")
    for i in q:
        if i== " " or i == "":
            q.remove(i)
    # q = q[:-1]
    wQuestions = ['what', 'when', 'where', 'how', 'why']
    vWords= ['should', 'will', 'can', 'does', 'is', 'could', 'present' , 'past', "future"]
    articles = ["a","the"]
    mWords = ["impact","alter","form","change", "positive","negative", "neutral"]
    updatedTense = ""
    userDefinedSubject = ""
    updatedPWOIndex = ""
    userDefinedProspect = ""
    dummyWord = ""

    # ! Remove Questions Words
    for i in q:
        if i.strip().lower() in wQuestions:
            q.remove(i)
            break
    
    # ! Remove Verb Words
    # display_print(q)
    for i in q:
        # display_print()
        if i.strip().lower() in vWords:
            # display_print(i)
            updatedTense = ""
            updatedTense = i
            q.remove(i)
            break

    # ! User Defined Subject
    for index in range(0, len(q)):
        # ? With Articles
        if q[index].strip().lower() in articles:
            userDefinedSubject = ""
            for i in range(index, len(q)):
                if(q[index].strip().lower() in mWords or q[index].strip() == '?'):
                    break
                else:
                    dummyWord += q[index] + " "
                    q.remove(q[index])
                    i = i-1
            userDefinedSubject = dummyWord.strip()
            break
        else:
            # ? Without Articles
            for i in range(index, len(q)):
                if(q[index].strip().lower() in mWords or q[index].strip() == '?'):
                    break
                else:
                    dummyWord += q[index] + " "
                    q.remove(q[index])
                    i = i-1
            userDefinedSubject = dummyWord.strip()
            break

    dummyWord = ""
    
    # ! Check if it is last element
    # ! if it is "?"
    if(len(q) == 1):
        if q[0] == "?":
            q.remove(q[0]) 


    # ! Orientation
    if(len(q) != 0):
        if q[0].strip().lower() in mWords:
            updatedPWOIndex = q[0]
            q.remove(q[0])
    

    display_print(q)

    if(len(q) != 0):
        userDefinedProspect=""
        for index in range(0, len(q)):
            if(q[index].strip() == "?"):
                userDefinedProspect = dummyWord.strip()
                break
            else:
                dummyWord += q[index] + " "
            
        dummyWord = ""
        
    return (updatedTense, userDefinedSubject, updatedPWOIndex, userDefinedProspect)



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
    elif project.stage == PROJ_STAGE_STRUCTURING:
        return redirect('project-subq', project.slug)

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
        'PAGE_TIP': getTip_title(),
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
        'PAGE_TIP': getTip_doc_type(),
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
        'PAGE_TIP': getTip_doc_sutype(project),
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
        'PAGE_TIP': getTip_doc_topic(),
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
        'PAGE_TIP': getTip_doc_len(),
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
        'PAGE_TIP': getTip_prop(project, prop.name),
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
        'PAGE_TIP': getTip_basecamp(),
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
        prop_val = prop_val.strip()
        if prop_val:
            if not prop.response:
                prop.response = prop_val
                prop.save()
            elif prop_val.lower() != prop.response.lower():
                prop.updateExpressedResponse(prop_val)
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

def projectPropertyUpdate_AJAX(request):
    if not (request.method == 'POST' and request.is_ajax() and request.user.is_authenticated):
        return JsonResponse({"updated": False, "message": "Not Authorized"})
    
    project_id = request.POST.get('project_id', None)
    responses = request.POST.get('responses', None)
    if not project_id or not responses:
        return JsonResponse({"updated": False, "message": "Invalid Data"})
    try:
        project_id = int(project_id)
        responses = json.loads(responses)
    except ValueError:
        return JsonResponse({"updated": False, "message": "Invalid Data"})
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return JsonResponse({"updated": False, "message": "Invalid Data"})
    # test user email verification
    # test if user has access to project (currently only the creator has access)
    if not request.user.email_verified or project.creator != request.user:
        return JsonResponse({"updated": False, "message": "Not Authorized"})
    updated_list = []
    with transaction.atomic():
        for p, r in responses.items():
            r = r.strip()
            if not r:
                return JsonResponse({"updated": False, "message": "Invalid Data"})
            try:
                prop = project.props.get(name=p)
            except Property.DoesNotExist:
                return JsonResponse({"updated": False, "message": "Invalid Data"})
            if prop.response_exp != r:
                prop.updateExpressedResponse(r)
                updated_list.append(p.name)
    # updated
    data = {
        'updated': True,
        'updated_list': updated_list,
        'responses_text': getDocBasecampResponsesList(project),
        'message': 'Successfully updated responses',
    }
    return JsonResponse(data)

def projectPropertyExpUpdate_AJAX(request):
    if not (request.method == 'POST' and request.is_ajax() and request.user.is_authenticated):
        return JsonResponse({"updated": False, "message": "Not Authorized"})
    
    project_id = request.POST.get('project_id', None)
    responses = request.POST.get('responses', None)
    if not project_id or not responses:
        return JsonResponse({"updated": False, "message": "Invalid Data"})
    try:
        project_id = int(project_id)
        responses = json.loads(responses)
    except ValueError:
        return JsonResponse({"updated": False, "message": "Invalid Data"})
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return JsonResponse({"updated": False, "message": "Invalid Data"})
    # test user email verification
    # test if user has access to project (currently only the creator has access)
    if not request.user.email_verified or project.creator != request.user:
        return JsonResponse({"updated": False, "message": "Not Authorized"})
    updated_list = []
    with transaction.atomic():
        for p, rexp in responses.items():
            rexp = rexp.strip()
            if not rexp:
                return JsonResponse({"updated": False, "message": "Invalid Data"})
            try:
                prop = project.props.get(name=p)
            except Property.DoesNotExist:
                return JsonResponse({"updated": False, "message": "Invalid Data"})
            if prop.response_exp != rexp:
                prop.updateUnexpressedResponse(rexp)
                updated_list.append(prop.name)
    # updated
    data = {
        'updated': True,
        'updated_list': updated_list,
        'responses_text': getDocBasecampResponsesList(project),
        'message': 'Successfully updated responses',
    }
    return JsonResponse(data)

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


@login_required
def PROJECTSEDITQUESTIONAJAX(request):
    # display_print(request.GET)
    q = request.GET['name']
    Tense = 1
    Orientation = 1

    # Questions
    questionsDict = {}

    # Question Leading Text..
    questionLeadingText = {}
    try:
        project = Project.objects.get(id=int(request.GET['project_id']))
        (updatedTense, userDefinedSubject, updatedPWOIndex, userDefinedProspect) = breakSentence(q)
        # project.getPROP_TOPIC_NAME()
        
        # display_print(project.setPROP_TOPIC_NAME(userDefinedSubject)
        display_print((updatedTense, userDefinedSubject, updatedPWOIndex, userDefinedProspect))
        # display_print(updatedTense)
        # )
        
        # ? Set Prohect User Defined Subject
        project.setPROP_TOPIC_NAME(userDefinedSubject)

        # ? Set Project User Defined Prospect
        # display_print(userDefinedProspect)
        if userDefinedProspect.strip().lower() == "":
            
            # display_print(project.getPROP_TOPIC_IMPACT())
            userDefinedProspect = project.getPROP_TOPIC_IMPACT()
        else:
            project.setPROP_TOPIC_IMPACT(userDefinedProspect)


        # display_print(updatedTense.strip().lower())
        # Update Sentence Tense Form
        if updatedTense.strip().lower() in verbForm:
            Tense = verbForm.index(updatedTense.strip().lower())
            # display_print(Tense)

        if  updatedPWOIndex.strip().lower() in pwoListsViews:
            Orientation = pwoListsViews.index(updatedPWOIndex.strip().lower())

        updatedQuestions = heirarchydummy.updatedExistingQuestion(userDefinedSubject, userDefinedProspect, Tense , Orientation)
        # display_print(updatedQuestions)
        (filteredQuestionList, leadingText, postQuestionMessage) = updatedQuestions
        # display_print((filteredQuestionList, leadingText, postQuestionMessage))
        for index in range(len(filteredQuestionList)) :
            questionsDict[index] = filteredQuestionList[index]
            questionLeadingText[index] = leadingText[index]

        # ! Save script generated questions and questions leading text to the database
        project.generatedQuestions = questionsDict
        project.generatedQuestionsLeadingText = questionLeadingText
        project.save()
        # display_print(project.getQuestoins())



        return JsonResponse(json.loads( json.dumps( {"QUESTIONS_DICT_AJAX" : questionsDict, "QUESTION_LEADING_TEXT_AJAX":  questionLeadingText})), status=200)

    except Exception as e:
        display_print(e)
        return JsonResponse(json.loads( json.dumps( {"instance": 'error'})), status=400)
    


@login_required
def projectSubquestions(request, slug):
    # !Question Dictionary ... 
    questionsDict = {}

    # Question Leading Text..
    questionLeadingText = {}

    # Answer for the Questions

    answersDict = {}
    try:
        project = Project.objects.get(slug=slug)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    
    if request.method == 'POST':
        # display_print(request.POST)
        project.generatedAnswers = json.loads(request.POST["answer_dict"])
        project.save()
        return redirect('project-topics', project.slug)



    # ! Find Index for 'masterDocTypeIndex
    # print("="*70)
    # print(subject_type_list.index(project.doc_topic))
    # print(project.getPROP_TARGET_READER_RESPONSE())
    # print("="*70)
    docLengthOptions = {"PDS_1" : 2, "PDS_UPTO_5" : 3, "PDS_UPTO_20" : 4, "PDS_UNLIMITED" : 5}


    # ! Check if the questions for the current project exists or not...
    # ! Check if the question leading text exists for the proejct
    if(len(project.getQuestoins()) == 0 or  project.getQuestoins().strip() == "" or len(project.getQuestionsLeadingText()) == 0 or  project.getQuestionsLeadingText().strip() == ""):
        # Question for the Script...
        (filteredQuestionList, leadingText, postQuestionMessage) =  question(
            firstName = request.user.email,
            projectName = project.title,
            masterDocTypeIndex = doc_list_1.index(project.doc_type),
            detailedDoctype = sub_type_list.index(project.doc_subtype),
            targetReader = project.getPROP_TARGET_READER_RESPONSE(),
            subjectType = subject_type_list.index(project.doc_topic),
            subjectName = project.getPROP_TOPIC_NAME(),
            affectedBy =  project.getPROP_TOPIC_IMPACT(),
            actionOrImpression = project.getPROP_TOPIC_CAUSE(),
            affectingOn = project.getPROP_TARGET_IMPRESSION(),
            docLengthChoice = docLengthOptions[project.doc_len]
        )
        for index in range(len(filteredQuestionList)) :
            questionsDict[index] = filteredQuestionList[index]
            questionLeadingText[index] = leadingText[index]

        # display_print((filteredQuestionList, leadingText, postQuestionMessage))

        # ! Save script generated questions and questions leading text to the database
        project.generatedQuestions = questionsDict
        project.generatedQuestionsLeadingText = questionLeadingText
        # display_print(project.getAnswers())
        project.save()

    # ! Create and Save an Answer Object when asnwrs are not provided
    if(len(project.getAnswers()) == 0 or project.getAnswers().strip() == ""):
        project.generatedAnswers = project.generatedQuestionsLeadingText
        A = eval(str(project.generatedAnswers))
        for i in A:
            if(len(A[i])!=0):
                for j in range(0, len(A[i])):
                    A[i][j] = ""
            else:
                A[i] = ""
        project.generatedAnswers = A
        project.save()
    # display_print(project.getAnswers())

    # GET
    burl, battr = getFlowBackUrlAttr(None)
    prop_topic_name_response = project.getPROP_TOPIC_NAME()
    context = {
        'project': project,
        'page_project': True,
        'sidebar_initial_collapsed': True,

        'QUESTION_TEXT': f"What is {prop_topic_name_response}",
        'QUESTION_LEADIN': f"{prop_topic_name_response} is...",
        "CONTENT_PAGE_PATH": "projects/struct.pages/content.subquestions.html",
        'PAGE_TIP': "",
        
        'PROJECT_TYPE': PROJ_TYPE_LIST[project.doc_type],
        'PROJECT_SUBTYPE': PROJ_SUBTYPE_CHOICES_SEL_LIST[project.doc_type][project.doc_subtype],
        'PROJECT_SVG': PROJ_TYPE_SVGS[project.doc_type],

        'FORM_INPUT_NAME': "",
        'FORM_URL_NAME': 'project-prop-update',
        'FORM_URL_ATTR': "project-subq",
        'BACK_URL': burl,
        'BACK_URL_ATTR': battr,
        "PROJECT_TOPIC_NAME": prop_topic_name_response,

        # ! Question
        "QUESTIONS_DICT": eval(str(project.generatedQuestions)), 

        # ! Question Leading Text
        "QUESTION_LEADING_TEXT" : eval(str(project.getQuestionsLeadingText())),

        # ! Answer 
        "ANSWER_DICT" : eval(str(project.getAnswers()))
    }

    return render(request, "projects/struct.pages/subquestions.html", context)

def projectTopics(request, slug):
    try:
        project = Project.objects.get(slug=slug)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    
    ch_head, ch_subtext, ch_minsel_count = getChoiceHeading_topics(project) 
    context = {
        'project': project,
        'page_project': True,
        'sidebar_initial_collapsed': True,

        'CHOICE_HEADING': ch_head,
        'CHOICE_SUBTEXT': ch_subtext,
        "CHOICES": getTopicsChoiceList(project),
        "CHOICE_MINSEL_COUNT": ch_minsel_count,

        "CONTENT_PAGE_PATH": "projects/struct.pages/content.topics.html",
        'PAGE_TIP': "",
        
        'PROJECT_TYPE': PROJ_TYPE_LIST[project.doc_type],
        'PROJECT_SUBTYPE': PROJ_SUBTYPE_CHOICES_SEL_LIST[project.doc_type][project.doc_subtype],
        'PROJECT_SVG': PROJ_TYPE_SVGS[project.doc_type],

        'FORM_INPUT_NAME': "",
        'FORM_URL_NAME': 'project-prop-update',
        'FORM_URL_ATTR': "project-subq",
        'BACK_URL': "project-subq",
    }

    return render(request, "projects/struct.pages/topics.html", context)


# ! AJAX CALL TO SAVE ANSWERS
def PROJECT_ANSWER_SAVE(request):
    display_print("ANSWER AJAX CALL WORKING")
    return JsonResponse(json.loads( json.dumps( {"instace": "success"})), status=200)