from wlnupdates_wrapper import *
import requests
import json

id = 12

print("series id: ", id, " output: ", wln_get().series_data(id))

print("publisher id: ", id, " output: ",wln_get().publisher_data(id))

print("group id: ", id, " output: ",wln_get().group_data(id))

print("artistid: ", id, " output: ",wln_get().artist_data(id))

print("author id: ", id, " output: ",wln_get().author_data(id))

print("genre id: ", id, " output: ",wln_get().genre_data(id))

print("all tags", " output: ",wln_utils().enumerate_tags())

print("all genres", " output: ",wln_utils().enumerate_genres())

# If not passed any other arguments other than the title-search-string, method/function will return the highest match if any
a = wln_search().title_search("Hamachi")
print("title search (no args) output: ", a)
print("title search (no args) length: ", len(a))

# If _listAll is set to True, method/function will return all matches
b = wln_search().title_search("Hamachi", _listAll=True)
print("title search (_listAll=True) output: ", b)
print("title search (_listAll=True) length: ", len(b))

# If _matchmin is set to a value(n), method/function will return all matches with "match" rating higher than n
c = wln_search().title_search("Hamachi", _listAll=True, _matchmin=0.5)
print("title search (_listAll=True, _matchmin=0.5) output: ", c)
print("title search (_listAll=True, _matchmin=0.5) length: ", len(c))

x = wln_search().advance_search(_genre_category={"comedy" : "include"})['data']

y = wln_utils().sort_tl_type(x, "translated")

z = wln_utils().sort_tl_type(x, "oel")

print("raw length: ", len(x))

print("tl length: ", len(y))

print("oel length: ", len(z))

