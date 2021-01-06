#determines how to express a topic (plural or singular and a or the or nothing)
import re                                      # REGULAR EXPRESSIONS.
import inflect                                 # PLURAL/SINGULAR PACKAGE.
import spacy                                   # NLP PACKAGE.
import nltk                                    # NLP PACKAGE.
from . import variableLibrary as vl
from .uncount import uncount_list               # IMPORTING UNCOUNTABLE WORDS.
from .help_funcs import user_query
from .app_lists import stops, min_tags, mid_tags, maxp_tags, maxs_tags
from .app_lists import sym_tags, con_tags
from .the_places import the_words, the_list, the_singular

nlp = spacy.load("en_core_web_md")             # LOADING SPACY DB.
p = inflect.engine()


def base_word(phrase):
    if phrase.find(" ") >= 0 :
        try:
            # LOOKING FOR ROOT WORD IN THE PHRASE.
            doc = nlp(phrase)
            b_word, u_word = None, None
            wl = phrase.split()
            for wch in doc.noun_chunks:
                if wch.root.dep_ == "ROOT":
                    b_word, u_word = wch.root.text, wch.root.text
            if b_word is None:
                if "with" in wl:
                    b_word, u_word = wl[0], wl[-1]
                if "of" in wl:
                    b_word, u_word = wl[0], wl[0]
                if "and" in wl:
                    b_word, u_word = wl[0], wl[0]
            if b_word is None:
                tags = [i.tag_ for i in doc]
                ix = -1
                for tg in tags[::-1]:
                    if tg in min_tags+sym_tags+con_tags:
                        ix -= 1
                    else:
                        break
                b_word, u_word = wl[ix], wl[ix]
            if b_word is None:
                b_word, u_word = wl[-1], wl[-1]
            # print("BASE WORD: %s\nUNCOUNTABLE CHECK: %s\n" % (b_word, u_word))
            return (b_word, u_word)
        except Exception:
            print("\nROOT WORDS AND UNCOUNT WORDS UNAVAILABLE!!!\n")
    else:
        b_word = phrase
        u_word = phrase
        return (b_word,u_word)
    # not sure if I need an exception here in case it fails

def q_comb(driver=None, article=None, query=None, prefix="What"):
    ql = [driver, article, query]
    quest_list = [l for l in ql if l is not None]
    question = "%s %s?" % (prefix, " ".join(quest_list))
    return question


def the_rule(query, b_word, driver, article):
    question = q_comb(driver=driver, article=article, query=query)
    doc = nlp(question)
    for ent in doc.ents:
        # print(ent.label_)
        if (ent.label_ == "ORG") or (ent.label_ == "GPE") or (
                ent.label_ == "PERSON"):
            if ent.end_char-ent.start_char == len(query):
                driver, article = driver, None
    if "of" in query.split()[1:]:
        if query.split()[0].lower() in stops:
            driver, article = driver, None
        else:
            driver, article = driver, "the"
    if ("on" in query.split()[1:]) or ("and" in query.split()[1:]) :
        if query.split()[0].lower() in stops:
            driver, article = driver, None
        else:
            driver, article = driver, article
    if (b_word.lower() in the_list) and (len(query.split()) > 1):
        if query.split()[0].lower() in stops:
            driver, article = driver, None
        else:
            driver, article = driver, "the"
    if query in the_list:
        if query.split()[0].lower() in stops:
            driver, article = driver, None
        else:
            driver, article = driver, article
    if query in the_words:
        if query.split()[0].lower() in stops:
            driver, article = driver, None
        else:
            driver, article = driver, "the"
    return (driver, article)


def q_what(query):
    queryLI = ""

    if query.find("my ") == 0:
        queryLI = query
        query = query.replace("my ", "your ")

    if query.find("My ") == 0:
        queryLI = query
        query = query.replace("My ", "your ")

    if "Our " in query :
        if query.find("Our ") == 0 :
            queryLI = query
            query = query.replace("Our ", "Your ")

    if "our " in query :
        if query.find("our ") == 0 :
            queryLI = query
            query = query.replace("our ", "your ")

    if query.find("me ") == 0:
        queryLI = query
        query = query.replace("me ", "you ")


    try:
        u_article, query = user_query(query)
        bw = base_word(query)
        b_word, u_word = bw[0], bw[1]
        reg1 = re.compile(r"[a-zA-Z0-9][.][a-z]")
        # if b_word.istitle():
        #     doc = nlp(b_word)
        #     for token in doc:
        #         tag = token.tag_
                # print(token.text, token.lemma_, token.pos_, token.tag_,
                #       token.dep_, token.shape_, token.is_alpha, token.is_stop)
#        else:
        word = nltk.word_tokenize(b_word)
        tag = nltk.pos_tag(word)[0][1]
#        print(b_word, tag)
        if (tag == "NN") or (tag =="VBG") or (tag == "VB") or (
                tag == "JJR") or (tag == "JJ") or (tag == "MD"):
            # print("Singular (is)")
            driver= "is"
            article = p.a(query.split()[0]).split()[0]
            # print("inflect article: ", article)
        elif (tag == "NNPS") or (tag == "NNS"):
            driver, article = "are", None
            if b_word in the_singular:
                driver, article = "is", "the"
        elif tag == "NNP":
            # print("Not Countable (no article)")
            driver, article = "is", None
        else:
            # print("Plural (are)")
            driver, article  = "is", None
        if b_word.endswith("ing"):
            article = None
        elif b_word.endswith("ness"):
            article = None
        elif b_word.endswith("less"):
            article = None
        elif b_word.endswith("ism"):
            article = None
        elif (reg1.search(u_word)) or (reg1.search(b_word)):
            driver, article = "is", None
        else:
            # print("Possibly countable (a or the)")
            article = article
        word_set = set(uncount_list)
        phrase_set = set(u_word.split())
        if word_set.intersection(phrase_set):
            article = None
        da = the_rule(query, b_word, driver, article)
        driver, article = da[0], da[1]
        if u_article is not None:
            article = u_article
            #Post processing for person related terms - to strip article
        if vl.passThroughExpressorFlag != True or query.find("your ") > -1 or query.find("his ") > -1 or query.find("her ") > -1 or query.find("their ") > -1 or query.find("you ") > -1:
            if query.find("a ") == 0:
                query = query.replace("a ", "")
            if query.find("an ") == 0:
                query = query.replace("an ", "")
            elif query.find("the ") == 0:
                query = query.replace("the ", "")


            article = None
        question = q_comb(driver=driver, article=article, query=query)
        # if both words plural then it is plural
        # if first word is plural and second is singular then singular
        # if first word is singular and second word is plural then plural
        # if both words singular then singular
        # query = word_tokenize(tag)
        # numberOfWords = len(query)
        # print(numberOfWords)
        # query = query[numberOfWords -1]
        # print(query)
        # print("question",question)
        # print("data current",question[question.index("the"):question.index(" ")])
        # print("question number", q_number(question)[0])
        # if(question[0:question.index(" ")] == "the" and q_number(question) == 4) :
        #     question = question[question.index(" ") +1:]
        #     print("changed",question)
        topicExpressed = ""
        if article is None :
            topicExpressed = query
        else :
            topicExpressed = article + " " + query
        # print("test data",question)
        return (question, query, driver, article, queryLI, b_word, u_word, tag, topicExpressed)
    except Exception:
        print("\nQUESTIONS UNAVAILABLE!!!\n")


def q_number(expres):
    try:
        # RETURNS NUMBER OF TOPIC AND QUESTION
        # 1 - What is topic?
        # 2 - What are topic?
        # 3 - What is a topic?
        # 4 - What is the topic?
        # 5 - What are the topic?
        a = " are "
        c = " the "
        d = " a "
        e = " an "
        if expres.find(a) >= 0 :
            if expres.find(c) >= 0:
                q_num = 5
            else :
                q_num = 2
        else :
            if expres.find(d) >= 0 :
                q_num = 3
            elif expres.find(e) >= 0:
                    q_num = 3
            elif expres.find((c)) >=1 :
                q_num = 4
            else :
                q_num = 1
        return (q_num, expres)
    except Exception:
        print("\nNUMBERING OF TOPIC UNAVAILABLE!!!\n")



if __name__ == "__main__":
    search_term = "mum"
    question = q_what(search_term)
    try:
        qn = q_number(question[0])
        print("%s) %s" % (qn[0], qn[1].strip()))
        print(qn[0])
    except Exception:
        pass