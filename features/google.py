# from pywikihow import search_wikihow
import pywhatkit

def how_to(query):
    try:
        max_results = 1  # one result from web
        x = pywhatkit.search_wikihow(query, max_results)
        assert len(how_to) == 1
        how_to[0].print()           # first result
        val = x[0].summary  # summary of 1st result

    except Exception as e:
        val = "Sorry sir, I am not able to find this"

    return val

#google search
def googlesearch(query):
    pywhatkit.search(query)  # perform search

# searches nearby
def nearby(query):
    #remove unimportant words from query
    if "show me" in query:
        query = query.replace("show me", "")
    temp = query
    if "me" in query:
        temp = query.replace("me", " you")

    # speak("Showing " + temp)
    googlesearch(query)  # search google for nearby
    return "Showing " + temp  # return string to print in chatbox
