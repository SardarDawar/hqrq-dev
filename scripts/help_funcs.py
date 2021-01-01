from .app_lists import stops


def good_query(search_term):
    sterm_list = search_term.split()
    n = 0
    for stm in sterm_list:
        if stm in stops:
            n += 1
        else:
            query = " ".join(search_term.split()[n:])
            break
    return query


def user_query(search_term):
    sterm_list = search_term.split()
    if sterm_list[0].lower() in stops:
        u_article, query = sterm_list[0], " ".join(sterm_list[1:])
    else:
        u_article, query = None, search_term
    return (u_article, query)