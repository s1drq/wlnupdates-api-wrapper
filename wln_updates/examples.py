'''
WLNUPDATES API WRAPPER
                                                  by: s1drq

A/NOTE:     I am not a programmer so this might not be the most efficient api wrapper.
            I said it was simple.... I didn't say that it was any good.

Issues:

    (1) watches_data() does not work for some reason. Please give me a heads up if you know why or can get it
        to work. Thanks!

    (2) My naming convention
            >   I add "_" for arguments passed to the function/method.
            >   It's weird I know and kinda comfusing for some.
            >   No. I won't be changing it anytime soon.

The last line is meant to give an error when the value entered is not "oel" or "translated"

CONSOLE MESSAGE:
    Traceback (most recent call last):
    File "<file-path>\wln_updates\examples.py", line 104, in <module>
        print("Search - advanced_search (magi) : ", wrp.search.advance_search('magi', _series_type="dfdfdf"))
    File "<file-path>\wln_updates\wln_search.py", line 79, in advance_search
        raise Exception("InputError: _series_type parameter only accepts 'translated' or 'oel.'")
    Exception: InputError: _series_type parameter only accepts 'translated' or 'oel.'

'''

from wln_updates.wln_client import Wrapper
import time

start = time.time()

wrp = Wrapper()

print("SERIES DATA:")
print("fetching series-raw : ", wrp.series(3))
print("fetching alternatenames : ", wrp.series.alternatenames(3))
print("fetching authors : ", wrp.series.authors(3))
print("fetching covers : ", wrp.series.covers(3))
print("fetching demographic : ", wrp.series.demographic(3))
print("fetching description : ", wrp.series.description(3))
print("fetching genres : ", wrp.series.genres(3))
print("fetching id : ", wrp.series.id(3))
print("fetching illustrators : ", wrp.series.illustrators(3))
print("fetching latest : ", wrp.series.latest(3))
print("fetching latest_chapter : ", wrp.series.latest_chapter(3))
print("fetching latest_fragment : ", wrp.series.latest_fragment(3))
print("fetching latest_published : ", wrp.series.latest_published(3))
print("fetching latest_str : ", wrp.series.latest_str(3))
print("fetching latest_volume : ", wrp.series.latest_volume(3))
print("fetching license_en : ", wrp.series.license_en(3))
print("fetching most_recent : ", wrp.series.most_recent(3))
print("fetching orig_lang : ", wrp.series.orig_lang(3))
print("fetching orig_status : ", wrp.series.orig_status(3))
print("fetching origin_loc : ", wrp.series.origin_loc(3))
print("fetching progress : ", wrp.series.progress(3))
print("fetching pub_date : ", wrp.series.pub_date(3))
print("fetching publishers : ", wrp.series.publishers(3))
print("fetching rating : ", wrp.series.rating(3))
print("fetching rating_count : ", wrp.series.rating_count(3))
print("fetching region : ", wrp.series.region(3))
print("fetching releases : ", wrp.series.releases(3))
print("fetching similar_series : ", wrp.series.similar_series(3))
print("fetching tags : ", wrp.series.tags(3))
print("fetching title : ", wrp.series.title(3))
print("fetching tl_type : ", wrp.series.tl_type(3))
print("fetching total_watches : ", wrp.series.total_watches(3))
print("fetching type : ", wrp.series.type(3))
print("fetching watch : ", wrp.series.watch(3))
print("fetching watchlists : ", wrp.series.watchlists(3))
print("fetching website : ", wrp.series.website(3))

print(" ")

print("PUBLISHER: ")
print("fetching publisher-raw: ", wrp.publisher(3))
print("fetching name : ", wrp.publisher.name(3))
print("fetching series : ", wrp.publisher.series(3))
print("fetching site : ", wrp.publisher.site(3))

print(" ")

print("GROUP:")
print("fetching group-raw ", wrp.group(3))
print("fetching active-series : ", wrp.group.active_series(3))
print("fetching alternate-names : ", wrp.group.alternate_names(3))
print("fetching feed-paginated : ", wrp.group.feed_paginated(3))
print("fetching group : ", wrp.group.group(3))
print("fetching id : ", wrp.group.id(3))
print("fetching releases-paginated : ", wrp.group.releases_paginated(3))
print("fetching site : ", wrp.group.site(3))

print(" ")

print("ARTIST:")
print("fetching artist-raw : ", wrp.artist(3))
print("fetching series : ", wrp.artist.series(3))

print(" ")

print("GENRE:")
print("fetching genre-raw : ", wrp.genre(3))
print("fetching genre : ", wrp.genre.genre(3))
print("fetching series : ", wrp.genre.series(3))

print(" ")

print("ONLINE FUNCTIONS:")
print("Logging in : ", wrp.online.login(_username="user", _password="pass"))
print("Getting watches data : ", wrp.online.watches_data())

print(" ")

print("LIST OF ALL TAGS AND GENRES")
print("Listing all tags : ", wrp.utils.enumerate_tags())
print("Listing all genres : ", wrp.utils.enumerate_genres())

print(" ")

print("TITLE SEARCH")
print("Search - title_search (magi) : ", wrp.search.title_search('magi'))
print("Search - title_search (magi) : ", wrp.search.title_search('magi', _matchmin=0.5))
print("Search - title_search (magi) : ", wrp.search.title_search('magi', _listAll=False))

print(" ")

print("ADVANCED SEARCH")
print("Search - advanced_search (magi) : ", wrp.search.advance_search('magi'))
print("Search - advanced_search (magi) : ", wrp.search.advance_search('magi', _genre_category={"romance" : "include"}))
print("Search - advanced_search (magi) : ", wrp.search.advance_search('magi', _genre_category={"romance" : "include"}, _include_results=['description']))
print("Search - advanced_search (magi) : ", wrp.search.advance_search('magi', _series_type="translated"))
print("Search - advanced_search (magi) : ", wrp.search.advance_search('magi', _series_type="oel"))
print("Search - advanced_search (magi) : ", wrp.search.advance_search('magi', _series_type="dfdfdf"))

finish = time.time()

print( "Diagnostics finished after {} seconds".format(round(finish-start), 2))

