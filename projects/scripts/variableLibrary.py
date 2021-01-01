#holds common variables for question generation
import spacy
nlp = spacy.load("en_core_web_sm")
usedQuestion ={}

# pastList = [0]
# presentList = [2,3,4,5,6,8,10,11]
# futureList = [1,7,9]

#Assumed Survey Question responses - at start of HyperQuestionairre
fname = "marcus"
userDefinedSubject = "market research"
userDefinedSubjectType = "concept"
userDefinedGrouping = "software"
userDefinedProspect = "Telstra"
userDefinedSupplier = "Roy Morgan"
selectedOrientation = -1 # selects positive, negative neutral
activeNodeId = 0
questionContent = {}
questionList = []

docLengthOptions = {"1 page" : 2, "5 pages" : 3, "20 pages" : 4, "unlimited - eg book" : 5}
tenseChoice = []

docOptionsList = []
docOptionsIndex = []

for k,v in docLengthOptions.items():
    docOptionsList.append(k)
    docOptionsIndex.append(v)
#print(docOptionsList,docOptionsIndex)

userDefinedSubjectTypeOptions = ['Please select...','person', 'company', 'group', 'product or service', 'concept or thing', 'place, destination or building']

#Question Element 3 - Uses words to define the relationship(s) between subject and object
primaryOrientation = ['Please Select...', "positively", "negatively", "neutrally"]
pwoLists = [['Please select'],["impact","improve", "strengthen","progress", "develop", "elevate", "upgrade", "help", "assist", "enhance", "better", "advance", "refine", "amplify"],["impact", "diminish", "reduce", "lessen","minimise", "lower", "decrease", "disturb","impinge on","upset"],["impact", "change", "affect", "influence", "transform", "alter", "shift"]]
#proposalWordsOutcome = ""
global proposalWordsOutcome
proposalWordsOutcome = ["impact", "change", "affect", "influence", "transform", "induce change in", "shift"]
#proposalWordsOutcomePos = ["strengthen", "improve", "progress", "develop", "drive growth in", "elevate", "upgrade", "help improve", "create growth in", "assist", "enhance", "better", "advance", "refine", "amplify", "further the peformance of"]
#proposalWordsOutcomeNeg = ["detract from", "diminish", "reduce", "lessen","minimise", "lower", "decrease", "disturb","impinge on","upset"]

proposalWordsOutcomesPossibilities = {}
#the below has been moded to front end questions, but woudl still be needed to run heirarchy - will migrate it to heirarchy also
for el in proposalWordsOutcome :
    proposalWordsOutcomesPossibilities[el] = []
    for i in range(3):
        global lemm
        lemm = el
        if(i == 0) :
            doc = nlp(el)
            for token in doc:
                    lemm = token.lemma_
#                    print("considered verb",el)
            proposalWordsOutcomesPossibilities[el] .append(lemm)
        if(i == 1) :
            if(el[-1] == 'e'):
                lemm = el + "d"
            elif(el[-1] != "e") :
                lemm = el + "ed"
            proposalWordsOutcomesPossibilities[el] .append(lemm)
        if(i == 2) :
            if(el[-1] == "e") :
                lemm = el[0:len(el) - 1] + "ing"
            else :
                lemm = el + "ing"
            proposalWordsOutcomesPossibilities[el] .append(lemm)
#print(proposalWordsOutcomesPossibilities)
#proposalWordsOutcomesPossibilities = {"change" : ["change","changing","changed"]}

# Question Elements 1 and 2 - Question Starters - Part 1 (qgen) and part 2 (pre) then present, past future - each one is split singular and plural
global qgen
qgen = ["what","when","how", "where", "why","who"] #removed second where from after where
global prePresent
prePresent= ["is","does", "can", "could", "are", "do", "can", "could"]        #have taken out doesnt as it is matching on does end singluar at could (note singular also option for plural for could and can

global prePast
prePast= ["has", "did", "have","did"]                                              #end on first did for singular - did repeated

global preFuture
preFuture= ["will", "would", "can", "should", "could"]                                           # No singular or plural for future tense - words presented here in decending order of being definite -

# Question Element - Final -  Key Value Pair to add suffix to question end - based on question starter (qgen)
global suffixdict
suffixdict= {"how" : " by", "why" : " because", "where" : " in", "what" : " is", "who" : " is", "when" : " when"}

#Question Element X = the final element of the question - the question mark!
punctuation = ["?", ".","!",",",";","-"]

global countableSubject
countable = True

global indefiniteSubject
indefiniteSubject = True

# Currently unused defined variables
gender =["male", "female", "other"]
possessivePronounMale = ["he", "him", "his"]
possessivePronounFemale = ["she", "her", "her"]
possessivePronounOther = ["its", "it", "it"]
possessivePronounGroup = ["they","their","them"]
questionLevel = ["1", "2", "3", "4", "5"]
#subjectType = userDefinedSubjectTypeOptions

#masterContentType = ["Analysis Report -assessment/review/report/comparison", "Compliance Document -policy document/procedures document","Creative Work -creative fiction/creative non-fiction","Rationale -decision rationale/selection analysis/recommendation","Direct Communication -email/letter/memo/notice/newsletter","Persuasive Piece -essay/article/blog/article/whitepaper/ebook","Promotional Work -website/landing page/advertisement/flier/brochure","Business Proposal -proposal/quote/potential scenario", "Requirements Document -scope/charter/business requirements document","Future Scenario -strategy/plan/goal definition document", "Technical Document -how to article/patent specification/product manual", "Training Program -curriculum/training document"]
doc_list1 = ['Please select...', 'Analysis Report', 'Compliance Document',
             'Creative Content', 'Rationale', 'Direct Communication',
             'Persuasive Piece', 'Promotional Content', 'Business Proposal',
             'Requirements Document', 'Future Scenario', 'Technical Document',
             'Training Program']
doc_list2 = ['Available types...',
             ['assessment', 'review', 'report', 'comparison'],
             ['policy document', 'proceedures document'],
             ['creative fiction', 'creative non-fiction'],
             ['decision rationale', 'selection analysis', 'recommendation'],
             ['email', 'letter', 'memo', 'notice', 'newsletter'],
             ['essay', 'article', 'blog post', 'e-book', 'book', 'whitepaper'],
             ['website', 'landing page', 'advertisement', 'flier', 'brochure'],
             ['proposal', 'quote', 'potential scenario'],
             ['scope', 'charter', 'business requirements document'],
             ['strategy', 'plan', 'goal outline','definition document'],
             ['how to article', 'patent specification', 'product manual'],
             ['curriculum', 'training document']]

doc_list2_1 = ['Description for document subtypes...',
               ['States a position or Hypothesis and breaks that position down into a number of supporting and dissenting view ultimately providing a rounded evaluation of a topic and usually presenting a recommendation','Evaluates the performance, features or benefits of something or someone and leaves the reader with an impression (a positive or negative feeling) related to the topic','Documents the findings that have resulted from the analysis of a core topic or objective and outlines the reasoning behind those findings','This document type makes a comparison between one or more people, places, things or groups. It is designed to compare and contrast different features, benefits or aspects.'],
               ['Offers a structured approach to presenting an organisations policies to staff, suppliers, customer or members. The document is clearly structured around legal or organisational objectives and is designed to make the reader able to assess if they are in compliance or not in compliance with policies', 'Outlines step by step activities that are required to achieve either compliance or a desired organisational objective.'],
               ['Not based on fact, but interesting presents a series of plausible hypotheticals. Not presented in a chronological manner.', 'A unique method for exploring non-fiction topics and drilling down into aspects of potential interest to the reader.'],
               ['Outlines the basis on which a decision is made or recommended, evaluates various benefits, features and aspects against objectives.', 'Provides reasoning behind the selection of one of several different options (usually three options are defined and assessed)', 'Outlines why a particular course of action is recommended. This can relate to a product, service, organisation or strategic initiative. It can also provide clarification of a proposed course of action for significant personal matters'],
               ['An electronic communication usually between one individual and another, although can be sent to groups of individuals. Usually has a specific and targetted message.', 'Usually a one or two-page personal communication, either sent as an attachment in an email or printed and posted. It is one of the more personal forms of communication for both business and personal communication', 'Used by organisations for internal communications although can be part of stakeholder or investor relations processes. A memo typically documents and communicates a memorandum of understanding', 'Provides new information to the reader about a topic that might affect them. Notices are a core aspect of stakeholder communications processes', 'A method of communicating multiple points to a largely homogenous group of individuals. It is often used in business or by sporting clubs to maintain membership and engagement'],
               ['A short formal piece of writing, usually for educational purposes to demonstrate knowledge of a topic or explore a topic.  It contains an introduction, body and conclusion and is usually a maximum of 5,000 words', 'An expose on a topic, articles are often used for online "content marketing" typically being between 400 words and 1,500 words in length', 'A blog post is similar in nature to an article although is often shorter and specifically targets a feature, benefit or pain point directly', 'A short-form book designed to be consumed by an e-reader.  Ebooks are often used as a free or low-cost introduction to a topic, product or service.  Our ebook format is output with images in PDF format and you may later need to popular ebook formats', 'A book is a detailed explanation on a topic and can run to many hundreds of pages.  In a book key topics or areas are often referred to as chapters.  Our book format contains text and has very limited scope for images and is delivered in MS Word and PDF formats', 'Aan informational document, usually issued by a company or not for profit organisation to promote or highlight features of a solution, product or service.  Often associated with the introduction of new technology.'],
               ['A series of inter-related web pages usually associated with a domain.  A website is similar to an online brochure that presents information about a company, product, service or cause.  A website can be a minimum of 3 web pages', 'A single-page website used to drive conversion online.  Conversions can relate to capturing leads, obtaining bookings or selling a product or service.', 'As used here relates typically to a full-page advertisement in a newspaper or magazine.  It is intended multiple advertisement output formats will be developed including online display, online search, and offline.', 'A form of advertisement intended for wide distribution either via printed copy or via attachment in electronic communication.  A flier is typically one to four pages in length and integrates imagery and design', 'Typically a glossy image-centric communication used by organisations to promote a product, service or concept.  Brochures are typically one to ten pages in length.'],
               ['A future-oriented document.  It relates to stating a written offer to a prospective buyer.  This format is suitable for proposals, requests for information and tender responses where the format is not specified.  Ideally suited to complex services proposals.  If the required format is specified by the prospect then some cutting and pasting may be required.', 'Typically a one or two-page (brief) proposal.  It is typically less convincing than a proposal but for small product or services sales is sufficient as the basis of a transaction.', 'A potential scenario relates to explaining what a future scenario may look-like, and providing a rationale for your views.'],
               ['Outlines the boundaries of a project (in-scope and out of scope).  Scope documents are most often used in large services-based projects and can range from one page to 10 pages in length.', 'Outlines the objectives and boundaries associated with a venture, organisation or program.', 'Outlines the requirements of a business or business unit in relation to the development of a new product, service or piece of software.'],
               ['A strategy, often referred to as a strategic plan is briefer than a business plan.  It focuses on defining a high-level future pathway and providing a rationale for the recommended goals, objectives and vision','Includes plans such as business plan, marketing plan, investment plan, human resources plan etc.  In words outlines the strategy and structure behind achieving a future-oriented objectives, and is designed as a sales document to convince and provide confidence in the achievement of the plan.','Typically one page and outlines key business goals and why they are important to the organisation.'],
               ['Describes to the target reader how to do something.  It is effectively a mini-product manual or guide that provides step-by-step guidance', 'A document that is designed to be used as part of a patent application.  It is not the full patent but is often referred to as the abstract and can stretch from one page to three pages in length.', 'A product manual is the type of printed or electronic document that accompanies the purchase of a product (Eg. a vehicle, computer or smartphone.  The manual covers all significant areas of usage'],
               ['Relates to the development of course materials for students and often comprises of multiple classes and topics', 'A step by step guide on what needs to be learned and accompanies either teaching materials or is used for train the trainer activities.']
              ]

doc_list2_2 = ['Selection of Heirarchy Method for Master Document Type...',
               ['criticalThinking'],
               ['tocBased'],
               ['freeForm'],
               ['criticalThinking'],
               ['freeForm'],
               ['freeForm'],
               ['promotional'],
               ['methodologyBased'],
               ['tocBased'],
               ['methodologyBased'],
               ['tocBased'],
               ['tocBased']
              ]

doc_list1_1 = ['Descriptions...',
             'Provides a structured framework for assessing something and documenting a report to communicate the findings. Leverages best practice methods in critical thinking',
             'A compliance document outlines how staff, contractors or third parties should act. Incorporates external 3rd party requirements such as government legislation and applies them to an organisational context. Available in MS Word/Google Docs/Pdf/Text. Outputs available from 5 pages to 100 pages. Deliverable contains introduction, table of contents, and numbered headings and sections. Logo and 3 customisable images available.',
             'Creative content is a work that is designed to delight and entertain. Content not based purely on analysis, uses ideas (unexpected connections) to "present with identity", enabling the content to be highly differentiated. Available in MS Word/Google Docs/Pdf/Text - Outputs available from 1 page to 500 pages. Deliverable is presented in topic order, does not contain table of contents or summary, designer template with no logo and scope for two custom images. Can be present, explanatory, explanatory MethodX, docTemplateX, icon Y',
             'A rationale is a document that uses Pyramid Thinking to identify and support a conclusion or recommendation. Helps the user to understand implications and choose between alternatives based on their personal or organisational situation. Available in MS Word/Google Docs/Pdf/Text - Outputs available from 1 page to 100 pages. Deliverable contains introduction, table of contents executive summary, conclusion and summary. Customisable images include one logo plus three custom images. Can be present, explanatory, explanatory MethodX, docTemplateX, icon Y',
             'A piece of communication designed to communicate a specific message to one or more readers in a direct (not broadcast) communication. Available in a range of formats suitable for each communication type (Text for Email), and MS Word/Google Docs/Pdf for Newsletters and Memos - Outputs available in 1-10 pages. Deliverable contains appropriate formatting and content for your chosen document type. Word document outputs include images - one logo plus three custom images. Can be present, explanatory, explanatory MethodX, docTemplateX, icon Y',
             'A persuasive/explanatory piece of writing on a particular subject (Non Fiction) that is designed to persuade a business or individual about either the benefits or implications of something. Available in MS Powerpoint/MS Word/Google Docs/Google Slides/Pdf/Text - Note multiple outputs availabe from a single consultation between 1 page and 50 pages. Deliverable is presented to maximise the structuring and presentation of arguments to lead the reader to a clear conclusion. Contains a table of contents, summary, designer template scope for custom logo and three custom images. Can be present, explanatory, explanatory MethodX, docTemplateX, icon Y',
             'Promotes a business, concept or idea. This content is designed to be used in marketing communication and broadcast to your prospective target audience. Available in HTML/XML/MS Powerpoint/MS Word/Goole Docs/Google Slides/Pdf/Text - Note some promotional work document categories provide a zipped folder of documents such as landing page and website. Format makes providsion for specified document format. Can be future, explanatory, explanatory MethodX, docTemplateX, icon Y',
             'A business document that assists you to identify, define and communicate a suggested future state, relationship or structure. Designed to elicit approval by a 3rd party. Available in MS Word/Google Docs/Pdf/Text - Outputs available from 1 page to 100 pages. Deliverable contains introduction, table of contents executive summary, conclusion and summary. Customisable images include one logo plus three custom images. Can be future, explanatory, explanatory MethodX, docTemplateX, icon Y',
             'A business document that to identify and communicate business or project requirements to another individual or organisation. Available in MS Word/Google Docs/Pdf/Text - Outputs available from 1 page to 100 pages - landscape or portrait format. Deliverable contains introduction, table of contents executive summary, conclusion and summary. Customisable images include one logo plus three custom images. Can be present, explanatory, explanatory MethodX, docTemplateX, icon Y',
             'Develops a clear picture of a future scenario that does not yet exist and positively presents this to the reader. Available in MS Powerpoint/MS Word/Google Docs/Google Slides/Pdf/Text - Note multiple outputs availabe from a single consultation between 1 page and 100 pages. Landscape and Portrait options available. Method used facilitates the development of a logically consistent future scenario. Contains a table of contents, summary, designer template scope for custom logo and three custom images. Can be future, explanatory, explanatory MethodX, docTemplateX, icon Y',
             'Outlines to the user of a product or service how to use that product or serviced. Available in MS Word/Google Docs/Pdf/Text. Outputs available from 5 pages to 100 pages. Presented in portrait format. Deliverable contains introduction, table of contents, and numbered headings and sections. Logo and 3 customisable images available. Can be present, explanatory, explanatory MethodX, docTemplateX, icon Y',
             'Content that is designed to train someone or teach someone how to do something - typically designed to be presented by a teacher, tutor etc. Available in MS Powerpoint/MS Word/Google Docs/Google Slides/Pdf/Text - Note multiple outputs availabe from a single consultation between 1 page and 100 pages. Landscape and Portrait options available. Method used facilitates the clear structuring of concepts for communication to those who are in a learning mode. Contains a table of contents, summary, designer template scope for custom logo and three custom images. Can be present, explanatory, explanatory MethodX, docTemplateX, icon Y']

doc_list1_2 = ['Outputs...',
               'Available in MS Word/Google Docs/Pdf/Text.  Outputs - 1 page to 100 pages - portrait format.  Includes: introduction, table of contents executive summary, conclusion and summary.  Offers 4 customisable images including logo.',
               'Available in MS Word/Google Docs/Pdf/Text.  Outputs - 5 pages to 100 pages.  Deliverable contains introduction, table of contents, and numbered headings and sections.  Logo and 3 customisable images available.',
               'Available in MS Word/Google Docs/Pdf/Text.  Outputs - 1 page to 500 pages.  Deliverable is presented in topic order, does not contain table of contents or summary, designer template with no logo and scope for two custom images.',
               'Available in MS Word/Google Docs/Pdf/Text.  Outputs available from 1 page to 100 pages.  Deliverable contains introduction, table of contents executive summary, conclusion and summary.  Customisable images include one logo plus three custom images.',
               'Available in a range of formats suitable for each communication type (Text for Email), and MS Word/Google Docs/Pdf for Newsletters and Memos -  Outputs available in 1-10 pages.  Deliverable contains appropriate formatting and content for your chosen document type.   Word document outputs include images - one logo plus three custom images.',
               'Available in MS Powerpoint/MS Word/Google Docs/Google Slides/Pdf/Text  - Note multiple outputs available from a single consultation between 1 page and 50 pages.  Deliverable is presented to maximise the structuring and presentation of arguments to lead the reader to a clear conclusion. Contains a table of contents, summary, designer template scope for custom logo and three custom images.',
               'Available in HTML/XML/MS Powerpoint/MS Word/Goole Docs/Google Slides/Pdf/Text - Note some promotional work document categories provide a zipped folder of documents such as landing page and website.  Format makes providsion for specified document format.',
               'Available in MS Word/Google Docs/Pdf/Text.  Outputs - 1 page to 100 pages.  Deliverable contains introduction, table of contents executive summary, conclusion and summary.  Customisable images include one logo plus three custom images.',
               'Available in MS Word/Google Docs/Pdf/Text.  Outputs available from 1 page to 100 pages - landscape or portrait format.  Deliverable contains introduction, table of contents executive summary, conclusion and summary.  Customisable images include one logo plus three custom images.',
               'Available in MS Powerpoint/MS Word/Google Docs/Google Slides/Pdf/Text  - Note multiple outputs availabe from a single consultation between 1 page and 100 pages.  Landscape and Portrait options available.  Method used facilitates the development of a logically consistent future scenario.  Contains a table of contents, summary, designer template scope for custom logo and three custom images.',
               'Available in MS Word/Google Docs/Pdf/Text.  Outputs - 5 pages to 100 pages.  Presented in portrait format.  Deliverable contains introduction, table of contents, and numbered headings and sections.  Logo and 3 customisable images available.',
               'Available in MS Powerpoint/MS Word/Google Docs/Google Slides/Pdf/Text  - Note multiple outputs availabe from a single consultation between 1 page and 100 pages.  Landscape and Portrait options available.  Method used facilitates the clear structuring of concepts for communication to those who are in a learning mode.  Contains a table of contents, summary, designer template scope for custom logo and three custom images.']

doc_list3_2 = [['tense', 'orientation','pleaseselect.png'],['t', 'neutrally', 'analysisreport.png'],
               ['f', 'neutrally', 'compliancedocument.png'],
               ['t', 'neutrally', 'creativework.png'],
               ['t', 'neutrally', 'rationale.png'],
               ['t', 'neutrally', 'directcommunication.png'],
               ['t', 'neutrally', 'persuasivepiece.png'],
               ['f', 'neutrally', 'promotionalwork.png'],
               ['f', 'positively', 'businessproposal.png'],
               ['t', 'neutrally', 'requirementsdocument.png'],
               ['f', 'positively', 'futurescenario.png'],
               ['t', 'neutrally', 'technicaldocument.png'],
               ['t', 'neutrally', 'trainingprogram.png']]

doc_list3 = ['Please select...',
             '1 page',
             '5 pages',
             '20 pages',
             'unlimited'
             ]

doc_list3_1 = ['Descriptions...',
               'Small document or overview - covers one master topic and 3 subtopics.  Wordcount from 200 words to 500 words depending on output format',
               '5 page document, a brief document typically covering one master topic, 3 subtopics and 2 further subtopics.  Wordcount 1,000 to 2,000 words depending on output format',
               '20 page document, a signficant document with master topics and subtopics dynamically assembled throughout the process - typically a 4 level topic heirarchy.  Wordcount 4,000 to 7,000 words depending on output format',
               'Unlimited size - eg book. Provides a substantial volume of content that includes numerous topics and subtopics.  Output will be largely text'
               ]

doc_tips = {'page1': 'Tip: Once you select an option, a detailed description will be displayed. Please consider carefully as different content types may produce different outcomes.',
            'page2': ['Note: If you are seeking to create multiple', 'documents then you can create a copy of this file once finished and edit.']}

userDefinedSubjectTypeDescriptions = [
    "Please Select", 
    "A person is typically one named individual who will be at the centre of your document. Effectively the entire document will be about them.", 
    "A company is a legal entity designed either for-profit.  An organisation is typically either a government agency or not-for-profit organisation.  Consider carefully when selecting a company or organisation that you are referring to the legal title of the organisation and not a division within an organisation.", 
    "A group is a named group of people, things or animals.  It could also be a division with a company or organisation, For example, a local football team is a group, elephants are a group of animals etc.", 
    "A product is a tangible item that is put on the market for acquisition, attention, or consumption, while a service is an intangible item, which arises from the output of one or more individuals.", 
    "This category relates to ideas and abstract concepts.  Examples include - climate - technology - flying.  Furthermore, this category also includes things these may be products such as - Lego - Computers - Boeing A380.", 
    "A place, destination or building is a physical area that can be seen on a map or satellite photograph.  If you are referring to a group of places (eg Parks) then group would be a better selection"
]

doctypeDescription = {"Analysis Report" : ["Provides a structured framework for assessing something and documenting a report to communicate the findings", "Available in MS Word/Google Docs/Pdf/Text.  Outputs available from 1 page to 100 pages - portrait format.  Deliverable contains introduction, table of contents executive summary, conclusion and summary.  Offers 4 customisable images including logo.", "present" ,"explanatory", "criticalthinking", "docTemplateX", "icon Y"], "Compliance Document" : ["A compliance document outlines how staff, contractors or third parties should act.  Incorporates external 3rd party requirements such as government legislation and applies them to an organisational context.", "Available in MS Word/Google Docs/Pdf/Text.  Outputs available from 5 pages to 100 pages.  Deliverable contains introduction, table of contents, and numbered headings and sections.  Logo and 3 customisable images available.", "future" ,"explanatory", "explanatory MethodX", "docTemplateX", "icon Y"], "Creative Work" : ["Creative content is a work that is designed to delight and entertain.  Content not based purely on analysis, uses ideas (unexpected connections) to 'present with identity', enabling the content to be highly differentiated.", "Available in MS Word/Google Docs/Pdf/Text - Outputs available from 1 page to 500 pages.  Deliverable is presented in topic order, does not contain table of contents or summary, designer template with no logo and scope for two custom images.", "present" ,"explanatory", "explanatory MethodX", "docTemplateX", "icon Y"], "Rationale" : ["A rationale is a document that uses Pyramid Thinking to identify and  support a conclusion or recommendation.  Helps the user to understand implications and choose between alternatives based on their personal or organisational situation.", "Available in MS Word/Google Docs/Pdf/Text -  Outputs available from 1 page to 100 pages.  Deliverable contains introduction, table of contents executive summary, conclusion and summary.  Customisable images include one logo plus three custom images.", "present" ,"explanatory", "explanatory MethodX", "docTemplateX", "icon Y"], "Direct Communication" : ["A piece of communication designed to communicate a specific message to one or more readers in a direct (not broadcast) communication.", "Available in a range of formats suitable for each communication type (Text for Email), and MS Word/Google Docs/Pdf for Newsletters and Memos -  Outputs available in 1-10 pages.  Deliverable contains appropriate formatting and content for your chosen document type.   Word document outputs include images - one logo plus three custom images.", "present" ,"explanatory", "explanatory MethodX", "docTemplateX", "icon Y"], "Persuasive Piece" : ["A persuasive/explanatory piece of writing on a particular subject (Non Fiction) that is designed to persuade a business or individual about either the benefits or implications of something.", "Available in MS Powerpoint/MS Word/Google Docs/Google Slides/Pdf/Text  - Note multiple outputs availabe from a single consultation between 1 page and 50 pages.  Deliverable is presented to maximise the structuring and presentation of arguments to lead the reader to a clear conclusion. Contains a table of contents, summary, designer template scope for custom logo and three custom images.", "present" ,"explanatory", "explanatory MethodX", "docTemplateX", "icon Y"],"Promotional Work" : ["Promotes a business, concept or idea.  This content is designed to be used in marketing communication and broadcast to your prospective target audience.", "Available in HTML/XML/MS Powerpoint/MS Word/Goole Docs/Google Slides/Pdf/Text - Note some promotional work document categories provide a zipped folder of documents such as landing page and website.  Format makes providsion for specified document format.", "future" ,"explanatory", "explanatory MethodX", "docTemplateX", "icon Y"], "Business Proposal" : ["A business document that assists you to identify, define and communicate a suggested future state, relationship or structure.  Designed to elicit approval by a 3rd party.", "Available in MS Word/Google Docs/Pdf/Text -  Outputs available from 1 page to 100 pages.  Deliverable contains introduction, table of contents executive summary, conclusion and summary.  Customisable images include one logo plus three custom images.", "future" ,"explanatory", "explanatory MethodX", "docTemplateX", "icon Y"], "Requirements Document" : ["A business document that to identify and communicate business or project requirements to another individual or organisation.", "Available in MS Word/Google Docs/Pdf/Text -  Outputs available from 1 page to 100 pages - landscape or portrait format.  Deliverable contains introduction, table of contents executive summary, conclusion and summary.  Customisable images include one logo plus three custom images.", "present" ,"explanatory", "explanatory MethodX", "docTemplateX", "icon Y"], "Future Scenario" : ["Develops a clear picture of a future scenario that does not yet exist and positively presents this to the reader.", "Available in MS Powerpoint/MS Word/Google Docs/Google Slides/Pdf/Text  - Note multiple outputs availabe from a single consultation between 1 page and 100 pages.  Landscape and Portrait options available.  Method used facilitates the development of a logically consistent future scenario.  Contains a table of contents, summary, designer template scope for custom logo and three custom images.", "future" ,"explanatory", "explanatory MethodX", "docTemplateX", "icon Y"], "Technical Document" : ["Outlines to the user of a product or service how to use that product or serviced.", "Available in MS Word/Google Docs/Pdf/Text.  Outputs available from 5 pages to 100 pages.  Presented in portrait format.  Deliverable contains introduction, table of contents, and numbered headings and sections.  Logo and 3 customisable images available.", "present" ,"explanatory", "explanatory MethodX", "docTemplateX", "icon Y"],"Training Program" : ["Content that is designed to train someone or teach someone how to do something - typically designed to be presented by a teacher, tutor etc.", "Available in MS Powerpoint/MS Word/Google Docs/Google Slides/Pdf/Text  - Note multiple outputs availabe from a single consultation between 1 page and 100 pages.  Landscape and Portrait options available.  Method used facilitates the clear structuring of concepts for communication to those who are in a learning mode.  Contains a table of contents, summary, designer template scope for custom logo and three custom images.", "present" ,"explanatory", "explanatory MethodX", "docTemplateX", "icon Y"]}
#split on dash then split on slash.
docSubtype = {"assessment" : ["this method uses critical thinking to clarify the differnece between options, and argue for the proposed selection", "question model", "description template"],"review" : ["review description", "question model ", "reviewtemplate"]}
analysisReport = ["assessment","review"]
assessment = ["detailed description: assessment is a bkfkdkfdkfdfjdfk"]


#Question selection Variables - Guide the selection of question generation method and the prefix to use - need to add to this the "Tone"  - definite or possible
primaryTense = ["Please Select","past","present","future"]
tenseWords = ["Please Select", ["has", "did", "have","did"] , ["is","does", "can", "could", "are", "do", "can", "could"] , ["will", "would", "can", "should", "could"]]

contentFlow = ["explanatory","chronological","methodology","document structure", "legislative clauses"]

# Define the article to be used with the userdefined subject
global article
article = ["the", "a", "an", "she", "he", "it"]

# Master Selected vairables that guide question selection - these need to be activated.
selectedSubjectType = (userDefinedSubjectTypeOptions[2])
selectedMasterSubject = (doc_list1[6])
selectedTense = "past"  #subjectTenseMapper[selectedMasterSubject]
SelectedSubcategory = "Business Proposal"

#transform the core words into more sophisticated questions
What = ["What"]
Where = ['In what area', 'In which situation', 'In which location', 'In what place', 'Whereabouts', 'In what direction', 'At which point', 'Where','In what location', 'In which situation', 'In which area', 'In what place', 'In what direction', 'In which precinct']
When = ['At what time', 'In what time period', 'How soon', 'Following what occurance', 'At what time', 'When','In what time period', 'In what instance', 'At what phase', 'On what occasion', 'At what moment']
How = ['In what way', 'By what method', 'How', 'In what manner', 'According to what approach', 'Through what approach', 'To what degree', 'By what means', 'By what system']
Why = ['By what reason', 'What factors', 'By what reasoning', 'As a result of what reason', 'On the basis of what facts', 'Why','What skills', 'On what basis', 'As the result of what cause', 'The underlying reason']


#Rule to apply for conversion from question to leadin - rule no 4
rule4 = ["where are", "where has","why will","how is", "how are", "how doesn't", "how have", "how has", "how was", "how were", "how can",  "how could", "how should ", "how will",
         "how would", "where doesn't" , "where can", "where could", "where should","where would","where will", "where have", "why is", "why are", "why doesn't", "why have", "why has", "why was", "why were", "why can", "why could", "why should", "why would", "when is", "when are", "when doesn't", "when have", "when has", "when was", "when were", "when was", "when can", "where is", "when could", "when should", "when will", "when would", "when is", "when are" ]
nullResult = ["what do", "what does", "what doesn't", "what did", "who did", "what has", "what can", "what could", "what should", "what will", "what would",
              "who do", "who does", "who doesnt", "who have", "who did", "who has", "who was", "Who were", "who can", "who could", "who type"]


q1_1 = (qgen[0])
q1_2 = (qgen[1])
q1_3 = (qgen[2])
q1_4 = (qgen[3])
q1_5 = (qgen[4])
