import random
import re
import requests
from bs4 import BeautifulSoup
from lxml.html import fromstring
# from itertools import cycle
import wikipediaapi
from wikipedia_api import wikipedia
import validators


def get_proxies():
    try:
        url = 'https://free-proxy-list.net/'
        response = requests.get(url)
        parser = fromstring(response.text)
        proxies = set()
        for i in parser.xpath('//tbody/tr')[0:10]:
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                proxy = ":".join([i.xpath('.//td[1]/text()')[0],
                                  i.xpath('.//td[2]/text()')[0]])
                proxies.add(proxy)
        return proxies
    except Exception:
        pass


def proxy_gen():
    try:
        proxy_work = None
        # proxies = get_proxies()
        # proxy_pool = cycle(proxies)
        # url = 'https://httpbin.org/ip'
        # for i in range(1, 11):
        #     proxy = next(proxy_pool)
        #     proxies = {"http": proxy, "https": proxy}
        #     try:
        #         requests.get(url, proxies=proxies)
        #         proxy_work = proxies
        #         break
        #     except:
        #         pass
        return proxy_work
    except Exception:
        pass


def head_gen():
    # RUNDOMLY GENERATES HEADERS FOR SCRAPPING.
    try:
        moz = float(random.randrange(5.0, 10.0, 1))
        awk = round(float(random.uniform(500.0, 600.0)), 2)
        saf = round(float(random.uniform(500.0, 600.0)), 2)
        chm = "%s.0.3770.80" % random.randrange(70, 85, 1)
        headers = {'User-Agent':
                   'Mozilla/%s (X11; Linux x86_64) AppleWebKit/%s (KHTML, like Gecko) Chrome/%s Safari/%s' % (
                       moz, awk, chm, saf)}
        return headers
    except Exception:
        print("\nHEADERS GENERATION UNAVAILABLE!!!\n")


def wiki_lists(query):
    # SCRAPPING LISTS AND LINKS OF THE WIKIPEDIA PAGE.
    try:
        wlist = []
        query = query.replace(' ', '_')
        headers = head_gen()
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
    except Exception:
        print("\nWIKIPEDIA LINKS AND LISTS SCRAPPING UNAVAILABLE!!!\n")


def wiki_summary(query):
    # SCRAPPING THE SUMMARY OF THE WIKIPEDIA PAGE.
    try:
        wikipedia.set_lang("en")
        wapi = wikipedia.page(query, auto_suggest=False)
        para = wapi.summary
        wpa_str = re.sub(r"\s\[.*?\]|\s\(.*?\)|\s\{.*?\}", "", para)
        wpa_list = wpa_str.split(".")
        return (wpa_list, query)
    except Exception:
        print("\nWIKIPEDIA SUMMARY SCRAPPING UNAVAILABLE!!!\n")


def wiki_suggest(query):
    # SCRAPPING THE SUGGEST FOR WIKIPEDIA PAGE.
    try:
        wapi = wikipedia.page(query, auto_suggest=True)
        para = wapi.summary
        wpa_str = re.sub(r"\s\[.*?\]|\s\(.*?\)|\s\{.*?\}", "", para)
        wpa_list = wpa_str.split(".")
        return (wpa_list, query)
    except Exception:
        print("\nWIKIPEDIA SUGGEST SCRAPPING UNAVAILABLE!!!\n")


def wiki_section(query):
    # SCRAPPING THE FIRST SECTION OF THE WIKIPEDIA PAGE. IF REFERS.
    try:
        wikia = wikipediaapi.Wikipedia('en')
        page = wikia.page(query)
        para = page.sections[0].text
        wpa_str = re.sub(r"\s\[.*?\]|\s\{.*?\}", "", para)
        wpa_list = wpa_str.split("\n")
        return (wpa_list, query)
    except Exception:
        print("\nWIKIPEDIA SECTION SCRAPPING UNAVAILABLE!!!\n")


def wiki_sections(query):
    # SCRAPPING SECTIONS, THAT NOT EMPTY, OF THE WIKIPEDIA PAGE. IF REFERS.
    try:
        wikia = wikipediaapi.Wikipedia('en')
        page = wikia.page(query)
        for s in page.sections:
            para = s.sections[0].text
            if len(para.split("\n")) > 1:
                break
        wpa_str = re.sub(r"\s\[.*?\]|\s\{.*?\}", "", para)
        wpa_list = wpa_str.split("\n")
        return (wpa_list, query)
    except Exception:
        print("\nWIKIPEDIA SECTIONS SCRAPPING UNAVAILABLE!!!\n")


def google_lists(query):
    # SCRAPPING LISTS OF THE GOOGLE PAGE.
    try:
        google = []
        query = query.replace(' ', '+')
        headers = head_gen()
        reg = re.compile(r"\.|\.\s...$", re.M)
        url = ["https://www.google.com/",
               "search?q={%s}" % query.lower(),
               "&hl=en", "&gl=us", "&lr=lang_en", "&safe=high"
               "&as_q={%s}" % query.lower()]
        url = "".join(url)
        html = requests.get(url, headers=headers)
        soup = BeautifulSoup(html.text, 'html.parser')
        bshtml = soup.find_all("li")
        for t1 in bshtml:
            tx1 = t1.get_text()
            if reg.search(tx1):
                google.append(tx1)
        return (google, query.lower().replace('+', ' '))
    except Exception:
        print("\nGOOGLE LISTS SCRAPPING UNAVAILABLE!!!\n")


def google_urls(query):
    # SCRAPPING OF THE URLS ON THE GOOGLE PAGE.
    try:
        url_list = []
        headers = head_gen()
        query = query.replace(' ', '+')
        url = ["https://www.google.com/",
               "search?q={%s}" % query.lower(),
               "&hl=en", "&gl=us", "&lr=lang_en", "&safe=high"]
        url = "".join(url)
        html = requests.get(url, headers=headers)
        if html.status_code == 200:
            bs = BeautifulSoup(html.text, 'html.parser')
            res = bs.find("div", {"id": "center_col"})
            n = 0
            for r in res.find_all("a"):
                if validators.url(r["href"]):
                    if n > 5:
                        break
                    else:
                        result = r["href"]
                        url_list.append(result)
                        n += 1
            return url_list
    except Exception:
        print("\nGOOGLE URLS SCRAPPING UNAVAILABLE!!!\n")


def google_result(query):
    # SCRAPPING OF THE GOOGLE RESULTS SEARCH NUMBER.
    try:
        headers = head_gen()
        query = query.replace(' ', '+')
        url = ["https://www.google.com/",
               "search?q={%s}" % query.lower(),
               "&hl=en", "&gl=us", "&lr=lang_en", "&safe=high"
               "&as_q={%s}" % query.lower()]
        url = "".join(url)
        html = requests.get(url, headers=headers)
        if html.status_code == 200:
            bs = BeautifulSoup(html.text, 'html.parser')
            res = bs.find("div", {"id": "result-stats"})
            reg = re.findall(r"\d+", res.get_text())
            result = "".join(reg[0:len(reg)-2])
            return (query.lower().replace('+', ' '), int(result))
    except Exception:
        print("\nGOOGLE RESULTS SCRAPPING UNAVAILABLE!!!\n")


def google_rbox(query):
    # SCRAPPING OF THE GOOGLE RIGHT BOX.
    try:
        g_list = []
        headers = head_gen()
        # proxies = proxy_gen()
        query = query.replace(' ', '+')
        url = ["https://www.google.com/",
               "search?q={%s}" % query.lower(),
               "&hl=en", "&gl=us", "&lr=lang_en", "&safe=high"
               "&as_q={%s}" % query.lower()]
        url = "".join(url)
        # html = requests.get(url, headers=headers, proxies=proxies)
        html = requests.get(url, headers=headers, proxies=None)
        if html.status_code == 200:
            bs = BeautifulSoup(html.text, 'html.parser')
            res = bs.find_all("div", {"class": "kno-rdesc"})
            for r in res:
                result = r.get_text().strip()
                sent = re.sub(r"Description", "", result)
                g_list = sent.split(".")
            return g_list[0:len(g_list)-1]
    except Exception:
        print("\nGOOGLE RIGHT BOX SCRAPPING UNAVAILABLE!!!\n")


def full_page(url):
    # SCRAPPING OF THE FULL PAGE BY HEADER AND BOLD TAGS WITH CUSTOM URL.
    try:
        full_list = []
        headers = head_gen()
        html = requests.get(url, headers=headers)
        # reg1 = re.compile(r"[a-zA-Z]", re.M)
        reg2 = re.compile(r"[0-9]\s|ISBN|[0-9]-|[+]", re.M)
        if html.status_code == 200:
            bs = BeautifulSoup(html.text, 'html.parser')
            for fl in bs.find_all(["h2", "b"]):
                tx = fl.get_text()
                if reg2.search(tx):
                    pass
                else:
                    full_list.append(tx)
            full_list = list(set(full_list))
            return full_list
    except Exception:
        print("\nFULL PAGE CUSTOM SCRAPPING UNAVAILABLE!!!\n")


if __name__ == "__main__":
    search_term = "porsche cayenne"
    # url = "https://en.wikipedia.org/wiki/%s" % str(
    #     search_term.replace(' ', '_'))
    # print("\n\nWIKIPEDIA LISTS AND LINKS:\n\n", wiki_lists(search_term))
    print("\n\nWIKIPEDIA SUMMARY:\n\n", wiki_summary(search_term))
    print("\n\nWIKIPEDIA SUGGEST:\n\n", wiki_suggest(search_term))
    print("\n\nWIKIPEDIA FIRST SECTION:\n\n", wiki_section(search_term))
    # print("\n\nWIKIPEDIA SECTIONS:\n\n", wiki_sections(search_term))
    # print("\n\nGOOGLE LISTS AND LINKS:\n\n", google_lists(search_term))
    # print("\n\nGOOGLE URLS:\n\n", google_urls(search_term))
    # print("\n\nGOOGLE RESULTS NUMBER:\n\n", google_result(search_term))
    # print("\n\nGOOGLE RIGHT BOX:\n\n", google_rbox(search_term))
    # print("\n\nPAGE WITH CUSTOM URL:\n\n", full_page(url))