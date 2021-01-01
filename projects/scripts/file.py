#Page 0a - Q1 This will come from account details - firstname
firstName = input("What is your first name?:  ")
firstName = firstName[0].upper() + firstName[1 : ]
if firstName[-1] == " " :
    firstName = firstName[:-1]
if firstName[-1] == "." :
    firstName = firstName[:-1]

#Page 0b - Name your project

q1 = "\nGreat, thanks " + firstName + ".  What would you like to call your new project?"
leadinText = "This new project will be called..."
tip = "Tips: Name your project something that will help you identify it.  Note that with HyperQuestions, we will use your name thorughout your document so pick something that also reads well"
suggestion = "Thinking will help you to distill many of the concepts involved in your document and prepare you for the process.  You can come back and change the document name before creating your document.  The document name will be used in your final document.  Here are some sample names to get you thinking: - Department of Defence HR Requirements - Microsoft Strategic Business Plan - Eucalypt Cultivation Guide - Plastic Products Overview"
print(q1 + "\n" + tip + "\n" + suggestion + "\n" + leadinText)
projectName = input()


#Page 1 - Q2 What mastere document type
q2 = "Ok so what type of document is your " + projectName + "? Select box below."
print("\n")

#update tip below to come from tip list
q2tip = "Tip: Once you select an option, a description of this type and its output formats will be displayed - this will help you be sure you have picked the best option.  Please consider carefully as each type may produce different outcomes – select one and see what it offers."
suggestion = "Select the closest category to your project.  What you are trying to create may be a sub-category - click and you will see the subtypes to help you select.  Your selection will potentially impact: - the method used for the remainder of the document creation process - the primary tense used in your document.  For example, a business proposal relates to the future. - the way in which key terms and inputs are interpreted by the HyperQuestions Ai Engine."
print(q2,"\n" + q2tip + "\n" + suggestion)
for x in range(len(vl.doc_list1)):
    print(x, vl.doc_list1[x])
masterDocTypeIndex = int(input("\nPlease enter Your choice (number) from the above list:  "))
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
q3tip = "Tip: these are sub-options associated with your selection of " + question[1] + ".  Once you select an option further information about its method and approach will be displayed."
suggestion = "Detailed document types more specifically detertmine the method, document length and output format for your document.  Select a box to see the details of that option"
print(q3,"\n" + q3tip + "\n" + suggestion)
docOptions = (vl.doc_list2[masterDocTypeIndex])
for x in range(len(docOptions)):
    print(x, docOptions[x])
detailedDoctype = int(input("\nPlease enter Your choice (number) from the above list:  "))
detailedDoctypeDesc = vl.doc_list2_1[masterDocTypeIndex][detailedDoctype]
print(detailedDoctypeDesc)
