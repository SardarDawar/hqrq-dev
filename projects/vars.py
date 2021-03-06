# Project 'stage' options
PROJ_STAGE_STARTED = 'STARTED'                              # just started, type selected
PROJ_STAGE_INIT_QUESTIONS = 'INIT_QUESTIONS'                # in process of asking initial set of questions
PROJ_STAGE_BASECAMP = 'BASECAMP'                            # reached document basecamp stage
PROJ_STAGE_STRUCTURING = 'STRUCTURING'                      # gen and fill nodes

PROJ_STAGE_DEFAULT = PROJ_STAGE_STARTED                     # default project stage on creation

PROJ_TEXT_STAGE_STARTED = 'Just Started'
PROJ_TEXT_STAGE_INIT_QUESTIONS = 'Asking Initial Questions'
PROJ_TEXT_STAGE_BASECAMP = 'Reached Document Basecamp'
PROJ_TEXT_STAGE_STRUCTURING = 'Structuring Project Nodes'

PROJ_STAGE_CHOICES = [
    (PROJ_STAGE_STARTED, PROJ_TEXT_STAGE_STARTED),
    (PROJ_STAGE_INIT_QUESTIONS, PROJ_TEXT_STAGE_INIT_QUESTIONS),
    (PROJ_STAGE_BASECAMP, PROJ_TEXT_STAGE_BASECAMP),
    (PROJ_STAGE_STRUCTURING, PROJ_TEXT_STAGE_STRUCTURING),
]

# Project 'status' options
PROJ_STATUS_IN_PROGRESS = 'IN_PROGRESS'                     # project in-progress
PROJ_STATUS_COMPLETE = 'COMPLETE'                           # project complete

PROJ_STATUS_DEFAULT = PROJ_STATUS_IN_PROGRESS               # default project status on creation

PROJ_TEXT_STATUS_IN_PROGRESS = 'In Progress'
PROJ_TEXT_STATUS_COMPLETE = 'Complete'

PROJ_STATUS_CHOICES = [
    (PROJ_STATUS_IN_PROGRESS, PROJ_TEXT_STATUS_IN_PROGRESS),
    (PROJ_STATUS_COMPLETE, PROJ_TEXT_STATUS_COMPLETE),
]

# Project 'doc_type' options
PROJ_TYPE_ANALYSIS_REPORT = 'PT_AN_REP'
PROJ_TYPE_COMPLIANCE_DOCUMENT = 'PT_COMP_DOC'
PROJ_TYPE_CREATIVE_CONTENT = 'PT_CREAT_CONT'
PROJ_TYPE_RATIONALE = 'PT_RATIONALE'
PROJ_TYPE_DIRECT_COMMUNICATION = 'PT_DIR_COMM'
PROJ_TYPE_PERSUASIVE_PIECE = 'PT_PERS_PEICE'
PROJ_TYPE_PROMOTIONAL_CONTENT = 'PT_PROMO_CONT'
PROJ_TYPE_BUSINESS_PROPOSAL = 'PT_BUSIN_PROP'
PROJ_TYPE_REQUIREMENTS_DOCUMENT = 'PT_REQ_DOC'
PROJ_TYPE_FUTURE_SCENARIO = 'PT_FUT_SCEN'
PROJ_TYPE_TECHNICAL_DOCUMENT = 'PT_TECH_DOC'
PROJ_TYPE_TRAINING_PROGRAM = 'PT_TRAIN_PROG'



# Master Doc Type List
doc_list_1 = [
    PROJ_TYPE_ANALYSIS_REPORT,
    PROJ_TYPE_COMPLIANCE_DOCUMENT,
    PROJ_TYPE_CREATIVE_CONTENT,
    PROJ_TYPE_RATIONALE,
    PROJ_TYPE_DIRECT_COMMUNICATION,
    PROJ_TYPE_PERSUASIVE_PIECE,
    PROJ_TYPE_PROMOTIONAL_CONTENT,
    PROJ_TYPE_BUSINESS_PROPOSAL,
    PROJ_TYPE_REQUIREMENTS_DOCUMENT,
    PROJ_TYPE_FUTURE_SCENARIO,
    PROJ_TYPE_TECHNICAL_DOCUMENT,
    PROJ_TYPE_TRAINING_PROGRAM
]


PROJ_TYPE_DEFAULT = PROJ_TYPE_ANALYSIS_REPORT

PROJ_TEXT_TYPE_ANALYSIS_REPORT = 'Analysis Report'
PROJ_TEXT_TYPE_COMPLIANCE_DOCUMENT = 'Compliance Document'
PROJ_TEXT_TYPE_CREATIVE_CONTENT = 'Creative Content'
PROJ_TEXT_TYPE_RATIONALE = 'Rationale'
PROJ_TEXT_TYPE_DIRECT_COMMUNICATION = 'Direct Communication'
PROJ_TEXT_TYPE_PERSUASIVE_PIECE = 'Persuasive Piece'
PROJ_TEXT_TYPE_PROMOTIONAL_CONTENT = 'Promotional Content'
PROJ_TEXT_TYPE_BUSINESS_PROPOSAL = 'Business Proposal'
PROJ_TEXT_TYPE_REQUIREMENTS_DOCUMENT = 'Requirements Document'
PROJ_TEXT_TYPE_FUTURE_SCENARIO = 'Future Scenario'
PROJ_TEXT_TYPE_TECHNICAL_DOCUMENT = 'Technical Document'
PROJ_TEXT_TYPE_TRAINING_PROGRAM = 'Training Program'




PROJ_TYPE_CHOICES = [
    (PROJ_TYPE_ANALYSIS_REPORT, PROJ_TEXT_TYPE_ANALYSIS_REPORT), 
    (PROJ_TYPE_COMPLIANCE_DOCUMENT, PROJ_TEXT_TYPE_COMPLIANCE_DOCUMENT),
    (PROJ_TYPE_CREATIVE_CONTENT, PROJ_TEXT_TYPE_CREATIVE_CONTENT), 
    (PROJ_TYPE_RATIONALE, PROJ_TEXT_TYPE_RATIONALE), 
    (PROJ_TYPE_DIRECT_COMMUNICATION, PROJ_TEXT_TYPE_DIRECT_COMMUNICATION),
    (PROJ_TYPE_PERSUASIVE_PIECE, PROJ_TEXT_TYPE_PERSUASIVE_PIECE ), 
    (PROJ_TYPE_PROMOTIONAL_CONTENT, PROJ_TEXT_TYPE_PROMOTIONAL_CONTENT), 
    (PROJ_TYPE_BUSINESS_PROPOSAL, PROJ_TEXT_TYPE_BUSINESS_PROPOSAL),
    (PROJ_TYPE_REQUIREMENTS_DOCUMENT, PROJ_TEXT_TYPE_REQUIREMENTS_DOCUMENT), 
    (PROJ_TYPE_FUTURE_SCENARIO, PROJ_TEXT_TYPE_FUTURE_SCENARIO), 
    (PROJ_TYPE_TECHNICAL_DOCUMENT, PROJ_TEXT_TYPE_TECHNICAL_DOCUMENT),
    (PROJ_TYPE_TRAINING_PROGRAM, PROJ_TEXT_TYPE_TRAINING_PROGRAM),
]

# Project 'subtype' options

PROJ_SUBTYPE_ASSESSMENT = 'PST_ASSESS'
PROJ_SUBTYPE_REVIEW = 'PST_REVIEW'
PROJ_SUBTYPE_REPORT = 'PST_REPORT'
PROJ_SUBTYPE_COMPARISON = 'PST_COMPAR'

PROJ_SUBTYPE_POLICY_DOCUMENT = 'PST_POLICY_DOC'
PROJ_SUBTYPE_PROCEDURES_DOCUMENT = 'PST_PROC_DOC'

PROJ_SUBTYPE_CREATIVE_FICTION = 'PST_CREATIVE_FICT'
PROJ_SUBTYPE_CREATION_NON_FICTION = 'PST_CREATIVE_NONFICT'

PROJ_SUBTYPE_DECISION_RATIONALE = 'PST_DECIS_RATIO'
PROJ_SUBTYPE_SELECTION_ANALYSIS = 'PST_SELECT_AN'
PROJ_SUBTYPE_RECOMMENDATION = 'PST_RECOMM'

PROJ_SUBTYPE_EMAIL = 'PST_EMAIL'
PROJ_SUBTYPE_LETTER = 'PST_LETTER'
PROJ_SUBTYPE_MEMO = 'PST_MEMO'
PROJ_SUBTYPE_NOTICE = 'PST_NOTICE'
PROJ_SUBTYPE_NEWSLETTER = 'PST_NEWSLETTER'

PROJ_SUBTYPE_ESSAY = 'PST_ESSAY'
PROJ_SUBTYPE_ARTICLE = 'PST_ARTICLE'
PROJ_SUBTYPE_BLOG_POST = 'PST_BLOG_POST'
PROJ_SUBTYPE_E_BOOK = 'PST_EBOOK'
PROJ_SUBTYPE_BOOK = 'PST_BOOK'
PROJ_SUBTYPE_WHITEPAPER = 'PST_WHITEPPR'

PROJ_SUBTYPE_WEBSITE = 'PST_WEBSITE'
PROJ_SUBTYPE_LANDING_PAGE = 'PST_LAND_PG'
PROJ_SUBTYPE_ADVERTISEMENT = 'PST_ADVERT'
PROJ_SUBTYPE_FLIER = 'PST_FLIER'
PROJ_SUBTYPE_BROCHURE = 'PST_BROCHURE'

PROJ_SUBTYPE_PROPOSAL = 'PST_PROPOS'
PROJ_SUBTYPE_QUOTE = 'PST_QUOTE'
PROJ_SUBTYPE_POTENTIAL_SCENARIO = 'PST_POT_SCEN'

PROJ_SUBTYPE_SCOPE = 'PST_SCOPE'
PROJ_SUBTYPE_CHARTER = 'PST_CHARTER'
PROJ_SUBTYPE_BUSINESS_REQUIREMENTS_DOCUMENT = 'PST_BUS_REQ_DOC'

PROJ_SUBTYPE_STRATEGY = 'PST_STRAT'
PROJ_SUBTYPE_PLAN = 'PST_PLAN'
PROJ_SUBTYPE_GOAL_OUTLINE = 'PST_GOAL_OUT'
PROJ_SUBTYPE_DEFINITION_DOCUMENT = 'PST_DEFIN_DOC'

PROJ_SUBTYPE_HOW_TO_ARTICLE = 'PST_HOW_ART'
PROJ_SUBTYPE_PATENT_SPECIFICATION = 'PST_PAT_SPEC'
PROJ_SUBTYPE_PRODUCT_MANUAL = 'PST_PROD_MAN'

PROJ_SUBTYPE_CURRICULUM = 'PST_CURRIC'
PROJ_SUBTYPE_TRAINING_DOCUMENT = 'PST_TRAIN_DOC'

PROJ_SUBTYPE_DEFAULT = PROJ_SUBTYPE_ASSESSMENT

PROJ_TEXT_SUBTYPE_ASSESSMENT = 'Assessment'
PROJ_TEXT_SUBTYPE_REVIEW = 'Review'
PROJ_TEXT_SUBTYPE_REPORT = 'Report'
PROJ_TEXT_SUBTYPE_COMPARISON = 'Comparison'

PROJ_TEXT_SUBTYPE_POLICY_DOCUMENT = 'Policy Document'
PROJ_TEXT_SUBTYPE_PROCEDURES_DOCUMENT = 'Procedures Document'

PROJ_SUBTYPE_CREATIVE_FICTION = 'Creative Fiction'
PROJ_SUBTYPE_CREATION_NON_FICTION = 'Creative Non-Fiction'

PROJ_TEXT_SUBTYPE_DECISION_RATIONALE = 'Decision Rationale'
PROJ_TEXT_SUBTYPE_SELECTION_ANALYSIS = 'Selection Analysis'
PROJ_TEXT_SUBTYPE_RECOMMENDATION = 'Recommendation'

PROJ_TEXT_SUBTYPE_EMAIL = 'Email'
PROJ_TEXT_SUBTYPE_LETTER = 'Letter'
PROJ_TEXT_SUBTYPE_MEMO = 'Memo'
PROJ_TEXT_SUBTYPE_NOTICE = 'Notice'
PROJ_TEXT_SUBTYPE_NEWSLETTER = 'Newsletter'

PROJ_TEXT_SUBTYPE_ESSAY = 'Essay'
PROJ_TEXT_SUBTYPE_ARTICLE = 'Article'
PROJ_TEXT_SUBTYPE_BLOG_POST = 'Blog Post'
PROJ_TEXT_SUBTYPE_E_BOOK = 'E-Book'
PROJ_TEXT_SUBTYPE_BOOK = 'Book'
PROJ_TEXT_SUBTYPE_WHITEPAPER = 'Whitepaper'

PROJ_TEXT_SUBTYPE_WEBSITE = 'Website'
PROJ_TEXT_SUBTYPE_LANDING_PAGE = 'Landing Page'
PROJ_TEXT_SUBTYPE_ADVERTISEMENT = 'Advertisement'
PROJ_TEXT_SUBTYPE_FLIER = 'Flier'
PROJ_TEXT_SUBTYPE_BROCHURE = 'Brochure'

PROJ_TEXT_SUBTYPE_PROPOSAL = 'Proposal'
PROJ_TEXT_SUBTYPE_QUOTE = 'Quote'
PROJ_TEXT_SUBTYPE_POTENTIAL_SCENARIO = 'Potential Scenario'

PROJ_TEXT_SUBTYPE_SCOPE = 'Scope'
PROJ_TEXT_SUBTYPE_CHARTER = 'Charter'
PROJ_TEXT_SUBTYPE_BUSINESS_REQUIREMENTS_DOCUMENT = 'Business Requirements Document'

PROJ_TEXT_SUBTYPE_STRATEGY = 'Strategy'
PROJ_TEXT_SUBTYPE_PLAN = 'Plan'
PROJ_TEXT_SUBTYPE_GOAL_OUTLINE = 'Goal Outline'
PROJ_TEXT_SUBTYPE_DEFINITION_DOCUMENT = 'Definition Document'

PROJ_TEXT_SUBTYPE_HOW_TO_ARTICLE = 'How-To Article'
PROJ_TEXT_SUBTYPE_PATENT_SPECIFICATION = 'Patent Specification'
PROJ_TEXT_SUBTYPE_PRODUCT_MANUAL = 'Product Manual'

PROJ_TEXT_SUBTYPE_CURRICULUM = 'Curriculum'
PROJ_TEXT_SUBTYPE_TRAINING_DOCUMENT = 'Training Document'


# Sub-doc type list
vl_sub_type_list = [
    [
        PROJ_SUBTYPE_ASSESSMENT,
        PROJ_SUBTYPE_REVIEW,
        PROJ_SUBTYPE_REPORT,
        PROJ_SUBTYPE_COMPARISON,
    ],
    [
        PROJ_SUBTYPE_POLICY_DOCUMENT,
        PROJ_SUBTYPE_PROCEDURES_DOCUMENT,
    ],
    [
        PROJ_SUBTYPE_CREATIVE_FICTION,
        PROJ_SUBTYPE_CREATION_NON_FICTION,
    ],
    [
        PROJ_SUBTYPE_DECISION_RATIONALE,
        PROJ_SUBTYPE_SELECTION_ANALYSIS,
        PROJ_SUBTYPE_RECOMMENDATION,
    ],
    [
        PROJ_SUBTYPE_EMAIL,
        PROJ_SUBTYPE_LETTER,
        PROJ_SUBTYPE_MEMO,
        PROJ_SUBTYPE_NOTICE,
        PROJ_SUBTYPE_NEWSLETTER,
    ],
    [
        PROJ_SUBTYPE_ESSAY,
        PROJ_SUBTYPE_ARTICLE,
        PROJ_SUBTYPE_BLOG_POST,
        PROJ_SUBTYPE_E_BOOK,
        PROJ_SUBTYPE_BOOK,
        PROJ_SUBTYPE_WHITEPAPER,
    ],
    [
        PROJ_SUBTYPE_WEBSITE,
        PROJ_SUBTYPE_LANDING_PAGE,
        PROJ_SUBTYPE_ADVERTISEMENT,
        PROJ_SUBTYPE_FLIER,
        PROJ_SUBTYPE_BROCHURE,
    ],
    [
        PROJ_SUBTYPE_PROPOSAL,
        PROJ_SUBTYPE_QUOTE,
        PROJ_SUBTYPE_POTENTIAL_SCENARIO,
    ],
    [
        PROJ_SUBTYPE_SCOPE,
        PROJ_SUBTYPE_CHARTER,
        PROJ_SUBTYPE_BUSINESS_REQUIREMENTS_DOCUMENT,
    ],
    [
        PROJ_SUBTYPE_STRATEGY,
        PROJ_SUBTYPE_PLAN,
        PROJ_SUBTYPE_GOAL_OUTLINE,
        PROJ_SUBTYPE_DEFINITION_DOCUMENT,
    ],
    [
        PROJ_SUBTYPE_HOW_TO_ARTICLE,
        PROJ_SUBTYPE_PATENT_SPECIFICATION,
        PROJ_SUBTYPE_PRODUCT_MANUAL,
    ],
    [
        PROJ_SUBTYPE_CURRICULUM,
        PROJ_SUBTYPE_TRAINING_DOCUMENT
    ]
]

sub_type_list = [
PROJ_SUBTYPE_ASSESSMENT,
PROJ_SUBTYPE_REVIEW,
PROJ_SUBTYPE_REPORT,
PROJ_SUBTYPE_COMPARISON,
PROJ_SUBTYPE_POLICY_DOCUMENT,
PROJ_SUBTYPE_PROCEDURES_DOCUMENT,
PROJ_SUBTYPE_CREATIVE_FICTION,
PROJ_SUBTYPE_CREATION_NON_FICTION,
PROJ_SUBTYPE_DECISION_RATIONALE,
PROJ_SUBTYPE_SELECTION_ANALYSIS,
PROJ_SUBTYPE_RECOMMENDATION,
PROJ_SUBTYPE_EMAIL,
PROJ_SUBTYPE_LETTER,
PROJ_SUBTYPE_MEMO,
PROJ_SUBTYPE_NOTICE,
PROJ_SUBTYPE_NEWSLETTER,
PROJ_SUBTYPE_ESSAY,
PROJ_SUBTYPE_ARTICLE,
PROJ_SUBTYPE_BLOG_POST,
PROJ_SUBTYPE_E_BOOK,
PROJ_SUBTYPE_BOOK,
PROJ_SUBTYPE_WHITEPAPER,
PROJ_SUBTYPE_WEBSITE,
PROJ_SUBTYPE_LANDING_PAGE,
PROJ_SUBTYPE_ADVERTISEMENT,
PROJ_SUBTYPE_FLIER,
PROJ_SUBTYPE_BROCHURE,
PROJ_SUBTYPE_PROPOSAL,
PROJ_SUBTYPE_QUOTE,
PROJ_SUBTYPE_POTENTIAL_SCENARIO,
PROJ_SUBTYPE_SCOPE,
PROJ_SUBTYPE_CHARTER,
PROJ_SUBTYPE_BUSINESS_REQUIREMENTS_DOCUMENT,
PROJ_SUBTYPE_STRATEGY,
PROJ_SUBTYPE_PLAN,
PROJ_SUBTYPE_GOAL_OUTLINE,
PROJ_SUBTYPE_DEFINITION_DOCUMENT,
PROJ_SUBTYPE_HOW_TO_ARTICLE,
PROJ_SUBTYPE_PATENT_SPECIFICATION,
PROJ_SUBTYPE_PRODUCT_MANUAL,
PROJ_SUBTYPE_CURRICULUM,
PROJ_SUBTYPE_TRAINING_DOCUMENT
]



PROJ_SUBTYPE_CHOICES = [
    (PROJ_SUBTYPE_ASSESSMENT, PROJ_TEXT_SUBTYPE_ASSESSMENT),
    (PROJ_SUBTYPE_REVIEW, PROJ_TEXT_SUBTYPE_REVIEW),
    (PROJ_SUBTYPE_REPORT, PROJ_TEXT_SUBTYPE_REPORT),
    (PROJ_SUBTYPE_COMPARISON, PROJ_TEXT_SUBTYPE_COMPARISON),

    (PROJ_SUBTYPE_POLICY_DOCUMENT, PROJ_TEXT_SUBTYPE_POLICY_DOCUMENT),
    (PROJ_SUBTYPE_PROCEDURES_DOCUMENT, PROJ_TEXT_SUBTYPE_PROCEDURES_DOCUMENT),

    (PROJ_SUBTYPE_CREATIVE_FICTION, PROJ_SUBTYPE_CREATIVE_FICTION),
    (PROJ_SUBTYPE_CREATION_NON_FICTION, PROJ_SUBTYPE_CREATION_NON_FICTION),

    (PROJ_SUBTYPE_DECISION_RATIONALE, PROJ_TEXT_SUBTYPE_DECISION_RATIONALE),
    (PROJ_SUBTYPE_SELECTION_ANALYSIS, PROJ_TEXT_SUBTYPE_SELECTION_ANALYSIS),
    (PROJ_SUBTYPE_RECOMMENDATION, PROJ_TEXT_SUBTYPE_RECOMMENDATION),

    (PROJ_SUBTYPE_EMAIL, PROJ_TEXT_SUBTYPE_EMAIL),
    (PROJ_SUBTYPE_LETTER, PROJ_TEXT_SUBTYPE_LETTER),
    (PROJ_SUBTYPE_MEMO, PROJ_TEXT_SUBTYPE_MEMO),
    (PROJ_SUBTYPE_NOTICE, PROJ_TEXT_SUBTYPE_NOTICE),
    (PROJ_SUBTYPE_NEWSLETTER, PROJ_TEXT_SUBTYPE_NEWSLETTER),

    (PROJ_SUBTYPE_ESSAY, PROJ_TEXT_SUBTYPE_ESSAY),
    (PROJ_SUBTYPE_ARTICLE, PROJ_TEXT_SUBTYPE_ARTICLE),
    (PROJ_SUBTYPE_BLOG_POST, PROJ_TEXT_SUBTYPE_BLOG_POST),
    (PROJ_SUBTYPE_E_BOOK, PROJ_TEXT_SUBTYPE_E_BOOK),
    (PROJ_SUBTYPE_BOOK, PROJ_TEXT_SUBTYPE_BOOK),
    (PROJ_SUBTYPE_WHITEPAPER, PROJ_TEXT_SUBTYPE_WHITEPAPER),

    (PROJ_SUBTYPE_WEBSITE, PROJ_TEXT_SUBTYPE_WEBSITE),
    (PROJ_SUBTYPE_LANDING_PAGE, PROJ_TEXT_SUBTYPE_LANDING_PAGE),
    (PROJ_SUBTYPE_ADVERTISEMENT, PROJ_TEXT_SUBTYPE_ADVERTISEMENT),
    (PROJ_SUBTYPE_FLIER, PROJ_TEXT_SUBTYPE_FLIER),
    (PROJ_SUBTYPE_BROCHURE, PROJ_TEXT_SUBTYPE_BROCHURE),

    (PROJ_SUBTYPE_PROPOSAL, PROJ_TEXT_SUBTYPE_PROPOSAL),
    (PROJ_SUBTYPE_QUOTE, PROJ_TEXT_SUBTYPE_QUOTE),
    (PROJ_SUBTYPE_POTENTIAL_SCENARIO, PROJ_TEXT_SUBTYPE_POTENTIAL_SCENARIO),

    (PROJ_SUBTYPE_SCOPE, PROJ_TEXT_SUBTYPE_SCOPE),
    (PROJ_SUBTYPE_CHARTER, PROJ_TEXT_SUBTYPE_CHARTER),
    (PROJ_SUBTYPE_BUSINESS_REQUIREMENTS_DOCUMENT, PROJ_TEXT_SUBTYPE_BUSINESS_REQUIREMENTS_DOCUMENT),
    
    (PROJ_SUBTYPE_STRATEGY, PROJ_TEXT_SUBTYPE_STRATEGY),
    (PROJ_SUBTYPE_PLAN, PROJ_TEXT_SUBTYPE_PLAN),
    (PROJ_SUBTYPE_GOAL_OUTLINE, PROJ_TEXT_SUBTYPE_GOAL_OUTLINE),
    (PROJ_SUBTYPE_DEFINITION_DOCUMENT, PROJ_TEXT_SUBTYPE_DEFINITION_DOCUMENT),

    (PROJ_SUBTYPE_HOW_TO_ARTICLE, PROJ_TEXT_SUBTYPE_HOW_TO_ARTICLE),
    (PROJ_SUBTYPE_PATENT_SPECIFICATION, PROJ_TEXT_SUBTYPE_PATENT_SPECIFICATION),
    (PROJ_SUBTYPE_PRODUCT_MANUAL, PROJ_TEXT_SUBTYPE_PRODUCT_MANUAL),

    (PROJ_SUBTYPE_CURRICULUM, PROJ_TEXT_SUBTYPE_CURRICULUM),
    (PROJ_SUBTYPE_TRAINING_DOCUMENT, PROJ_TEXT_SUBTYPE_TRAINING_DOCUMENT),
]

PROJ_SUBTYPE_CHOICES_SEL = {
    PROJ_TYPE_ANALYSIS_REPORT: [
        (PROJ_SUBTYPE_ASSESSMENT, PROJ_TEXT_SUBTYPE_ASSESSMENT),
        (PROJ_SUBTYPE_REVIEW, PROJ_TEXT_SUBTYPE_REVIEW),
        (PROJ_SUBTYPE_REPORT, PROJ_TEXT_SUBTYPE_REPORT),
        (PROJ_SUBTYPE_COMPARISON, PROJ_TEXT_SUBTYPE_COMPARISON),
    ], 
    PROJ_TYPE_COMPLIANCE_DOCUMENT: [
        (PROJ_SUBTYPE_POLICY_DOCUMENT, PROJ_TEXT_SUBTYPE_POLICY_DOCUMENT),
        (PROJ_SUBTYPE_PROCEDURES_DOCUMENT, PROJ_TEXT_SUBTYPE_PROCEDURES_DOCUMENT),
    ],
    PROJ_TYPE_CREATIVE_CONTENT: [
        (PROJ_SUBTYPE_CREATIVE_FICTION, PROJ_SUBTYPE_CREATIVE_FICTION),
        (PROJ_SUBTYPE_CREATION_NON_FICTION, PROJ_SUBTYPE_CREATION_NON_FICTION),
    ], 
    PROJ_TYPE_RATIONALE: [
        (PROJ_SUBTYPE_DECISION_RATIONALE, PROJ_TEXT_SUBTYPE_DECISION_RATIONALE),
        (PROJ_SUBTYPE_SELECTION_ANALYSIS, PROJ_TEXT_SUBTYPE_SELECTION_ANALYSIS),
        (PROJ_SUBTYPE_RECOMMENDATION, PROJ_TEXT_SUBTYPE_RECOMMENDATION),
    ], 
    PROJ_TYPE_DIRECT_COMMUNICATION: [
        (PROJ_SUBTYPE_EMAIL, PROJ_TEXT_SUBTYPE_EMAIL),
        (PROJ_SUBTYPE_LETTER, PROJ_TEXT_SUBTYPE_LETTER),
        (PROJ_SUBTYPE_MEMO, PROJ_TEXT_SUBTYPE_MEMO),
        (PROJ_SUBTYPE_NOTICE, PROJ_TEXT_SUBTYPE_NOTICE),
        (PROJ_SUBTYPE_NEWSLETTER, PROJ_TEXT_SUBTYPE_NEWSLETTER),
    ],
    PROJ_TYPE_PERSUASIVE_PIECE: [
        (PROJ_SUBTYPE_ESSAY, PROJ_TEXT_SUBTYPE_ESSAY),
        (PROJ_SUBTYPE_ARTICLE, PROJ_TEXT_SUBTYPE_ARTICLE),
        (PROJ_SUBTYPE_BLOG_POST, PROJ_TEXT_SUBTYPE_BLOG_POST),
        (PROJ_SUBTYPE_E_BOOK, PROJ_TEXT_SUBTYPE_E_BOOK),
        (PROJ_SUBTYPE_BOOK, PROJ_TEXT_SUBTYPE_BOOK),
        (PROJ_SUBTYPE_WHITEPAPER, PROJ_TEXT_SUBTYPE_WHITEPAPER),
    ], 
    PROJ_TYPE_PROMOTIONAL_CONTENT: [
        (PROJ_SUBTYPE_WEBSITE, PROJ_TEXT_SUBTYPE_WEBSITE),
        (PROJ_SUBTYPE_LANDING_PAGE, PROJ_TEXT_SUBTYPE_LANDING_PAGE),
        (PROJ_SUBTYPE_ADVERTISEMENT, PROJ_TEXT_SUBTYPE_ADVERTISEMENT),
        (PROJ_SUBTYPE_FLIER, PROJ_TEXT_SUBTYPE_FLIER),
        (PROJ_SUBTYPE_BROCHURE, PROJ_TEXT_SUBTYPE_BROCHURE),
    ], 
    PROJ_TYPE_BUSINESS_PROPOSAL: [
        (PROJ_SUBTYPE_PROPOSAL, PROJ_TEXT_SUBTYPE_PROPOSAL),
        (PROJ_SUBTYPE_QUOTE, PROJ_TEXT_SUBTYPE_QUOTE),
        (PROJ_SUBTYPE_POTENTIAL_SCENARIO, PROJ_TEXT_SUBTYPE_POTENTIAL_SCENARIO),
    ],
    PROJ_TYPE_REQUIREMENTS_DOCUMENT: [
        (PROJ_SUBTYPE_SCOPE, PROJ_TEXT_SUBTYPE_SCOPE),
        (PROJ_SUBTYPE_CHARTER, PROJ_TEXT_SUBTYPE_CHARTER),
        (PROJ_SUBTYPE_BUSINESS_REQUIREMENTS_DOCUMENT, PROJ_TEXT_SUBTYPE_BUSINESS_REQUIREMENTS_DOCUMENT),
    ], 
    PROJ_TYPE_FUTURE_SCENARIO: [
        (PROJ_SUBTYPE_STRATEGY, PROJ_TEXT_SUBTYPE_STRATEGY),
        (PROJ_SUBTYPE_PLAN, PROJ_TEXT_SUBTYPE_PLAN),
        (PROJ_SUBTYPE_GOAL_OUTLINE, PROJ_TEXT_SUBTYPE_GOAL_OUTLINE),
        (PROJ_SUBTYPE_DEFINITION_DOCUMENT, PROJ_TEXT_SUBTYPE_DEFINITION_DOCUMENT),
    ], 
    PROJ_TYPE_TECHNICAL_DOCUMENT: [
        (PROJ_SUBTYPE_HOW_TO_ARTICLE, PROJ_TEXT_SUBTYPE_HOW_TO_ARTICLE),
        (PROJ_SUBTYPE_PATENT_SPECIFICATION, PROJ_TEXT_SUBTYPE_PATENT_SPECIFICATION),
        (PROJ_SUBTYPE_PRODUCT_MANUAL, PROJ_TEXT_SUBTYPE_PRODUCT_MANUAL),
    ],
    PROJ_TYPE_TRAINING_PROGRAM: [
        (PROJ_SUBTYPE_CURRICULUM, PROJ_TEXT_SUBTYPE_CURRICULUM),
        (PROJ_SUBTYPE_TRAINING_DOCUMENT, PROJ_TEXT_SUBTYPE_TRAINING_DOCUMENT),
    ],
}


# Project 'doc_len' options
PROJ_DOCSIZE_1 = 'PDS_1'
PROJ_DOCSIZE_UPTO_5 = 'PDS_UPTO_5'
PROJ_DOCSIZE_UPTO_20 = 'PDS_UPTO_20'
PROJ_DOCSIZE_UNLIMITED = 'PDS_UNLIMITED'

PROJ_DOCSIZE_DEFAULT = PROJ_DOCSIZE_1                     # default project doc_len on creation

PROJ_TEXT_DOCSIZE_1 = '1 Page'
PROJ_TEXT_DOCSIZE_UPTO_5 = 'Upto 5 Pages'
PROJ_TEXT_DOCSIZE_UPTO_20 = 'Upto 20 Pages'
PROJ_TEXT_DOCSIZE_UNLIMITED = 'Unlimited'

document_length_list = [
PROJ_DOCSIZE_1,
PROJ_DOCSIZE_UPTO_5,
PROJ_DOCSIZE_UPTO_20,
PROJ_DOCSIZE_UNLIMITED
]

PROJ_DOCSIZE_CHOICES = [
    (PROJ_DOCSIZE_1, PROJ_TEXT_DOCSIZE_1),
    (PROJ_DOCSIZE_UPTO_5, PROJ_TEXT_DOCSIZE_UPTO_5),
    (PROJ_DOCSIZE_UPTO_20, PROJ_TEXT_DOCSIZE_UPTO_20),
    (PROJ_DOCSIZE_UNLIMITED, PROJ_TEXT_DOCSIZE_UNLIMITED),
]

# Project 'doc_topic' options
PROJ_TOPIC_PERSON = 'PTOP_1'
PROJ_TOPIC_COMPANY = 'PTOP_2'
PROJ_TOPIC_GROUP = 'PTOP_3'
PROJ_TOPIC_PRODUCT_SERVICE = 'PTOP_4'
PROJ_TOPIC_CONCEPT_THING = 'PTOP_5'
PROJ_TOPIC_PLACE_DEST_BUILDING = 'PTOP_6'

PROJ_TOPIC_DEFAULT = PROJ_TOPIC_PERSON                  # default project doc_topic on creation

PROJ_TEXT_TOPIC_PERSON = 'Person'
PROJ_TEXT_TOPIC_COMPANY = 'Company'
PROJ_TEXT_TOPIC_GROUP = 'Group'
PROJ_TEXT_TOPIC_PRODUCT_SERVICE = 'Product or Service'
PROJ_TEXT_TOPIC_CONCEPT_THING = 'Concept or Thing'
PROJ_TEXT_TOPIC_PLACE_DEST_BUILDING = 'Place, Destination or Building'

subject_type_list=[
PROJ_TOPIC_PERSON,
PROJ_TOPIC_COMPANY,
PROJ_TOPIC_GROUP,
PROJ_TOPIC_PRODUCT_SERVICE,
PROJ_TOPIC_CONCEPT_THING,
PROJ_TOPIC_PLACE_DEST_BUILDING
]

PROJ_TOPIC_CHOICES = [
    (PROJ_TOPIC_PERSON, PROJ_TEXT_TOPIC_PERSON),
    (PROJ_TOPIC_COMPANY, PROJ_TEXT_TOPIC_COMPANY),
    (PROJ_TOPIC_GROUP, PROJ_TEXT_TOPIC_GROUP),
    (PROJ_TOPIC_PRODUCT_SERVICE, PROJ_TEXT_TOPIC_PRODUCT_SERVICE),
    (PROJ_TOPIC_CONCEPT_THING, PROJ_TEXT_TOPIC_CONCEPT_THING),
    (PROJ_TOPIC_PLACE_DEST_BUILDING, PROJ_TEXT_TOPIC_PLACE_DEST_BUILDING),
]

# project initial questions/properties
PROP_TARGET_READER = 'PROP_TARGET_READER'
PROP_TOPIC_NAME = 'PROP_TOPIC_NAME'
PROP_TOPIC_IMPACT = 'PROP_TOPIC_IMPACT'
PROP_TARGET_IMPRESSION = 'PROP_TARGET_IMPRESSION'
PROP_TOPIC_CAUSE = 'PROP_TOPIC_CAUSE'

PROJ_BASE_PROPS = [
    PROP_TARGET_READER,
    PROP_TOPIC_NAME,
    PROP_TOPIC_IMPACT,
    PROP_TARGET_IMPRESSION,
    PROP_TOPIC_CAUSE,
]

# project initial questions flow
INIT_Q_TITLE = 'INIT_Q_TITLE'       # attr
INIT_Q_TYPE = 'INIT_Q_TYPE'         # attr
INIT_Q_SUBTYPE = 'INIT_Q_SUBTYPE'   # attr
INIT_Q_DOC_LEN = 'INIT_Q_LEN'       # attr
INIT_Q_DOC_TOPIC = 'INIT_Q_TOPIC'   # attr
INIT_Q_PROP = 'INIT_Q_PROP'         # props

INIT_Q_ATTR_NAME_LIST = {
    INIT_Q_TITLE: 'title',
    INIT_Q_TYPE: 'doc_type',
    INIT_Q_SUBTYPE: 'doc_subtype',
    INIT_Q_DOC_LEN: 'doc_len',
    INIT_Q_DOC_TOPIC: 'doc_topic',
}

PROJ_INIT_QUESTIONS_FLOW = {
    '-2': {
        'ID': INIT_Q_TITLE,
    },
    '-1': {
        'ID': INIT_Q_TYPE,
    },
    '0': {
        'ID': INIT_Q_SUBTYPE,
    },
    '1': {
        'ID': INIT_Q_PROP,
        'STEPS': [
            PROP_TARGET_READER,
        ],
    },
    '2': {
        'ID': INIT_Q_DOC_TOPIC,
    },
    '3': {
        'ID': INIT_Q_PROP,
        'STEPS': [
            PROP_TOPIC_NAME,
            PROP_TOPIC_IMPACT,
            PROP_TARGET_IMPRESSION,
            PROP_TOPIC_CAUSE,
        ],
    },
    '4': {
        'ID': INIT_Q_DOC_LEN,
    },
}

PROJ_HOME_URLNAME = 'project'
PROJ_UPD_ATTR_URLNAME = 'project-update'
PROJ_UPD_PROP_URLNAME = 'project-prop-update'

def getFlowBackUrlAttr(curr, stp=None):
    burl = None
    battr = None
    for n, q in PROJ_INIT_QUESTIONS_FLOW.items():
        if q['ID'] == INIT_Q_PROP:
            for p in q['STEPS']:
                if curr == INIT_Q_PROP and stp == p:
                    return burl, battr
                burl = PROJ_UPD_PROP_URLNAME
                battr = p
        else:
            if q['ID'] == curr:
                return burl, battr
            burl = PROJ_UPD_ATTR_URLNAME
            battr = INIT_Q_ATTR_NAME_LIST[q['ID']]
    # return url for last step in flow
    return burl, battr

def getFlowNextUrlAttr(curr, stp=None):
    found = False
    for n, q in PROJ_INIT_QUESTIONS_FLOW.items():
        if found:
            if q['ID'] == INIT_Q_PROP:
                return PROJ_UPD_PROP_URLNAME, q['STEPS'][0]
            else:
                return PROJ_UPD_ATTR_URLNAME, INIT_Q_ATTR_NAME_LIST[q['ID']]
        if q['ID'] == curr:
            if q['ID'] == INIT_Q_PROP:
                for p in q['STEPS']:
                    if found:
                        return PROJ_UPD_PROP_URLNAME, p
                    if p == stp:
                        found = True
            else:
                found = True
    return PROJ_HOME_URLNAME, None

def getFlowNextNameStep(curr, stp=None):
    found = False
    for n, q in PROJ_INIT_QUESTIONS_FLOW.items():
        if found:
            return q['ID'], INIT_Q_ATTR_NAME_LIST[q['ID']]
        if q['ID'] == curr:
            if q['ID'] == INIT_Q_PROP:
                for p in q['STEPS']:
                    if found:
                        return q['ID'], p
                    if p == stp:
                        found = True
            else:
                found = True
    # probably should lead to basecamp
    return PROJ_HOME_URLNAME, None

INIT_Q_ATTR_INV_LIST = {
    'title': INIT_Q_TITLE,
    'doc_type': INIT_Q_TYPE,
    'doc_subtype': INIT_Q_SUBTYPE,
    'doc_len': INIT_Q_DOC_LEN,
    'doc_topic': INIT_Q_DOC_TOPIC,
}

def getAttrName(attr_val):
    return INIT_Q_ATTR_INV_LIST.get(attr_val, None)



PAGE_TIP = ["""<p>
    <strong>WHAT</strong>
    : A <em>definitive</em> question.
</p>
<p>
    Clearly and succinctly define your topic and select ‘Next’ to move to the
    next question.
</p>
<p>
    Your answer should follow on from the lead-in text below (no need to repeat
    the lead-in text in your answer).
</p>
<p>
    Use ‘Answer for me’ to try to find a result on the web (works for most
    simple topics).
</p>
<p>
    You can edit the web result to tailor it to your document.
</p>
<p>
    Some topics are specific to you and may require more thought or research to
    prepare the best answer.
</p>"""
, """<p>
    <strong>WHERE</strong>
    : A <em>location</em> question - relates to a destination, aspect, place in
    time, division, space or place.
</p>
<p>
    Your answer should follow on from the lead-in text (do not repeat the
    lead-in text). This understanding of context is used by the HyperQuestions
    AI Engine.
</p>
<p>
    <u> </u>
</p>
<p>
    <u>Example</u>
    :
</p>
<p>
    <strong>Question</strong>
    :
    <em>
        Where could a poodle enhance the life of elderly nursing home
        residents?
    </em>
</p>
<p>
    <strong>Lead-in</strong>
    :
    <em>
        A poodle could enhance the life of elderly nursing home residents in …
    </em>
</p>
<p>
    <strong>Answer</strong>
    :
    <em>
        … low-care nursing homes that offer independent living and allow
        residents to keep pets.
    </em>
</p>
<p>
    <em> </em>
</p>
<p>
    <u>Not sure this is the perfect question for you? </u>
</p>
<p>
    Use grey arrows to see alternate versions of the question – you may use any
    one of these.
</p>
<p>
    Your selection will be locked-in once you enter an answer and click ‘Next’.
</p>
<p>
    The ‘Edit’ button will edit all questions across this topic and can only be
    undertaken before a response is entered and saved (by hitting ‘Next’).
</p>
<p>
    <u>Edit options include</u>
    : Changing the tense of the question, changing the expression of the
    subject or object and changing the relationship between subject and object
    (positive relationship, negative or neutral).
</p>
<p>
    On hitting ‘Done’ all questions will be refreshed for this topic.
</p>
<p>
    If none of the above offers a question you feel is workable, you can go
    back and change the topic, or skip this question by typing the answer as
    ‘Skip’.
</p>
<p>
    Enter an answer (by voice or typing) and click ‘Next’ to save your response
    and proceed to the next question or topic selection process.
</p>""","""<p>
    <strong>WHEN</strong>
    : A <em>time-related</em> question - relates to defining a point in time.
</p>
<p>
    For example, next month, next year, in January, in the next decade, in 30
    seconds, during his youth, in the Jurassic period etc.
</p>
<p>
    Your answer should follow on from the lead-in text (not repeat the lead-in
    text). This understanding of context is used by the HyperQuestions Ai
    Engine.
</p>
<p>
    <u>Example</u>
    :
</p>
<p>
    <strong>Question</strong>
    :
    <em>
        When could a poodle enhance the life of elderly nursing home residents?
    </em>
</p>
<p>
    <strong>Lead-in</strong>
    :
    <em>
        A poodle could enhance the life of elderly nursing home residents when
        …
    </em>
</p>
<p>
    <strong>Answer</strong>
    :
    <em>
        … they have been able to experience the companionship associated with
        caring for and receiving affection from an animal. Residents have
        noticed an improvement in their outlook, attitude and zest for life
        within 6 months of receiving a poodle to care for.
    </em>
</p>
<p>
    <em><u>Not sure this is the perfect question for you?</u> </em>
</p>
<p>
    Use grey arrows to see alternate versions of the question – you may use any
    one of these. Your selection will be locked in once you enter an answer and
    click next.
</p>
<p>
    The edit button will edit all questions across this topic and can only be
    undertaken before a response is entered and saved (by hitting next). Edit
    options include: changing the tense of the question, changing the
    expression of the subject or object and changing the relationship between
    subject and object (positive relationship, negative or neutral). On hitting
    “done” all questions will be re-loaded for this topic.
</p>
<p>
    If none of the above offers a question you feel is workable, you can go
    back and change the topic, or skip this question by typing the answer as
    “skip”.
</p>
<p>
    Enter an answer (voice or typing) and click next to save your response and
    proceed to the next question or topic selection process.
</p>""", """<p>
    <strong>How</strong>
    : a method or functional question - this question relates to defining the
    approach by which a result will be achieved.
</p>
<p>
    For example, by using XYZ resources, deploying the ABC methodology, using
    the XYZ approach, doing A) then B) then C).
</p>
<p>
    An answer should follow on from the lead-in text (not repeat the lead-in
    text). This understanding of context is used by the HyperQuestions Ai
    Engine.
</p>
<p>
    <strong> </strong>
</p>
<p>
    <u>Example</u>
    :
</p>
<p>
    <strong>Question</strong>
    :
    <em>
        How can a poodle enhance the life of elderly nursing home residents?
    </em>
</p>
<p>
    <strong>Lead-in</strong>
    :
    <em>
        A poodle can enhance the life of elderly nursing home residents by …
    </em>
</p>
<p>
    <strong>Answer</strong>
    :
    <em>
        … providing a reason for living. Through the need to feed and provide
        water to the dog each day, residents experience a level of purpose,
        they have often not had for many years. These efforts are rewarded
        through the love and affection provided by the dog, sitting on their
        lap each evening.
    </em>
</p>
<p>
    <strong> </strong>
</p>
<p>
    <u>Not sure this is the perfect question for you? </u>
</p>
<p>
    Use grey arrows to see alternate versions of the question – you may use any
    one of these. Your selection will be locked in once you enter an answer and
    click next.
</p>
<p>
    The edit button will edit all questions across this topic and can only be
    undertaken before a response is entered and saved (by hitting next). Edit
    options include: changing the tense of the question, changing the
    expression of the subject or object and changing the relationship between
    subject and object (positive relationship, negative or neutral). On hitting
    “done” all questions will be re-loaded for this topic.
</p>
<p>
    If none of the above offers a question you feel is workable, you can go
    back and change the topic, or skip this question by typing the answer as
    “skip”.
</p>
<p>
    Enter an answer (voice or typing) and click next to save your response and
    proceed to the next question or topic selection process.
</p>""", """<p>
    <strong>WHY</strong>
    : a <em>reasoning</em> question - this question relates to outlining a
    rationale or reason to explain what makes this important.
</p>
<p>
    For example, provides XYZ benefits, informs ABC, offers advanages to XYZ
    group, enables XYZ process.
</p>
<p>
    An answer should follow on from the lead-in text (not including the lead-in
    text). This understanding of context is used by the HyperQuestions Ai
    Engine.
</p>
<p>
    <strong>Example:</strong>
</p>
<p>
    <strong>Question</strong>
    :
    <em>
        How can a poodle enhance the life of elderly nursing home residents?
    </em>
</p>
<p>
    <strong>Lead-in</strong>
    :
    <em>
        A poodle can enhance the life of elderly nursing home residents because
        …
    </em>
</p>
<p>
    <strong>Answer</strong>
    :
    <em>
        … is can provide love and support beyond that which is provided by
        family and friends. They offer a 24/7 bedside companion that responds
        to touch and provides new meaning to the lives of the elderly.
    </em>
</p>
<p>
    <strong> </strong>
</p>
<p>
    <u>Not sure this is the perfect question for you? </u>
</p>
<p>
    Use grey arrows to see alternate versions of the question – you may use any
    one of these. Your selection will be locked in once you enter an answer and
    click next.
</p>
<p>
    The edit button will edit all questions across this topic and can only be
    undertaken before a response is entered and saved (by hitting next). Edit
    options include: changing the tense of the question, changing the
    expression of the subject or object and changing the relationship between
    subject and object (positive relationship, negative or neutral). On hitting
    “done” all questions will be re-loaded for this topic.
</p>
<p>
    If none of the above offers a question you feel is workable, you can go
    back and change the topic, or skip this question by typing the answer as
    “skip”.
</p>
<p>
    Enter an answer (voice or typing) and click next to save your response and
    proceed to the next question or topic selection process.
</p>"""]