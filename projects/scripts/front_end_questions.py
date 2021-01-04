# Questions at beginning of process to determine all initial variables and determine which method to deploy and which output format to use
import variableLibrary as vl
import inflect
import topic_expressor as te
p = inflect.engine()
import spacy
nlp = spacy.load("en_core_web_sm")
# import heirarchyx as hmv

proposalWordOutcome = 'impact'


#Page 0a - Q1 This will come from account details - firstname
firstName = input("What is your first name?:  ")
firstName = firstName[0].upper() + firstName[1 : ]
if firstName[-1] == " " :
    firstName = firstName[:-1]
if firstName[-1] == "." :
    firstName = firstName[:-1]
if firstName[-1] == "," :
    firstName = firstName[:-1]
vl.fname = firstName
#Page 0b - Name your project

q1 = "\nGreat, thanks " + firstName + ".  What would you like to call your new project?"
leadinText = "This project will be called..."
tip = "Tip: Name your project something that will help you identify it.  Note that with HyperQuestions, we will use your name throughout your document so pick something that also reads well"
suggestion = "Thinking will help you to distil many of the concepts involved in your document and prepare you for the process.  You can come back and change the document name before creating your document.  The document name will be used in your final document.  Here are some sample names to get you thinking: - Department of Defence HR Requirements - Microsoft Strategic Business Plan - Eucalypt Cultivation Guide - Plastic Products Overview"
# print(q1 + "\n" + tip + "\n" + suggestion + "\n" + leadinText)
projectName = input()
vl.projectName = projectName

#Page 1 - Q2 What mastere document type
q2 = "So what type of document is your " + projectName + "? Select box below."
# print("\n")

tip = "Tip: Once you select an option, a description of this type and its output formats will be displayed - this will help you be sure you have picked the best option.  Please consider carefully as each type may produce different outcomes – select one and see what it offers."
suggestion = "Select the closest category to your project.  What you are trying to create could be a sub-category (next page) - click and you will see the subtypes to help you select.  Your selection will potentially impact: - the method used for the remainder of the document creation process - the primary tense used in your document.  For example, a business proposal relates to the future. - your selection will impact the way in which key terms and inputs are interpreted by the HyperQuestions Ai Engine."
print(q2,"\n" + tip + "\n" + suggestion)
for x in range(len(vl.doc_list1)):
    print(x, vl.doc_list1[x])
masterDocTypeIndex = int(input("\nPlease enter Your choice (number) from the above list:  "))
vl.masterDocTypeSelection = masterDocTypeIndex

chosenDoctype = vl.doc_list1[masterDocTypeIndex]
chosenDoctype = chosenDoctype.lower()
question = te.q_what(chosenDoctype)
listofsubtypes = " ,".join(vl.doc_list2[masterDocTypeIndex])
print("\nIncludes the following :",listofsubtypes +"\nDescription\n" + vl.doc_list1_1[masterDocTypeIndex] + "\nOutputs\n" +vl.doc_list1_2[masterDocTypeIndex])
#Descriptions and breakdowns needed here for each content type - displayed on selection.
masterDocTypeDetail = vl.doc_list1_1[masterDocTypeIndex]     # detailed description of master doc type selected
masterDocTypeOutputs = vl.doc_list1_2[masterDocTypeIndex]
print("\n")

#Page2 - Q3 - what subtype of document
q3 = "What sort of " + question[1] + ", would you like to start creating?  Select from the dropdown list."
#update tip below to come from tip list
tip = "Tip: these are sub-options associated with your selection of " + question[1] + ".  Once you select an option further information about its method and approach will be displayed."
suggestion = "Detailed document types more specifically determine the method, document length and output format for your document.  Select a box to see the details of that option"
print(q3,"\n" + tip + "\n" + suggestion)
docOptions = (vl.doc_list2[masterDocTypeIndex])
for x in range(len(docOptions)):
    print(x, docOptions[x])
detailedDoctype = int(input("\nPlease enter Your choice (number) from the above list:  "))
detailedDoctypeDesc = vl.doc_list2_1[masterDocTypeIndex][detailedDoctype]
print(detailedDoctypeDesc)
# document subtype Expression
detailedDoctypeSelected = vl.doc_list2[masterDocTypeIndex][detailedDoctype]
detailedDoctypeExpression = te.q_what(detailedDoctypeSelected)
dde = detailedDoctypeExpression[-1]
print("\n")

#Page 3 - Question 4 - Who is target reader
q4 = firstName + ", who (what individual or group) will be reading your " + detailedDoctypeSelected + "?"
q4leadin = "My " + detailedDoctypeSelected.lower() + " is ultimately for :  "
tip = "Tip: This is your target reader - it can be an individual (e.g. Nicholas Tesla), a group (e.g. board of directors), a company (e.g. Microsoft), an industry or sector (e.g. manufacturing). Please use correct capitalisation and resist responses like 'everyone'...you may need to think specifically about who will be the target reader."
suggestion = "Considering and defining your “target reader” is one of the most critical steps in creating a great document that builds a bridge between your message and your intended outcome. Some example answers include: - investors - the board of directors - staff in the Human  Resources Division - website visitors who searched for XYZ Please don’t use one of the above unless it is the right answer in your situation."
print(q4 + "\n" + tip + "\n" + suggestion + "\n" + q4leadin)
targetReader = input()
print('\n')

# target reader expression
targetReaderExpressed = te.q_what(targetReader)
tRE = targetReaderExpressed[-1]



#Page 4 - Question 5 - What is the category of subject
q5 = "What is the main subject or topic you would like to cover in this " + detailedDoctypeSelected + " for " + tRE + "?"
q5leadin = "The main subject or topic for this " + detailedDoctypeSelected + " will be a..."
tip = "Tip: Select your subject/topic type from the table below, try for a best-fit approach if your topic crosses several types."
suggestion = "Choose the category of subject that you would like to cover in your document.  The category helps the HyperQuestions Ai engine better understand the sort of primary subject you are seeking to cover."
print(q5,"\n" + q5leadin + "\n" + tip)
subjectType = (vl.userDefinedSubjectTypeOptions)
for x in range(len(subjectType)):
    print(x, subjectType[x])
subjectType = int(input("\nPlease enter Your choice (number) from the above list:  "))
print("\n")
subjectTypeName = vl.userDefinedSubjectTypeOptions[subjectType]
####need here the english version of subjectType

#Page 5 - Question 6
q6 = "What is the name of the " + subjectTypeName + " you would like to cover in this " + detailedDoctypeSelected + "?"
q6leadin = "The name of the " + subjectTypeName + " to be covered in this document is..."
tip = "Tip: This is the main/primay subject in your document.  Think carefully about this as it will impact everything you do from now on.  You may not get it right at this time, and may need to come back and revise it once you see it presented in other contexts."
suggestion = "Consider that the name used here will appear in the document, so choose a name that will read well in the context of a sentence.  This name is effectively the core topic for your document and you will see it come up quite often. You will have the option to come-back and change the name once you have seen it used in the next few pages.  After a few more questions, you will soon reach ”Document Basecamp”, once you proceed past that page, you will no longer be able to return and edit these answers.  Click the ? icon for more tips."
print(q6,"\n" + tip + "\n" + suggestion +"\n" + q6leadin)
subjectName = input()
print("\n")

# if subjectName.lower().find("my ") == 0 :
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



#Page 7 - Question 8
q8 = "Who or what is most " + "impacted by the " + vl.userDefinedSubjectTypeOptions[subjectType] + " - '" + subjectName + "'?"
q8leadin = subjectExpressonStartSentence + " will have the greatest " + "impact on..."
tip = "Tip: Think of this in the context of your document - what you are trying to say about " + subjectExpressionJoin + ".  This can be a: person, division within an organisation, organisation/entity, place, product concept etc.  It could also be the target reader of your document (" + tRE + ").  Try to separate from target reader if possible.  Eg If target reader is board of a company, those affected could be the staff."
suggestion = "Understanding who is most impacted by your subject lets us understand the relationships involved in your document.  This helps the HyperQuestions AI engine to add value to the process and ensures you are presenting information about the impacts of the subject.  Note: This could also be your target reader. If it is also your target reader then enter the name."
print("\n" + q8 + "\n" + tip + "\n" + suggestion + "\n" + q8leadin)
affectedBy = input()
print("\n")

# affectedBy expression
affectedBy = te.q_what(affectedBy)
affectedByExpression = affectedBy[-1]


#Page 9 - Question 10
q10 = "What action or impression do you want " + tRE + " to have as a result of reading this " + detailedDoctypeSelected +" on " + subjectExpressionJoin + "?"
q10leadin = "I would like " + tRE + " to...  "
tip = "Tip: Example: I would like " + tRE + " to...(buy our product, visit our website, make x decision, feel informed, become more engaged etc)."
suggestion = "The action or impression is the ultimate outcome you wish to achieve as a result of producing this document. it could relate to: - an action by the target reader - a new level of understanding - empathy or a feeling about your topic.  Be specific if possible, as ultimately your document will be oriented around achieving this goal. Try to list only one primary goal.  If you have a few, try to summarise them to a higher-level goal."
print(q10,"\n" +  tip +"\n" + suggestion + "\n" + q10leadin)
actionOrImpression = input()
if actionOrImpression[0 : 1] == "to":
    actionOrImpression = actionOrImpression[2:]
print("\n")

#Page 8 - Question 9
q9 = "Who or what is affecting, causing or creating" + " " + subjectExpressionJoin + "?"
q9leadin = subjectExpressionJoin.capitalize()[0] + subjectExpressionJoin[1:] + " will be impacted by...  "
tip = "Tip: This is ideally something or someone that is driving change in " + subjectExpressionJoin + ".  It could be a person, team (e.g. marketing), regulation, place, product concept etc.  If you really get stuck, don't worry just use " + tRE + "."
suggestion = "This is the person, organisation or thing that is is having an impact on the achievement of your document goal or objective. Some sample answers include: - Web Development  - Swiss Bank Policy - Human Resources team.  Please don’t use the above and avoid using “Me” if the answer is really you then please use your name or your title in the context of the document (eg Director)."
print(q9 + "\n" + tip + "\n" + suggestion + "\n" + q9leadin )
affectingOn = input()
print("\n")

#affecting on expression
affectingOn = te.q_what(affectingOn)
#print(affectingOn)
affectingOnExpression = affectingOn[-1]





#Page 10 - Question 11 - doc Length
q11 = "Thanks " + firstName + ",I now have a much better understanding of what you are looking to do.  \nHow long (approximately) would you like your " + chosenDoctype + " to be?"
tip = "Tip: Document length is approximate and will be used to determine the number of topics and questions required (actual length is dependent on several factors including: document format, answer length and the number of skipped questions"
suggestion = "Sizing is approximate in HyperQuestions and will vary based on your answers to questions.  The above selection is not exact and may be + or - 30%.  Note: our sizing assumes approximately 250 words per page.  Pick the option that most closely reflects what you are looking to do. If you reach one page and want to keep going you can still create a 10,000-word document, but we will help to keep you on track."
print(q11,"\n" + tip + "\n" + suggestion + "ADD Lookup Value - description of doc length")
typeCount = 0
for key in vl.docLengthOptions.keys():
    print (typeCount,"-",key)
    typeCount += 1
docLengthChoice = int(input("\nPlease enter Your choice (number) from the above list: "))
endingLevel = vl.docOptionsIndex[docLengthChoice]
print('\n')

#Page 11 - Checkpoint
print("You have reached your Document Basecamp\n")
print("Let's make sure we are 'on the same page' - it will make the rest of this journey much easier.\n")
print("Please review your brief and the selections below - if you see any issues go-back to correct now (it will save time - even small issues such as like capitalisation).\n")

sEWPlural = ""
if subjectExpressionWhat.find("are") == 0 :
    sEWPlural = "s"


# Tense - now automated - need to buld manual check selection
# q17 = "Thinking about your primary topic, " + subjectExpressionJoin + ", is this of primary interest to " + tRE +" in the past, present or future?"
# q17a = subjectExpressionJoinLI.capitalize() + " is to be presented predominantly in the..."
# q17tip = "Tip: Tense is important as it will govenn the primary tense used in your document and whether you are talking about a topic in the past, present or future."
# print(q17 + "\n" + q17a + "\n" + q17tip)
presentedTense = (vl.primaryTense)
# for x in range(len(presentedTense)):
#     print(x, presentedTense[x])
autoTense = vl.doc_list3_2[masterDocTypeIndex][0]

# print("autotense",autoTense)
vl.masterDocTypeIndex = autoTense
selectedTense = autoTense

# vl.masterDocTypeIndex = int(input("\nPlease enter Your choice (number) from the above list:  "))
# primaryTenseIndex = vl.masterDocTypeIndex
# selectedTense = vl.primaryTense[vl.masterDocTypeIndex]
# tenseWord = vl.tenseWords[vl.masterDocTypeIndex][1]

#Orientation - positve, negative or neutral
# q7 = "How would you like to present this " + detailedDoctypeSelected + " about " + subjectExpressionJoin + " to " + tRE + "?"
# q7a = "I would like " + subjectExpressionJoinLI + " to be presented..."
# q7tip = "Tip: This will set the overall orientation of your document.  The orientation sets a relationship between the sbject and the reader.  Orientation can be updated later for individual topics."
# print("\n" + q7 + "\n" + q7a + "\n" + q7tip)
# presentedOrientation = (vl.primaryOrientation)
# for x in range(len(presentedOrientation)):
#     print(x, presentedOrientation[x])
# vl.selectedOrientation = int(input("\nPlease enter Your choice (number) from the above list:  "))
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
#                    print("considered verb",el)
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
print(p11subhead.upper())
p11header = "The way I see it " + firstName + ", is that you are looking to develop " + dde + " that will be read primarily by " + tRE + ".  \n" + subjectExpressionJoin.capitalize()[0] + subjectExpressionJoin[1:] + " " + subjectExpressionWhat + " the primary subject" + sEWPlural + "/topic" + sEWPlural +" that will be covered in this " + chosenDoctype + ".\nThe main goal of this document is for " + tRE + " to " + actionOrImpression + ".  "

p11body = "\nThis document will clearly and succinctly communicate how " + subjectName + " will impact " + selectedOrientationText + " on " + affectedByExpression + ".\n\nOk let's go."
print(p11header + "\n" + p11body)
print("\n")




#Outputs
firstName = firstName                                        # Users first name

projectName = projectName                                    # Name of the project as defined by user

# Master Document Type
vl.masterDocTypeIndex  = masterDocTypeIndex                                           #index Id of chosen document Type
vl.chosenDoctype  = chosenDoctype                                                #lower case master document Type
vl.listofsubtypes  = listofsubtypes                                               # list of document subtypes for chosen option
vl.masterDocTypeDetail  = masterDocTypeDetail                                          # detailed description of master doc type selected
vl.masterDocTypeOutputs = masterDocTypeOutputs                                         # master document outputs/deliverables based on selection

# Detailed Document Type
vl.detailedDoctype  = detailedDoctype                                              # index of selected detailed document type
vl.detailedDoctypeSelected = detailedDoctypeSelected                                      # english version of detailed doc type selected without article
vl.detailedDoctypeDesc  = detailedDoctypeDesc                                          # detailed description of detailed doc type selected
vl.dde = dde                                                    # detailed document type expression (english) after topic expressor

#Target REader
vl.targetReader= targetReader                                                 # target reader as entered by user
vl.tRE = tRE                                                          # targe reader as expressed by topic expressor

#Subject Type is Category of Subject
vl.subjectType = subjectType                                                  # index of subject type
vl.subjectTypeName = subjectTypeName                                              # english of subject type

#Sybject as provided by user
vl.subjectName= subjectName                                                  # the name of the subject as entered by the user
vl.subjectExpressionJoin = subjectExpressionJoin                                        # subject expressed
vl.subjectExpressonStartSentence = subjectExpressonStartSentence                                # subject expression at the start of sentence - Capitalised
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
