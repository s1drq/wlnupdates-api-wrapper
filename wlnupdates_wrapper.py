'''
SUPER SIMPLE WLNUPDATES API WRAPPER
by: s1drq

NOTE:   I am not a programmer so this might not be the most efficient api wrapper.
        I said it was simple.... I didn't say that it was any good.

Issues:
    (1) series-type parameter does not work on my end.
            >   I will update the package as soon as I get it fixed or a work around has been found but
                for now, this parameter returns nothing.

            >   Added wln_utils().sort_tl_type() as a work around for series-type bug
                    Example usage:
                        x = wln_search().advance_search(_genre_category={"comedy" : "include"})['data']
                        y = wln_utils().sort_tl_type(x, "translated")
                        z = wln_utils().sort_tl_type(x, "oel")

                        print("raw length: ", len(x))
                        print("tl length: ", len(y))
                        print("oel length: ", len(z))

                    CONSOLE RESULT:
                            raw length:  100
                            tl length:  89
                            oel length:  11

    (2) online().watches_data() does not work for some reason. Please give me a heads up if you know.

    (3) Naming convention
            >   I add "_" for arguments a function/method will accept.
            >   It's weird I know and kinda comfusing for some.
            >   No. I won't be changing it anytime soom.
'''

import requests
import json


class wln_utils:
    def sort_tl_type(self, _json, _key):
        fList = []
        for x in range(len(_json)):
            if _key == "translated":
                if _json[x]['tl_type'] == 'translated':
                    fList.append(_json[x])

            elif _key == "oel":
                if _json[x]['tl_type'] == 'oel':
                    fList.append(_json[x])

            else:
                print("ERROR: Invalid parameters")
        return fList

class fetch_data:
    def __init__(self):
        self.headers = {'Content-Type': 'application/json'}
        self.url = "https://www.wlnupdates.com/api"

    def POSTjson(self, _params):
        response = requests.request("POST",self.url, headers=self.headers, data=json.dumps(_params))

        try:        json_data  = response.json()
        except:     return "the raw data does not exist"

        if json_data['error'] is True:
            return f"ERROR: {json_data['message']}"

        else:
            return json_data

class online:
    def login(self, _username, _password, _rememberme='False'):
        return fetch_data().POSTjson({
            "mode": 'do-login', "username": _username, 'password': _password, 'remember me' : _rememberme
        })

    def watches_data(self, _filter='all'):
        return fetch_data().POSTjson({
            "mode": 'get-watches', "active-filter": _filter
        })

class wln_get:
    def series_data(self, _id):
        return (fetch_data().POSTjson({"id" : _id, "mode" : "get-series-id"}))['data']

    def publisher_data(self, _id):
        return (fetch_data().POSTjson({"id" : _id, "mode" : "get-publisher-id"}))['data']

    def group_data(self, _id):
        return (fetch_data().POSTjson({"id" : _id, "mode" : "get-group-id"}))['data']

    def artist_data(self, _id):
        return (fetch_data().POSTjson({"id" : _id, "mode" : "get-artist-id"}))['data']

    def author_data(self, _id):
        return (fetch_data().POSTjson({"id" : _id, "mode" : "get-author-id"}))['data']

    def genre_data(self, _id):
        return (fetch_data().POSTjson({"id" : _id, "mode" : "get-genre-id"}))['data']

    def enumerate_tags(self,):
        return fetch_data().POSTjson({'mode': 'enumerate-tags'})['data']

    def enumerate_genres(self, ):
        return fetch_data().POSTjson({'mode': 'enumerate-genres'})['data']

class wln_search:
    def title_search(self, _name, _matchmin=0, _listAll=False):

        json_data = fetch_data().POSTjson({"title": _name, "mode": "search-title"})['data']['results']

        if _listAll is True:
            matchList = []
            for results in json_data:
                if results['match'][0][0] >= _matchmin: matchList.append(results)
            return matchList
        else:
            return json_data[0]

    def advance_search(self,
                       _name=None,
                       _tag_category=None,
                       _include_results=None,
                       _genre_category=None,
                       _chapter_limits=None,
                       _series_type=None,
                       _sort_mode=None):

        params = {"mode": "search-advanced"}

        try:
            if _name:
                params['title-search-text']     = _name

            if _chapter_limits:
                params['chapter-limits']        = _chapter_limits

            if _sort_mode:
                params['sort-mode']             = _sort_mode

            if _include_results:
                params['include-results']             = _include_results

            if _series_type:
                pass    #   Not working. Please see Notes at the top part of the package.
                # params['series-type'] = _series_type

            if _tag_category:
                params['tag-category'] = _tag_category

            if _genre_category:
                params['genre-category'] = _genre_category

        except Exception as e:
            print(e)

        print(params)
        return fetch_data().POSTjson(params)


