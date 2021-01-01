# version for testing only - excludes google to prevent getting blocked
# import time
import concurrent.futures
import re
import requests
from bs4 import BeautifulSoup
import validators
from. import variableLibrary as vl
# import nltk
import spacy

nlp = spacy.load("en_core_web_sm")

search_text = vl.userDefinedSubject

if "a " in search_text or "A " in search_text :
    search_text = search_text[search_text.index(" ") + 1 :]


search_elements = ["elements of", "list of", "lists of", "aspects of",
                   "parts of", "components of", "how to", "main goals of",
                   "topics for", "type of", "types of", "kinds of"]

headers = {
    'User-Agent': 'Mozilla/6.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3770.80 Safari/557.36'}


# print(nltk.pos_tag(nltk.word_tokenize("Завантажити")))
# doc = nlp("All")
# for token in doc:
#     print(token.lemma_, token.pos_, token.tag_)

def wikiSearch(query=None):
    wlist = []
    reg = re.compile(r"[0-9]\s|ISBN|[0-9]-", re.M)
    url = "https://en.wikipedia.org/wiki/%s" % str(query)
    html = requests.get(url, headers=headers)
    if html.status_code == 200:
        soup = BeautifulSoup(html.text, 'html.parser')
        bshtml = soup.find("div", {"class": "mw-parser-output"})
        for tx1 in bshtml:
            try:
                if tx1.name == "ul":
                    for tx2 in tx1:
                        if tx2.name == "li":
                            for tx3 in tx2:
                                if tx3.name == "a":
                                    if reg.search(tx3.get_text()):
                                        pass
                                    else:
                                        tx = tx3.get_text()
                                        wlist.append(tx)
                if tx1.name == "div":
                    for tx2 in tx1:
                        if tx2.name == "ul":
                            for tx3 in tx2:
                                if tx3.name == "li":
                                    for tx4 in tx3:
                                        if tx4.name == "a":
                                            if reg.search(tx4.get_text()):
                                                pass
                                            else:
                                                tx = tx4.get_text()
                                                wlist.append(tx)
            except Exception:
                pass
    wlist = list(set(wlist))
    return (wlist, query.replace('_', ' '))


def googleSearch(query=None):
    google = []
    reg = re.compile(r"\.|\.\s...$", re.M)
    url = "https://google.com/search?q={%s}" % str(query)
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser')
    bshtml = soup.find_all("li")
    for t1 in bshtml:
        tx1 = t1.get_text()
        if reg.search(tx1):
            google.append(tx1)
    return (google, query.replace('+', ' '))


def data_wiki(query=None):
    wiki_list = []
    wiki_query = query.replace(' ', '_')
    res = wikiSearch(wiki_query)
    if len(res[0]) > 3:
        for result in res[0]:
            result = result.strip("\n\r\t\v. ...")
            if len(result.split()) < 10:
                if result != '':
                    wiki_list.append(result)
            else:
                pass
#    print("\n",query,"WIKI Search COMPLETED\n")
    return wiki_list


def data_google(query=None):
    sel = search_elements
    elem_list = []
    hows_list = []
    goal_list = []
    topi_list = []
    type_list = []
    workers = len(sel) + 1
    google_query = query.replace(' ', '+')
    search_list = [
        i.replace(' ', '+') + "+" + google_query for i in sel]
    ex1 = concurrent.futures.ThreadPoolExecutor(max_workers=workers)
    for g in ex1.map(googleSearch, search_list):
        if g is not None:
            el = g[1].split()
            if len(g[0]) > 3:
                for result in g[0]:
                    result = result.strip("\n\r\t\v. ...")
                    if len(result.split()) < 10:
                        if result != '':
                            for e in sel[0:5]:
                                if e == " ".join(el[0:2]):
                                    elem_list.append(result)
                            if sel[6] == " ".join(el[0:2]):
                                hows_list.append(result)
                            if sel[7] == " ".join(el[0:3]):
                                goal_list.append(result)
                            if sel[8] == " ".join(el[0:2]):
                                topi_list.append(result)
                            for e in sel[9:12]:
                                if e == " ".join(el[0:2]):
                                    type_list.append(result)
            else:
                pass
    ("\n.......GOOGLE Scrapping COMPLETED.......\n")
    return (elem_list, hows_list, goal_list, topi_list, type_list)


def google_result(query):
    try:
        query1 = query + " " + search_text
        query2 = query1.replace(' ', '+')
        url = "https://google.com/search?q={%s}" % str(query2)
        html = requests.get(url, headers=headers)
        if html.status_code == 200:
            bs = BeautifulSoup(html.text, 'html.parser')
            res = bs.find("div", {"id": "result-stats"})
            reg = re.findall(r"\d+", res.get_text())
            result = "".join(reg[0:len(reg) - 2])
            return (query, int(result))
    except Exception:
        pass


def google_first(query):
    url_list = []
    query = query.replace(' ', '+')
    url = "https://google.com/search?q={%s}" % str(query)
    html = requests.get(url, headers=headers)
    if html.status_code == 200:
        bs = BeautifulSoup(html.text, 'html.parser')
        res = bs.find("div", {"id": "search"})
        n = 0
        for r in res.find_all("a"):
            if validators.url(r["href"]):
                if n > 3:
                    break
                else:
                    result = r["href"]
                    url_list.append(result)
                    n += 1
        return url_list


def full_page(url):
    full_list = []
    html = requests.get(url, headers=headers)
    reg1 = re.compile(r"[a-zA-Z]", re.M)
    reg2 = re.compile(r"[0-9]\s|ISBN|[0-9]-", re.M)
    if html.status_code == 200:
        bs = BeautifulSoup(html.text, 'html.parser')
        for fl in bs.find_all(["h2", "b"]):
            tx = fl.get_text()
            if reg1.search(tx):
                if reg2.search(tx):
                    pass
                else:
                    full_list.append(tx)
        setf = set(full_list)
        full_list = list(setf)
        return full_list


def wiki_run(query):
    scrap_res = data_wiki(query=query)
    setl = set(scrap_res)
    scr = list(setl)
    w_list = []
    for sc in scr:
        irel = 0
        sc = sc.strip()
        for t in nlp(sc):
            if (t.tag_ == 'NNP') or (t.tag_ == 'NNPS') or (
                    t.tag_ == 'PRP$') or (t.tag_ == 'PRP') or (
                    t.tag_ == 'SYM') or (t.tag_ == 'CD') or (
                    t.tag_ == 'FW') or (t.tag_ == ':'):
                irel = 1
        if sc.title() == search_text.title():
            irel = 1
        if irel == 0:
            w_list.append(sc)
    # result_list = []
    # workers = len(w_list) + 1
    # ex1 = concurrent.futures.ThreadPoolExecutor(max_workers=workers)
    # for wg in ex1.map(google_result, w_list[0:20]):
    #     if wg is not None:
    #         result_list.append(wg)
    # result_list = sorted(result_list, key=lambda t: (-t[1], t[0]))
    # return result_list
    return w_list


def google_run(query):
    new_lists = []
    scrap_res = data_google(query=query)
    for grs in scrap_res:
        setl = set(grs)
        scr = list(setl)
        g_list = []
        for sc in scr:
            irel = 0
            sc = sc.strip()
            for t in nlp(sc):
                if (t.tag_ == 'NNPS') or (t.tag_ == 'PRP$') or (
                        t.tag_ == 'PRP') or (t.tag_ == 'SYM') or (
                        t.tag_ == 'CD') or (t.tag_ == 'FW') or (
                        t.tag_ == ':') or (t.tag_ == 'RB'):
                    irel = 1
            if sc.title() == search_text.title():
                irel = 1
            if irel == 0:
                sc = sc.replace(".", "")
                g_list.append(sc)
        new_lists.append(g_list)
    return new_lists


def full_run(query):
    url = google_first(query)
    ex2 = concurrent.futures.ThreadPoolExecutor(max_workers=3)
    for fres in ex2.map(full_page, url):
        if fres is not None:
            setl = set(fres)
            fls = list(setl)
            f_list = []
            for fl in fls:
                irel = 0
                fl = fl.strip()
                for t in nlp(fl):
                    if (t.tag_ == 'PRP$') or (t.tag_ == 'PRP') or (
                            t.tag_ == 'SYM') or (t.tag_ == 'CD') or (
                            t.tag_ == 'FW') or (t.tag_ == ':'):
                        irel = 1
                if fl.title() == search_text.title():
                    irel = 1
                if irel == 0:
                    f_list.append(fl.title())
            setl = set(f_list)
            f_list = list(setl)
            return f_list


# gr = google_run(search_text.title())
wr = wiki_run(search_text.title())

empty = 0
# term_names =["ELEMENTS OF", "HOW TO", "MAIN GOALS OF",
#              "TOPICS FOR", "TYPES OF"]
# for term, goog in zip(term_names, gr):
#     if len(goog) < 3:
#         empty += 1
#     else:
#         print("\n%s %s:" % (term, search_text.upper()))
#         for g in goog:
#             print(g)
result_list = []
if len(wr) < 3:
    empty += 1
else:
 #   print("\n%s %s:" % ("WIKIPEDIA", search_text.upper()))
#    print(wr[0:15])
    for w in wr[0:15]:
        result_list.append(w)
#        print(w)
if len(result_list) == 0 :
    result_list.append("test")
    result_list.append("test1")
    result_list.append("test2")
    result_list.append("test3")

#     txt = "articles on %s" % search_text.title()
#     query = txt.replace(' ', '+')
#     results = full_run(query)
#     print("\nFULL-PAGE SEARCH %s:" % txt)
#     for fpr in results:
#         print(fpr)

# with concurrent.futures.ThreadPoolExecutor(
#         max_workers=len(wiki_list)+1) as executor:
#     result = executor.submit(google_result, query)
#     res = google_result.result()