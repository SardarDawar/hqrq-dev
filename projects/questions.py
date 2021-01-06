# Questions at beginning of process to determine all initial variables and determine which method to deploy and which output format to use
from  .scripts import variableLibrary as vl
import inflect
from .scripts import topic_expressor as te
from .scripts import  heirarchydummy as hmd
p = inflect.engine()
import spacy
nlp = spacy.load("en_core_web_sm")

proposalWordOutcome = 'impact'

def question(
        firstName = "HQRQ", 
        projectName = "Tesla", 
        masterDocTypeIndex = 1,
        detailedDoctype = 1,
        targetReader = "HQRQ",
        subjectType = 1,
        subjectName = "HQRQ",
        affectedBy =  "HQRQ",
        actionOrImpression = "HQRQ",
        affectingOn = "HQRQ",
        docLengthChoice = 1
    ):
    # ! FIRST NAME
    firstName = firstName[0].upper() + firstName[1 : ]
    if firstName[-1] == " " :
        firstName = firstName[:-1]
    if firstName[-1] == "." :
        firstName = firstName[:-1]
    if firstName[-1] == "," :
        firstName = firstName[:-1]
    vl.fname = firstName

    # ! PROJECT NAME
    vl.projectName = projectName

    # !  TYPE OF DOCUMENT
    q2 = "So what type of document is your " + projectName + "? Select box below."
    vl.masterDocTypeSelection = masterDocTypeIndex
    chosenDoctype = vl.doc_list1[masterDocTypeIndex]
    chosenDoctype = chosenDoctype.lower()
    question = te.q_what(chosenDoctype)
    listofsubtypes = " ,".join(vl.doc_list2[masterDocTypeIndex])
    masterDocTypeDetail = vl.doc_list1_1[masterDocTypeIndex] 
    masterDocTypeOutputs = vl.doc_list1_2[masterDocTypeIndex]

    # ! SUB-TYPE OF DOCUMENT
    q3 = "What sort of " + question[1] + ", would you like to start creating?  Select from the dropdown list."
    docOptions = (vl.doc_list2[masterDocTypeIndex])
    detailedDoctypeDesc = vl.doc_list2_1[masterDocTypeIndex][detailedDoctype]

    # ! DOCUMENT SUBTYPE EXPRESSION
    detailedDoctypeSelected = vl.doc_list2[masterDocTypeIndex][detailedDoctype]
    detailedDoctypeExpression = te.q_what(detailedDoctypeSelected)
    try:
        dde = detailedDoctypeExpression[-1]
    except:
        dde = detailedDoctypeExpression

    # ! WHO IS TARGET READER
    q4 = firstName + ", who (what individual or group) will be reading your " + detailedDoctypeSelected + "?"
    q4leadin = "My " + detailedDoctypeSelected.lower() + " is ultimately for :  "

    # ! TARGET READER EXPRESSION
    targetReaderExpressed = te.q_what(targetReader)
    tRE = targetReaderExpressed[-1]

    # ! WHAT IS THE CATEGORY OF SUBJECT
    q5 = "What is the main subject or topic you would like to cover in this " + detailedDoctypeSelected + " for " + tRE + "?"
    q5leadin = "The main subject or topic for this " + detailedDoctypeSelected + " will be a..."
    subjectType = subjectType
    subjectTypeName = vl.userDefinedSubjectTypeOptions[subjectType]

    # ! QUESTION 6
    q6 = "What is the name of the " + subjectTypeName + " you would like to cover in this " + detailedDoctypeSelected + "?"
    q6leadin = "The name of the " + subjectTypeName + " to be covered in this document is..."
    subjectName = subjectName
    subjectExpression = te.q_what(subjectName)
    subjectExpressionJoin = subjectExpression[-1]
    subjectExpressionWhat = subjectExpression[2]
    subjectExpressionJoinLI = ""
    if (len(subjectExpression[4]) > 1)  :
        subjectExpressionJoinLI = subjectExpression[4]
    else:
        subjectExpressionJoinLI = subjectExpressionJoin
    test = subjectExpressionJoin[0].upper()
    test1 = subjectExpressionJoin[1:]
    subjectExpressonStartSentence = test + test1

    # ! QUESTION 8
    q8 = "Who or what is most " + "impacted by the " + vl.userDefinedSubjectTypeOptions[subjectType] + " - '" + subjectName + "'?"
    q8leadin = subjectExpressonStartSentence + " will have the greatest " + "impact on..."
    affectedBy = affectedBy
    affectedBy = te.q_what(affectedBy)
    affectedByExpression = affectedBy[-1]

    # ! QUESTION 10
    q10 = "What action or impression do you want " + tRE + " to have as a result of reading this " + detailedDoctypeSelected +" on " + subjectExpressionJoin + "?"
    q10leadin = "I would like " + tRE + " to...  "
    actionOrImpression = actionOrImpression
    if actionOrImpression[0 : 1] == "to":
        actionOrImpression = actionOrImpression[2:]

    # ! QUESTION 9
    q9 = "Who or what is affecting, causing or creating" + " " + subjectExpressionJoin + "?"
    q9leadin = subjectExpressionJoin.capitalize()[0] + subjectExpressionJoin[1:] + " will be impacted by...  "
    affectingOn = affectingOn
    affectingOn = te.q_what(affectingOn)
    affectingOnExpression = affectingOn[-1]

    # ! QUESTION 11 - DOC LENGTH
    q11 = "Thanks " + firstName + ",I now have a much better understanding of what you are looking to do.  \nHow long (approximately) would you like your " + chosenDoctype + " to be?"
    docLengthChoice = docLengthChoice
    endingLevel = vl.docOptionsIndex[docLengthChoice]

    # ! CHECKPOINT
    sEWPlural = ""
    if subjectExpressionWhat.find("are") == 0 :
        sEWPlural = "s"

    presentedTense = (vl.primaryTense)
    autoTense = vl.doc_list3_2[masterDocTypeIndex][0]
    vl.masterDocTypeIndex = autoTense
    selectedTense = autoTense
    autoOrientation = vl.doc_list3_2[masterDocTypeIndex][1]
    vl.proposalWordsOutcome = vl.pwoLists[vl.selectedOrientation]
    for el in vl.proposalWordsOutcome :
        vl.proposalWordsOutcomesPossibilities[el] = []
        for i in range(3):
            global lemm
            lemm = el
            if(i == 0) :
                doc = nlp(el)
                for token in doc:
                        lemm = token.lemma_
                vl.proposalWordsOutcomesPossibilities[el] .append(lemm)
            if(i == 1) :
                if(el[-1] == 'e'):
                    lemm = el + "d"
                elif(el[-1] != "e") :
                    lemm = el + "ed"
                vl.proposalWordsOutcomesPossibilities[el] .append(lemm)
            if(i == 2) :
                if(el[-1] == "e") :
                    lemm = el[0:len(el) - 1] + "ing"
                else :
                    lemm = el + "ing"
                vl.proposalWordsOutcomesPossibilities[el] .append(lemm)
    selectedOrientationText = vl.primaryOrientation[vl.selectedOrientation]
    p11subhead = (chosenDoctype + " brief\n")
    p11header = "The way I see it " + firstName + ", is that you are looking to develop " + dde + " that will be read primarily by " + tRE + ".  \n" + subjectExpressionJoin.capitalize()[0] + subjectExpressionJoin[1:] + " " + subjectExpressionWhat + " the primary subject" + sEWPlural + "/topic" + sEWPlural +" that will be covered in this " + chosenDoctype + ".\nThe main goal of this document is for " + tRE + " to " + actionOrImpression + ".  "
    p11body = "\nThis document will clearly and succinctly communicate how " + subjectName + " will impact " + selectedOrientationText + " on " + affectedByExpression + ".\n\nOk let's go."
    firstName = firstName
    projectName = projectName
    vl.masterDocTypeIndex  = masterDocTypeIndex
    vl.chosenDoctype  = chosenDoctype
    vl.listofsubtypes  = listofsubtypes
    vl.masterDocTypeDetail  = masterDocTypeDetail
    vl.masterDocTypeOutputs = masterDocTypeOutputs
    vl.detailedDoctype  = detailedDoctype
    vl.detailedDoctypeSelected = detailedDoctypeSelected
    vl.detailedDoctypeDesc  = detailedDoctypeDesc
    vl.dde = dde
    vl.targetReader= targetReader
    vl.tRE = tRE
    vl.subjectType = subjectType
    vl.subjectTypeName = subjectTypeName
    vl.subjectName= subjectName
    vl.subjectExpressionJoin = subjectExpressionJoin
    vl.subjectExpressonStartSentence = subjectExpressonStartSentence
    vl.subjectExpressionJoinLI = subjectExpressionJoinLI                                      # subject expression for use in leadin text (me you in particular)

    #Tense Provided by user
    vl.selectedTense = selectedTense                                                # Selected tense in english
    vl.autoTense = autoTense                                                    # machine selected tense based on doctype

    #Selected Orientation
    vl.selectedOrientation                                       # index of the selected orientation
    vl.selectedOrientationText= selectedOrientationText                                      # text associated with the selected orientation - Positively - Negativly -  Neutrally

    #Who is affected by the subject
    vl.affectedBy = affectedBy                                                   # affected by as entered by user
    vl.affectedByExpression = affectedByExpression                                         # affected by as expressed by topic expressor

    # Who is impacting on the subject
    vl.affectingOn = affectingOn                                                  # affecting on as entered by user
    vl.affectingOnExpression= affectingOnExpression                                        # affecting on as expressed

    #action or impression desired on Target Reader as a result of covering subject
    vl.actionOrImpression = actionOrImpression                                           # action or impression as entered by user.  Preceded by word "To"

    # Document Length and Document Level
    vl.docLengthChoice = docLengthChoice                                              # selected choice by user (index)
    vl.endingLevel = endingLevel                                                  # level at which to terminate heirarchy

    #heirarchy1 = hmv.heirarchyMaster(firstName, masterDocTypeIndex,docLengthChoice, endingLevel, affectedByExpression, subjectExpressionJoin )


    # hmv.heirarchyMaster(firstName,masterDocTypeIndex,docLengthChoice,endingLevel,affectedByExpression, subjectExpressionJoin)
    # print("="*70)
    # print("Script is in running state")
    # print("selected orientationtext",vl.selectedOrientationText)
    #  hmd.heirarchyDummy(firstName,masterDocTypeIndex,docLengthChoice,endingLevel,affectedByExpression, subjectExpressionJoin)
    return hmd.heirarchyDummy(firstName = firstName, tenseChoice = masterDocTypeIndex, docLengthChoice = docLengthChoice,endingLevel = endingLevel, userDefinedProspect = affectedByExpression, userDefinedSubject = subjectExpressionJoin)
    # print((filteredQuestionList, leadingText, postQuestionMessage))
    # for index in range(len(filteredQuestionList)) :
    #     print(filteredQuestionList[index])
    #     print(leadingText[index])
    #     if(not postQuestionMessage.get(index) == "") :
    #         print(postQuestionMessage.get(index))
    #         # return vl.postQuestionMessage.get(index)
    #     else :
    #         print("Message is empty - No message")
    # print(response)
    # print("="*70)