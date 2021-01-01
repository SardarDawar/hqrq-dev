#Controls use of topicFinder
from  . import variableLibrary as vl
import inflect
from . import topicFinder
p = inflect.engine()
#import heirarchy1 as he
#import questionSelector as qs

def masterMethodAllocator(l,le,topic,userDefinedProspect) :
    vl.answerModifier = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1}
    vl.postQuestionMessage = {0: "", 1: "", 2: "", 3: "", 4: ""}
    selectedMethod = vl.doc_list2_2[vl.masterDocTypeSelection]
    print(selectedMethod[0])
    print("received L and Le",l,le)

    if selectedMethod[0] == "freeForm" :

        # True means change the topic on the node and in topicfinder run (a True change) to run "phantom questions" but retain original node topic then false
        #node zero
        if l == 0 and le == 0 :
            topic = "testing subject"
            userDefinedProspect = "testing object"
            #vl.finalQuestions[0,1]
            #topicOveride = "Santa Clause" #topic to run in topicFinder
            #topicfindermethod = wiki # determines function to run
            return True,topic, userDefinedProspect
        #l = level 1
        if (l == 1):
            # le = Node index
            if (le == 0) :
                topic = "northern lights"
                userDefinedProspect = "southern lights"
                updatedPWOIndex = 2
                updatedPWOIndex = int(updatedPWOIndex)
                vl.proposalWordsOutcome = vl.pwoLists[updatedPWOIndex]
                return True,topic,userDefinedProspect

            if (le == 1):
                topic = "car"
                userDefinedProspect = "Switzerland"

                print("changing to car", topic, type(topic))
                return True,topic,userDefinedProspect
                # presentedquestions = questionList[1,3,5]
                # vl.userDefinedSubject = topic

        if (l == 2):
            if (le == 1):
                topic = "fatty"
                userDefinedProspect = "North Pole"
                print("changing to fatty")
                return True, topic, userDefinedProspect


    elif selectedMethod == "tocBased" :

        donothing = "donothing"

    elif selectedMethod[0] == "criticalThinking":

        # True means change the topic on the node and in topicfinder run (a True change) to run "phantom questions" but retain original node topic then false
        # node zero
        if l == 0 and le == 0:


            return True, topic, userDefinedProspect
            donothing = "donothing"
            # XXXX Send Data to Front End XXXX
            # vl.finalQuestionstoDisplay[0,3]
            # vl.finalQuestionsMessage [0 : ""],[3: "Name three reasons]
            # vl.answerFormatOverideDefault [3 : 3] - tells for question at index three to take three answers
            # topicfindermethod = Skip topic finder and uses reasons as selected topics

        # l = level 1
        if (l == 1):
            # le = Node index
            if (le == 0):
                donothing = "donothing"
                # XXXX Send Data to Front End XXXX
                # vl.finalQuestionstoDisplay[0,1,3,4]
                # vl.finalQuestionsMessage [3: "Name three reasons]
                # vl.answerFormatOverideDefault [3 : 3] - tells for question at index three to take three answers
                # topicfindermethod = Skip topic finder and uses reasons as selected topics for children

            if (le == 1):
                donothing = "donothing"
                # XXXX Send Data to Front End XXXX
                # vl.finalQuestionstoDisplay[0,2,3,4]
                # vl.finalQuestionsMessage [3: "Name three reasons]
                # vl.answerFormatOverideDefault [3 : 3] - tells for question at index three to take three answers
                # topicfindermethod = Skip topic finder and uses reasons as selected topics for children

            if (le == 2):
                donothing = "donothing"
                # XXXX Send Data to Front End XXXX
                # vl.finalQuestionstoDisplay[0,1,4]
                # vl.finalQuestionsMessage [3: "Name three reasons]
                # no children - skip topic finder and add no subtopics
        #Level 2
        if (l == 2):
            if (le == 0):
                donothing = "donothing"
                # XXXX Send Data to Front End XXXX
                # vl.finalQuestionstoDisplay[0,1,3,4]
                # vl.finalQuestionsMessage [3: "Name three reasons]
                # vl.answerFormatOverideDefault [3 : 3] - tells for question at index three to take three answers
                # topicfindermethod = Skip topic finder and uses reasons as selected topics for children

            if (le == 1):
                donothing = "donothing"
                # XXXX Send Data to Front End XXXX
                # vl.finalQuestionstoDisplay[0,2,3,4]
                # vl.finalQuestionsMessage [3: "Name three reasons]
                # vl.answerFormatOverideDefault [3 : 3] - tells for question at index three to take three answers
                # topicfindermethod = Skip topic finder and uses reasons as selected topics for children

            if (le == 2):
                donothing = "donothing"
                # XXXX Send Data to Front End XXXX
                # vl.finalQuestionstoDisplay[0,1,4]
                # vl.finalQuestionsMessage [3: "Name three reasons]
                # no children - skip topic finder and add no subtopics
        #Level 3
        if (l == 3):
            if (le == 0):
                donothing = "donothing"
                # XXXX Send Data to Front End XXXX
                # vl.finalQuestionstoDisplay[0,1,3,4]
                # vl.finalQuestionsMessage [3: "Name three reasons]
                # vl.answerFormatOverideDefault [3 : 3] - tells for question at index three to take three answers
                # topicfindermethod = Skip topic finder and uses reasons as selected topics for children

            if (le == 1):
                donothing = "donothing"
                # XXXX Send Data to Front End XXXX
                # vl.finalQuestionstoDisplay[0,2,3,4]
                # vl.finalQuestionsMessage [3: "Name three reasons]
                # vl.answerFormatOverideDefault [3 : 3] - tells for question at index three to take three answers
                # topicfindermethod = Skip topic finder and uses reasons as selected topics for children

            if (le == 2):
                donothing = "donothing"
                # XXXX Send Data to Front End XXXX
                # vl.finalQuestionstoDisplay[0,1,4]
                # vl.finalQuestionsMessage [3: "Name three reasons]
                # no children - skip topic finder and add no subtopics
                # Terminate Here and re-call heirarchy with different variables

    elif selectedMethod[0] == "methodologyBased":
        donothing = "donothing"

    elif selectedMethod[0] == "promotional":

        if (l == 0):
            # l is leve and le = Node index
            # Vl's update current in variable library
            if (le == 0):
                vl.activeQuestions = [0, 1, 2, 4]
                vl.answerModifier = {0: 1, 1: 1, 2: 1, 3: 3, 4: 1}
                vl.postQuestionMessage = {0: "", 1: "", 2: "", 3: "", 4: ""}

                topic = vl.subjectName
                print("vl affected by",vl.affectedBy)
                userDefinedProspect = vl.affectedBy
                updatedPWOIndex = 3
                updatedPWOIndex = int(updatedPWOIndex)
                vl.proposalWordsOutcome = vl.pwoLists[updatedPWOIndex]
                return True, topic, userDefinedProspect

        if (l == 1):
            # l is leve and le = Node index
            # Vl's update current in variable library
            if (le == 0) :
                vl.activeQuestions = [0,2,4]
                vl.answerModifier = {0:1, 1:1, 2:1, 3:1, 4:1}
                vl.postQuestionMessage = {0: "", 1: "", 2: "", 3: "provide 3 reasons", 4: ""}

                topic = vl.userDefinedSubject
                userDefinedProspect = vl.userDefinedProspect
                updatedPWOIndex = 1
                updatedPWOIndex = int(updatedPWOIndex)
                vl.proposalWordsOutcome = vl.pwoLists[updatedPWOIndex]
                print("topic is", topic)
                return True,topic,userDefinedProspect
            if (le == 1) :
                vl.activeQuestions = [0,1,3]
                vl.answerModifier = {0:1, 1:1, 2:1, 3:3, 4:1}
                vl.postQuestionMessage = {0: "", 1: "", 2: "", 3: "Enter three reasons", 4: ""}

                # topic = vl.userDefinedSubject
                # userDefinedProspect = vl.userDefinedProspect
                updatedPWOIndex = 1
                updatedPWOIndex = int(updatedPWOIndex)
                vl.proposalWordsOutcome = vl.pwoLists[updatedPWOIndex]
                return True,topic,userDefinedProspect
            if (le == 2) :
                vl.activeQuestions = [0,2,4]
                vl.answerModifier = {0:1, 1:1, 2:1, 3:3, 4:1}
                vl.postQuestionMessage = {0: "", 1: "", 2: "", 3: "", 4: ""}

                # topic = vl.userDefinedSubject
                # userDefinedProspect = vl.userDefinedProspect
                updatedPWOIndex = 1
                updatedPWOIndex = int(updatedPWOIndex)
                vl.proposalWordsOutcome = vl.pwoLists[updatedPWOIndex]
                return True,topic,userDefinedProspect
            if (le == 3) :
                vl.activeQuestions = [0,2,4]
                vl.answerModifier = {0:1, 1:1, 2:1, 3:1, 4:1}
                vl.postQuestionMessage = {0: "", 1: "", 2: "", 3: "", 4: ""}

                # topic = vl.userDefinedSubject
                # userDefinedProspect = vl.userDefinedProspect
                updatedPWOIndex = 1
                updatedPWOIndex = int(updatedPWOIndex)
                vl.proposalWordsOutcome = vl.pwoLists[updatedPWOIndex]
                return True,topic,userDefinedProspect
            if (le == 4) :
                vl.activeQuestions = [0,1]
                vl.answerModifier = {0:3, 1:1, 2:1, 3:1, 4:1}
                vl.postQuestionMessage = {0: "Enter three reasons", 1: "", 2: "", 3: "", 4: ""}

                # topic = vl.userDefinedSubject
                # userDefinedProspect = vl.userDefinedProspect
                updatedPWOIndex = 1
                updatedPWOIndex = int(updatedPWOIndex)
                vl.proposalWordsOutcome = vl.pwoLists[updatedPWOIndex]
                return True,topic,userDefinedProspect
        donothing = "Need to request - pass three answers for question[3] through to topicFinder - auto"


    elif selectedMethod[0] == "historical":
        donothing = "donothing"
    else :
        donothing = "donothing"

    return False, topic, userDefinedProspect



#Method 1 - Vanilla Heirarchy - Freeform
            # def freeForm() :
            #     dog = cat
    #Done
    # Rerun all questions on a node (with new variables) and keep original variables (Creates "Phantom Questions") - achieved in Quesiton Selector
    # intercept question generation at a node and inject "phantom variable" based on level and index on level
    # intercept question generation at a node and inject "new variable" based on level and index on level and update core variable (eg. Userdefined subject)

    #To Do
    #re-run all questions on a node with different variables and replace original (update node name, update uds, update udp, update pwo, update tense)
    #control number of questions sent to front end based on level and index

    #artificially add a node (pre-program to add one automatically)
    #enable manual addition to topic list @ level 0
    #program node question eg Q5 to take multiple answers

    #run hierachy multiple times and yet manage overall document size


    #enable "tuning" of topic Finder based on different doc types



#****** Method 2 - Critical thinking ********
# def criticalThinking() :
#     if vl.activeNodeId == 0 :
#         vl.userDefinedSubject = front_end_questions.affectedBy
#         presentedQuestions = questionselector.questionstopresent[0,1,4]
#
# # for the below to work active node Id's need to be stored as indexes in a list so we can find index zero on a level
#     if vl.level == 1 :
#         if vl.activeNodeId[0]
#             vl.userDefinedProspect = front_end_questions.affectingOn + front_end_questions.affectingOn
#             presentedQuestions = Questionselector.questionstopresent[0,1,2,3,4]
#             #re-run node with different variables???
#         if vl.activeNodeId[1]
#             vl.userDefinedProspect = front_end_questions.affectingOn + front_end_questions.affectingOn
#             presentedQuestions = questionselector.questionstopresent[0,4]
#         if vl.activeNodeId[2]
#             vl.userDefinedProspect = front_end_questions.affectingOn + front_end_questions.affectingOn
#             presentedQuestions = questionselector.questionstopresent[0,3]
#         if vl.activeNodeId[3]
#             vl.userDefinedProspect = vl.userDefinedProspect
#             presentedQuestions = questionselector.questionstopresent[1,4]
#         if vl.activeNodeId[4]
#             vl.userDefinedProspect = vl.userDefinedProspect
#             presentedQuestions = questionselector.questionstopresent[5]
#         if vl.activeNodeId[5:]
#             vl.userDefinedProspect = vl.userDefinedProspect
#             presentedQuestions = questionselector.questionstopresent[5]
#     if vl.level == 2 :
#         if vl.activeNodeId[0]
#             vl.userDefinedProspect = front_end_questions.affectingOn + front_end_questions.affectingOn
#             presentedQuestions = Questionselector.questionstopresent[0,1,4]
#         if vl.activeNodeId[1]
#             vl.userDefinedProspect = front_end_questions.affectingOn + front_end_questions.affectingOn
#             presentedQuestions = questionselector.questionstopresent[0,4]
#         if vl.activeNodeId[2]
#             vl.userDefinedProspect = front_end_questions.affectingOn + front_end_questions.affectingOn
#             presentedQuestions = questionselector.questionstopresent[0,3]
#         if vl.activeNodeId[3]
#             vl.userDefinedProspect = vl.userDefinedProspect
#             presentedQuestions = questionselector.questionstopresent[1,4]
#         if vl.activeNodeId[4]
#             vl.userDefinedProspect = vl.userDefinedProspect
#             presentedQuestions = questionselector.questionstopresent[5]
#         if vl.activeNodeId[5:]
#             vl.userDefinedProspect = vl.userDefinedProspect
#             presentedQuestions = questionselector.questionstopresent[5]
#     if vl.level == > 2:
#         if vl.activeNodeId[0]
#             vl.userDefinedProspect = front_end_questions.affectingOn + front_end_questions.affectingOn
#             presentedQuestions = Questionselector.questionstopresent[0, 1, 4]
#         if vl.activeNodeId[1]
#             vl.userDefinedProspect = front_end_questions.affectingOn + front_end_questions.affectingOn
#             presentedQuestions = questionselector.questionstopresent[0, 4]
#         if vl.activeNodeId[2]
#             vl.userDefinedProspect = front_end_questions.affectingOn + front_end_questions.affectingOn
#             presentedQuestions = questionselector.questionstopresent[0, 3]
#         if vl.activeNodeId[3]
#             vl.userDefinedProspect = vl.userDefinedProspect
#             presentedQuestions = questionselector.questionstopresent[1, 4]
#         if vl.activeNodeId[4]
#             vl.userDefinedProspect = vl.userDefinedProspect
#             presentedQuestions = questionselector.questionstopresent[5]
#         if vl.activeNodeId[5:]
#             vl.userDefinedProspect = vl.userDefinedProspect
#             presentedQuestions = questionselector.questionstopresent[5]
#
#
#
#     # run node x multiple times with different variables -  retain original
#     # run node x multiple times with different variables -  update original
#     # program node question eg Q5 to take multiple answers
#     # modify a specific question on a node after generation (changing PWO, UDS or UDP)
#     # re-run a question on a node with different variables and replace original
#     # rerun aquesiton on a node (with new variables) and keep original variables
#     # run heairachy multipole times and yet manage overall document size
#     # artificially add a node (pre-program to add one automatically)
#     # enable manual addition to topic list @ level 0
#     # enable "tuning" of topic Finder based on different doc types
#     # determine which questions to show based on level and position in heirarchy (eg. L1 Node 2 show only 1 1 and 3 - call two question template
#
#
# #Method 3 - Methodology based
# def methodology() :
#
#
#     # run node x multiple times with different variables -  retain original
#     # run node x multiple times with different variables -  update original
#     # program node question eg Q5 to take multiple answers
#     # modify a specific question on a node after generation (changing PWO, UDS or UDP)
#     # re-run a question on a node with different variables and replace original
#     # rerun aquesiton on a node (with new variables) and keep original variables
#     # run heairachy multipole times and yet manage overall document size
#     # artificially add a node (pre-program to add one automatically)
#     # enable manual addition to topic list @ level 0
#     # enable "tuning" of topic Finder based on different doc types
#     # determine which questions to show based on level and position in heirarchy (eg. L1 Node 2 show only 1 1 and 3 - call two question template
#
#
# #Method 4 - Toc based
# def toc()
#
#
#     # run node x multiple times with different variables -  retain original
#     # run node x multiple times with different variables -  update original
#     # program node question eg Q5 to take multiple answers
#     # modify a specific question on a node after generation (changing PWO, UDS or UDP)
#     # re-run a question on a node with different variables and replace original
#     # rerun aquesiton on a node (with new variables) and keep original variables
#     # run heairachy multipole times and yet manage overall document size
#     # artificially add a node (pre-program to add one automatically)
#     # enable manual addition to topic list @ level 0
#     # enable "tuning" of topic Finder based on different doc types
#     # determine which questions to show based on level and position in heirarchy (eg. L1 Node 2 show only 1 1 and 3 - call two question template
#
#
# # Method 5 - promotional
# def promotional() :
#
#     # run node x multiple times with different variables -  retain original
#     # run node x multiple times with different variables -  update original
#     # program node question eg Q5 to take multiple answers
#     # modify a specific question on a node after generation (changing PWO, UDS or UDP)
#     # re-run a question on a node with different variables and replace original
#     # rerun aquesiton on a node (with new variables) and keep original variables
#     # run heairachy multipole times and yet manage overall document size
#     # artificially add a node (pre-program to add one automatically)
#     # enable manual addition to topic list @ level 0
#     # enable "tuning" of topic Finder based on different doc types
#     # determine which questions to show based on level and position in heirarchy (eg. L1 Node 2 show only 1 1 and 3 - call two question template
#
#
# # Method 6 - Historical
#
#     # run node x multiple times with different variables -  retain original
#     # run node x multiple times with different variables -  update original
#     # program node question eg Q5 to take multiple answers
#     # modify a specific question on a node after generation (changing PWO, UDS or UDP)
#     # re-run a question on a node with different variables and replace original
#     # rerun aquesiton on a node (with new variables) and keep original variables
#     # run heairachy multipole times and yet manage overall document size
#     # artificially add a node (pre-program to add one automatically)
#     # enable manual addition to topic list @ level 0
#     # enable "tuning" of topic Finder based on different doc types
#     # determine which questions to show based on level and position in heirarchy (eg. L1 Node 2 show only 1 1 and 3 - call two question template

def topicDeterminer(node,l) :
    # return false if you dont want to go through topic finder.
    selectedMethod = vl.doc_list2_2[vl.masterDocTypeSelection]
    subtopics = []

    if selectedMethod[0] == "freeForm":

        subtopics = topicFinder.wiki_run(node)[0:15]
        print("\n", node, "WIKI Search COMPLETED\n")
        return False, subtopics

    elif selectedMethod[0] == "criticalThinking":
        print("l",l)
        if l == 1 :
            subtopics = ["injected topic for selection 1","injected topic for selection 2","injected topic for selection 3"]
        else :
            node = "another dummy topic"
            subtopics = topicFinder.data_google(node)[0:15]
            print("\n", node, "WIKI Search COMPLETED\n")
        return False, subtopics

    elif selectedMethod[0] == "methodologyBased":
        subtopics = []
        subtopics = topicFinder.wiki_run(node)[0:15]
        print("\n", node, "WIKI Search COMPLETED\n")
        return False, subtopics


    elif selectedMethod[0] == "promotional":
        print("l", l)
        if vl.detailedDoctypeSelected == "landing page" :
            if l == 1:
                if vl.userDefinedSubject[-1] != "s" :
                    updatedSubject = vl.userDefinedSubject + "s'"
                else :
                    updatedSubject = vl.userDefinedSubject + "'"
                subject1 = "the key features of " + vl.userDefinedSubject
                subject2 = "the major benefits of " + vl.userDefinedSubject
                subject3 = "the track record of success"
                subject4 = "you should consider " + vl.userDefinedSubject + " to"
                subject5 = "the top three reasons you should " + vl.actionOrImpression + " of " + vl.userDefinedSubject
                subtopics = [subject1, subject2, subject3, subject4, subject5]
                return True, subtopics
            else:
                subtopics = []
                subtopics = topicFinder.wiki_run(node)[0:15]
                print("\n", node, "WIKI Search COMPLETED\n")
                return False, subtopics
        else :
            subtopics = []
            subtopics = topicFinder.wiki_run(node)[0:15]
            print("\n", node, "WIKI Search COMPLETED\n")
            return False, subtopics

    elif selectedMethod[0] == "historical":
        print("l", l)
        if l == 1:
            if vl.userDefinedSubject[-1] != "s" :
                updatedSubject = vl.userDefinedSubject + "s'"
            else :
                updatedSubject = vl.userDefinedSubject + "'"
            subject1 = "the key features of " + vl.userDefinedSubject
            subject2 = "the major benefits of " + vl.userDefinedSubject
            subject3 = updatedSubject + " " + " track record of success"
            subtopics = [subject1, subject2, subject3]
            return True, subtopics
        else:
            node = "fish"
            subtopics = topicFinder.data_google(node)[0:15]
        return False, subtopics

    else:
        subtopics = []
        subtopics = topicFinder.wiki_run(node)[0:15]
        print("\n", node, "WIKI Search COMPLETED\n")
        return False, subtopics

