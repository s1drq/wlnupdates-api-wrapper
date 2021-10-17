from wln_updates.wln_fetch import Series
from wln_updates.wln_fetch  import Publisher
from wln_updates.wln_fetch  import Group
from wln_updates.wln_fetch  import Artist
from wln_updates.wln_fetch  import Author
from wln_updates.wln_fetch  import Genre
from wln_updates.wln_search import Search
import requests
import json


class Wrapper:
    def __init__(self):
        self.series = Series()
        self.publisher = Publisher()
        self.group = Group()
        self.artist = Artist()
        self.author = Author()
        self.genre = Genre()
        self.search = Search()
        self.online = Online()
        self.utils = Utils()


    class Fetch:
        def __init__(self):
            self.headers = {'Content-Type': 'application/json'}
            self.url = "https://www.wlnupdates.com/api"

        def request(self, _method, _data=None, _params=None):
            response = requests.request(_method, self.url, headers=self.headers, data=_data, params=_params)

            try:
                json_data  = response.json()
            except Exeption as e:
                print("Error:", e)

            if json_data['error'] is True:
                return f"jsonERROR: {json_data['message']}"
            else:
                return json_data

        def POST(self, _data):
            return self.request("POST", _data=json.dumps(_data))

        def GET(self, _data):
            return self.request("GET", _data=json.dumps(_data))

class Utils:
    def enumerate_tags(self):
        return Wrapper.Fetch().POST(_data={'mode': 'enumerate-tags'})

    def enumerate_genres(self):
        return Wrapper.Fetch().POST(_data={'mode': 'enumerate-genres'})


class Online:
    def login(self,
              _username=None,
              _password=None,
              _rememberme=True):

        self.data = {"mode": 'do-login',
                     "username": _username,
                     'password': _password,
                     'remember me': _rememberme}

        check = [
            _username is None,
            _password is None,
            _rememberme == False]

        if all(check):
            raise Exception("Parameters for Login are invalid")

        else:
            return Wrapper.Fetch().POST(_data=self.data)

    def watches_data(self, _filter='all'):
        return Wrapper.Fetch().POST(_data={
            "mode": 'get-watches', "active-filter": _filter
        })

class wln_Error:
    class error(Exception):

        def __init__(self, message="wrong inputs"):
            super().__init__(message)

        def __str__(self):
            return self.message

    #   When wlnupdates finally implements a GET method, def GET() will be here for you.
    #   Always watching. Always waiting. Reeeeeeeeee.









