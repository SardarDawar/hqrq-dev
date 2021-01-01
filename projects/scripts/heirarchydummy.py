# master process for bringing together elements sequentially
from . import heirarchyControlModule
from . import variableLibrary as vl
from . import topicFinder
import inflect
from . import topic_expressor as te
import random
p = inflect.engine()
Heirarchy = []
NodeVariables = []
NodeTracking = {}
NodeId = 0
global lv
lv = 1
selectedOrientation = -1 # selects positive, negative neutral
proposalWordOutcome = 'impact'

def questionGenerator(userDefinedSubject,userDefinedProspect) :

    whatQuestion = ["What is " + userDefinedSubject,]
    whereQuestion = ["Where will " + userDefinedSubject + " impact " + userDefinedProspect, "Where could " + userDefinedSubject + " alter " + userDefinedProspect, "Where should " + userDefinedSubject + " change " + userDefinedProspect]
    whenQuestion = ["When should " + userDefinedSubject + " change " + userDefinedProspect, "When will " + userDefinedSubject + " form " + userDefinedProspect, "When can " + userDefinedSubject + " alter " + userDefinedProspect]
    howQuestion = ["How can " + userDefinedSubject + " change " + userDefinedProspect, "How does " + userDefinedSubject + " change " + userDefinedProspect, "How can " + userDefinedSubject + " alter " + userDefinedProspect]
    whyQuestion = ["Why can " + userDefinedSubject + " change " + userDefinedProspect,   "Why does " + userDefinedSubject + " change " + userDefinedProspect, "Why can " + userDefinedSubject + " alter " + userDefinedProspect]

    filteredQuestionList = [whatQuestion,whereQuestion, whenQuestion, howQuestion, whyQuestion]


    whatLeadin = [userDefinedSubject + " is"]
    whereLeadin = [userDefinedSubject + " will impact " + userDefinedProspect + " in", userDefinedSubject + " could alter " + userDefinedProspect + " in ", userDefinedSubject + " will change " + userDefinedProspect + " in "]
    whenLeadin = [userDefinedSubject + " should change " + userDefinedProspect + " when", userDefinedSubject + " will form " + userDefinedProspect + " when", userDefinedSubject + " can alter " + userDefinedProspect + " when"]
    howLeadin = [userDefinedSubject + " can change " + userDefinedProspect + " by", userDefinedSubject + " changes " + userDefinedProspect + " by", userDefinedSubject + " alters " + userDefinedProspect + " by"]
    whyLeadin = [userDefinedSubject + " can change " + userDefinedProspect + " because ", userDefinedSubject + " does change " + userDefinedProspect + " because ", userDefinedSubject + " can alter " + userDefinedProspect  + " because"]

    leadingText = [whatLeadin, whereLeadin, whenLeadin, howLeadin, whyLeadin]
    print("Question Indexes to display in Front End", vl.activeQuestions)
    print("Number of Answers to take by question index", vl.answerModifier)
    return (filteredQuestionList, leadingText, vl.postQuestionMessage)




def heirarchyDummy(firstName, tenseChoice, docLengthChoice, endingLevel, userDefinedProspect ,userDefinedSubject) :
    activeQuestions = [0,1,2,3,4]
    vl.activeQuestions = activeQuestions
    leadingTextIndex = []
    global NodeId
    changingStatus,userDefinedSubject1,userDefinedProspect = heirarchyControlModule.masterMethodAllocator(0,0,userDefinedSubject,userDefinedProspect)
    if changingStatus :
        userDefinedSubject = userDefinedSubject1
    # question = te.q_what(userDefinedSubject)
    # udsNo = te.q_number(question[0])
    # vl.udsNo = udsNo

    # question = te.q_what(userDefinedProspect)
    # udpNo = te.q_number(question[0])
    # vl.udpNo = udpNox


    # questionGenerator(userDefinedSubject,userDefinedProspect)
    # for index in range(len(filteredQuestionList)) :
    #     print(filteredQuestionList[index])
    #     print(leadingText[index])
    #     if(not postQuestionMessage.get(index) == "") :
    #         print(postQuestionMessage.get(index))
    #         # return vl.postQuestionMessage.get(index)
    #     else :
    #         print("Message is empty - No message")
            # return "Message is empty - No message" 

    return questionGenerator(userDefinedSubject,userDefinedProspect)
        #leadingText = leadingTextGenerator.RuleMapper(question)
    print(" first presented questions above ")

    proceed = input("Would you like to re-structure the questions (enter Y or N) :  ")
    while proceed == "Y" :

        userDefinedSubject = input("Updated User Defined Subject")
        #vl.userDefinedSubject = userDefinedSubject

        # question = te.q_what(vl.userDefinedSubject)
        # print("quesiton",question)
        # udsNo = te.q_number(question[0])
        # print(udsNo)
        # vl.udsNo = udsNo
        if userDefinedSubject.find("a ") != 0 and userDefinedSubject.find("the ") != 0:
            vl.passThroughExpressorUDS = False
        else :
            vl.passThroughExpressorUDS = True
        userDefinedProspect = input("Updated User Defined Prospect")
        # question = te.q_what(vl.userDefinedProspect)
        # print("quesiton prospect",question)
        # udpNo = te.q_number(question[0])
        # print(udpNo)
        # vl.udpNo = udpNo
        if userDefinedProspect.find("a ") != 0 and userDefinedProspect.find("the ") != 0:
            vl.passThroughExpressorUDP = False
        else :
            vl.passThroughExpressorUDP = True

        updatedTense = input("Please enter a Tense number 1-5")
        updatedPWOIndex = input("Please select your Orientation (1 for positive, 2 for negative, 3 for neutral")
        updatedPWOIndex = int(updatedPWOIndex)
        vl.proposalWordsOutcome = vl.pwoLists[updatedPWOIndex]
        #updatedPWO = input("Enter your Orientation - Positive, Negative, Neutral")
        updatedTense = int(updatedTense)
        questionGenerator(userDefinedSubject, userDefinedProspect)
        vl.passThroughExpressor = True
        # filteredQuestionList = gl.filterQuestions(questionList)
        # leadingTextIndex = []
        # for index in range(len(filteredQuestionList)):
        #     leadingTextIndex.append([])
        #     for question in filteredQuestionList[index]:
        #         leadingText = leadingTextGenerator.RuleMapper(question)
        #         leadingTextIndex[index].append(leadingText)
        # for question in filteredQuestionList:
        #     print(question)
        # for leadingText in leadingTextIndex:
        #     print(leadingText)
        # print("Question Indexes to display in Front End", vl.activeQuestions)
        # print("Number of Answers to take by question index", vl.answerModifier)
        # for index in vl.activeQuestions:
        #     print(filteredQuestionList[index])
        #     print(leadingTextIndex[index])
        #     if (not vl.postQuestionMessage.get(index) == ""):
        # #         print(vl.postQuestionMessage.get(index))
        #     else:
        #         print("Message is empty - No message")
        vl.proposalWordsOutcome = vl.pwoLists[int(vl.orienationIndex)]
        print("The Node Zero Rerun questions are above ")

        proceed = input("Would you like to re-structure the questions (enter Y or N) :  ")
    # leadingTextIndex = []
    # for index in range(len(filteredQuestionList)):
    #     leadingTextIndex.append([])
    #     # for question in filteredQuestionList[index]:
    #     #     leadingText = leadingTextGenerator.RuleMapper(question)
    #     #     leadingTextIndex[index].append(leadingText)
    #     #     print(filteredQuestionList[index])
    #     #     print(leadingTextIndex[index])
    #     #     if (not vl.postQuestionMessage.get(index) == ""):
    #     #         print(vl.postQuestionMessage.get(index))
    #     #     else:
    #     #         print("Message is empty - No message")
    #             # for question in filteredQuestionList:
    # #     print(question)
    # # for leadingText in leadingTextIndex:
    # #     print(leadingText)
        questionGenerator(userDefinedSubject, userDefinedProspect)
        node = userDefinedSubject
    # print(" final questions for node Zero above ")

    Heirarchy.append({userDefinedSubject: [userDefinedSubject]})
    global NodeId
    NodeTracking.update({NodeId: {"level": 0, "parent": userDefinedSubject, "levelIndex": 0, "Name": userDefinedSubject}})
    vl.activeQuestions = activeQuestions
    print(NodeTracking)
    input("stop")
    NodeId += 1
    vl.activeNodeId = NodeId
    print("vl.userDefined Prospect",vl.userDefinedProspect)
    print("vl.usewrDefined Subject",vl.userDefinedSubject)

#below is to be able to run different topic in topic finder (to original node) - to be provided from heirarchy control module
    # global topicOveride
    # topicOveride = ""
    # if topicOveride != "":
    #     node = topicOveride
    for level in Heirarchy:
        print(level)
    #    print("questionlist", questionList)
    choice = "Y"
    level = 0
    l = 0

    while (choice != "N"):
        for x in range(level, level + 1):
            for lev in Heirarchy:
                # print(lev)
                dictt = {}
                for k, v in lev.items():
                    for node in v:
                        if (l == endingLevel - 1):
                            choice = "N"
                            print("breaking it here",node)
                            break
                        subtopics = []
                        global le
                        changingStatus, subtopics = heirarchyControlModule.topicDeterminer(node,l + 1)

#                        userDefinedProspect = userDefinedSubject
#                         userDefinedProspect = vl.userDefinedSubject
#                         print("changing userdefined prospect", userDefinedProspect)

                        topicList = []

                        print("length of subtopics", len(subtopics))
                        if not changingStatus :
                            if (len(subtopics) != 0):
                                topicMessage = "Select the most important topics for your " + vl.detailedDoctypeSelected
                                print(topicMessage)
                                count = 0
                                print("length of subtopics", len(subtopics))
    #                            global le
                                le = -1
                                for index in range(len(subtopics)):
                                    print(count, subtopics[index])
                                    count += 1
                                level1Subtopics = input("Select numbers using commas")
                                ch = -1
                                if level1Subtopics == "" :
                                    ch = 0
                                choice = "N"
                                if ch != 0 :
                                    try:
                                        for index in level1Subtopics.split(","):
                                            topicList.append(subtopics[int(index)])
                                    except:
                                        print("Not numbers and commas - enter manually")

                            choice = input("Do you want to add a topic - Press Y or N: ")
                            while (choice != "N"):
                                subject = input("Please enter your topic: ")
                                topicList.append(subject)
                                choice = input("Do you want to add a topic - Press Y or N: ")
                        else :
                            topicList = subtopics
                        print("got list",topicList)
                        dictt.update({node: topicList})
                        NodeVariables.append({node: [userDefinedProspect, proposalWordOutcome]})
                        le = -1
                        count = 0
                        for topic in topicList :
                            le +=1
                            count += 1
                            # if l+1 == 1 :
                                # if count == 4 :
                                #     count = 0
                                #     break
                            print("data topiclist", len(topicList),topicList)
                            # NodeTracking.update({NodeId: {"level": l + 1, "parent": node, "levelIndex": le, "Name": topic}})
                            # #print("node track :",NodeTracking)
                            # vl.activeNodeId = NodeId
                            # NodeId += 1
                            #print("questions for filtering ",topic)
                            #print("UDS before ",userDefinedSubject)
                            userDefinedProspect = node
                            print("changing userdefinedprospect to : ",userDefinedProspect)
                            print("l and le",l+1,le)

                            vl.userDefinedSubject = topic
                            userDefinedSubject = topic
                            #print("Vl uds after",topic)

                            changingStatus, userDefinedSubject1, userDefinedProspect = heirarchyControlModule.masterMethodAllocator(l + 1, le, userDefinedSubject, userDefinedProspect)
                            if changingStatus:
                                topicList[topicList.index(userDefinedSubject)] = userDefinedSubject1
                                userDefinedSubject = userDefinedSubject1
                                print("changing status active")
                            print("got user defined subject",userDefinedSubject)
                            questionGenerator(userDefinedSubject, userDefinedProspect)
                            # questionList = gl.createQuestions(userDefinedSubject, userDefinedProspect, tenseChoice)
                            # filteredQuestionList = gl.filterQuestions(questionList)
                            # leadingTextIndex=[]
                            # for index in range(len(filteredQuestionList)):
                            #     leadingTextIndex.append([])
                            #     for question in filteredQuestionList[index]:
                            #         leadingText = leadingTextGenerator.RuleMapper(question)
                            #         leadingTextIndex[index].append(leadingText)
                            # print("Question Indexes to display in Front End",vl.activeQuestions)
                            # print("Number of Answers to take by question index", vl.answerModifier)
                            # for index in vl.activeQuestions:
                            #     print(filteredQuestionList[index])
                            #     print(leadingTextIndex[index])
                            #     if (not vl.postQuestionMessage.get(index) == ""):
                            #         print(vl.postQuestionMessage.get(index))
                            #     else:
                            #         print("Message is empty - No message")
                            #
                            # print(" first presented questions above node 1+ ")
                            # post the filtered questions to variable library
                            proceed = input("Would you like to re-structure the questions (enter Y or N) :  ")
                            while proceed == "Y":
                                oldUserDefinedSubject = userDefinedSubject
                                userDefinedSubject = input("Updated User Defined Subject")
                                if userDefinedSubject.find("a ") != 0 and userDefinedSubject.find("the ") != 0:
                                    vl.passThroughExpressorUDS = False
                                else:
                                    vl.passThroughExpressorUDS = True

                                userDefinedProspect = input("Updated User Defined Prospect")
                                if userDefinedProspect.find("a ") != 0 and userDefinedProspect.find("the ") != 0:
                                    vl.passThroughExpressorUDP = False
                                else:
                                    vl.passThroughExpressorUDP = True
                                updatedTense = input("Please enter a Tense number 1-5")
                                updatedPWOIndex = input("Please select your Orientation (1 for positive, 2 for negative, 3 for neutral")
                                updatedPWOIndex = int(updatedPWOIndex)
                                vl.proposalWordsOutcome = vl.pwoLists[updatedPWOIndex]
                                # updatedPWO = input("Enter your Orientation - Positive, Negative, Neutral")
                                updatedTense = int(updatedTense)
                                questionGenerator(userDefinedSubject, userDefinedProspect)
                                # questionList = gl.createQuestions(userDefinedSubject, userDefinedProspect, updatedTense)
                                # topicList[topicList.index(oldUserDefinedSubject)] = userDefinedSubject
                                # filteredQuestionList = gl.filterQuestions(questionList)
                                # leadingTextIndex = []
                                # for index in range(len(filteredQuestionList)):
                                #     leadingTextIndex.append([])
                                #     for question in filteredQuestionList[index]:
                                #         leadingText = leadingTextGenerator.RuleMapper(question)
                                #         leadingTextIndex[index].append(leadingText)
                                #         print(filteredQuestionList[index])
                                #         if (not vl.postQuestionMessage.get(index) == ""):
                                #             print(vl.postQuestionMessage.get(index))
                                #         else:
                                #             print("Message is empty - No message")
                                #             # for question in filteredQuestionList:
                                # #     print(question)
                                # # for leadingText in leadingTextIndex:
                                # #     print(leadingText)
                                # print(vl.activeQuestions)
                                # for index in vl.activeQuestions:
                                #     print(filteredQuestionList[index])
                                #     print(leadingTextIndex[index])
                                #     if (not vl.postQuestionMessage.get(index) == ""):
                                #         print(vl.postQuestionMessage.get(index))
                                #     else:
                                #         print("Message is empty - No message")
                                vl.proposalWordsOutcome = vl.pwoLists[int(vl.orienationIndex)]
                                print("The Node 1+ Rerun questions are above ")

                                proceed = input("Would you like to re-structure the questions (enter Y or N) :  ")
                                questionGenerator(userDefinedSubject, userDefinedProspect)
                            # leadingTextIndex = []
                            # for index in range(len(filteredQuestionList)):
                            #     leadingTextIndex.append([])
                            #     for question in filteredQuestionList[index]:
                            #         leadingText = leadingTextGenerator.RuleMapper(question)
                            #         leadingTextIndex[index].append(leadingText)
                            print("NodeId",NodeId,"and vl.activenode id: ",vl.activeNodeId)
                            vl.activeQuestions = activeQuestions
                            NodeTracking.update({NodeId: {"level": l + 1, "parent": node, "levelIndex": le, "Name": userDefinedSubject}})
                            print("node track :",NodeTracking)
                            NodeId += 1
                            vl.activeNodeId = NodeId
                            input("breaking between nodes")

                if not not dictt:
                    Heirarchy.append(dictt)
                    l += 1
                    print(Heirarchy)
                    # userDefinedProspect = userDefinedSubject
                    # print("changing userdefined prospect",userDefinedProspect)
                    print('End of Level {}'.format(l))
    print(Heirarchy[-1])
    for k,v in Heirarchy[-1].items():
        for node in v :
            NodeVariables.append({node : [userDefinedProspect,proposalWordOutcome]})
    print(len(Heirarchy))
    for level in range(len(Heirarchy)):
        print(level, Heirarchy[level])
    print('Node Variables ')
    for node in range(len(NodeVariables)):
        print(NodeVariables[node])
    for k, v in NodeTracking.items():
        print(k, v)
    print(len(vl.usedQuestion))
    for k, v in vl.usedQuestion.items() :
        print(k,len(v))
        print(k,v)
#heirarchyMaster("Marcus",2,2,2,"Telstra","Market Research Assessment")

def parentFinder(childNode,level) :
    print(NodeTracking[level])
