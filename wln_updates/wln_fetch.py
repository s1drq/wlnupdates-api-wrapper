from wln_updates import wln_client

class Series:
    def __init__(self):
        self.data = {"mode": "get-series-id"}
        self.fetch = wln_client.Wrapper.Fetch()

    def __call__(self, _id):
        self.data['id'] = _id
        return self.fetch.POST(_data=self.data)['data']

    def alternatenames(self, _id):
        return self.__call__(_id)['alternatenames']

    def authors(self, _id):
        return self.__call__(_id)['authors']

    def covers(self, _id):
        return self.__call__(_id)['covers']

    def demographic(self, _id):
        return self.__call__(_id)['demographic']

    def description(self, _id):
        return self.__call__(_id)['description'].replace("<p>", "").replace("</P>", "")

    def genres(self, _id):
        return self.__call__(_id)['genres']

    def id(self, _id):
        return self.__call__(_id)['id']

    def illustrators(self, _id):
        return self.__call__(_id)['illustrators']

    def latest(self, _id):
        return self.__call__(_id)['latest']

    def latest_chapter(self, _id):
        return self.__call__(_id)['latest_chapter']

    def latest_fragment(self, _id):
        return self.__call__(_id)['latest_fragment']

    def latest_published(self, _id):
        return self.__call__(_id)['latest_published']

    def latest_str(self, _id):
        return self.__call__(_id)['latest_str']

    def latest_volume(self, _id):
        return self.__call__(_id)['latest_volume']

    def license_en(self, _id):
        return self.__call__(_id)['license_en']

    def most_recent(self, _id):
        return self.__call__(_id)['most_recent']

    def orig_lang(self, _id):
        return self.__call__(_id)['orig_lang']

    def orig_status(self, _id):
        return self.__call__(_id)['orig_status']

    def origin_loc(self, _id):
        return self.__call__(_id)['origin_loc']

    def progress(self, _id):
        return self.__call__(_id)['progress']

    def pub_date(self, _id):
        return self.__call__(_id)['pub_date']

    def publishers(self, _id):
        return self.__call__(_id)['publishers']

    def rating(self, _id):
        return self.__call__(_id)['rating']

    def rating_count(self, _id):
        return self.__call__(_id)['rating_count']

    def region(self, _id):
        return self.__call__(_id)['region']

    def releases(self, _id):
        return self.__call__(_id)['releases']

    def similar_series(self, _id):
        return self.__call__(_id)['similar_series']

    def tags(self, _id):
        return self.__call__(_id)['tags']

    def title(self, _id):
        return self.__call__(_id)['title']

    def tl_type(self, _id):
        return self.__call__(_id)['tl_type']

    def total_watches(self, _id):
        return self.__call__(_id)['total_watches']

    def type(self, _id):
        return self.__call__(_id)['type']

    def watch(self, _id):
        return self.__call__(_id)['watch']

    def watchlists(self, _id):
        return self.__call__(_id)['watchlists']

    def website(self, _id):
        return self.__call__(_id)['website']

class Publisher:
    def __init__(self):
        self.data = {"mode": "get-publisher-id"}
        self.fetch = wln_client.Wrapper.Fetch()

    def __call__(self, _id):
        self.data['id'] = _id
        return self.fetch.POST(_data=self.data)['data']

    def name(self, _id):
        return self.__call__(_id)['name']

    def series(self, _id):
        return self.__call__(_id)['series']

    def site(self, _id):
        return self.__call__(_id)['site']

class Group:
    def __init__(self):
        self.data = {"mode": "get-group-id"}
        self.fetch = wln_client.Wrapper.Fetch()

    def __call__(self, _id):
        self.data['id'] = _id
        return self.fetch.POST(_data=self.data)['data']

    def active_series(self, id):
        return self.__call__(id)['active-series']

    def alternate_names(self, id):
        return self.__call__(id)['alternate-names']

    def feed_paginated(self, id):
        return self.__call__(id)['feed-paginated']

    def group(self, id):
        return self.__call__(id)['group']

    def id(self, id):
        return self.__call__(id)['id']

    def releases_paginated(self, id):
        return self.__call__(id)['releases-paginated']

    def site(self, id):
        return self.__call__(id)['site']

class Artist:
    def __init__(self):
        self.data = {"mode": "get-artist-id"}
        self.fetch = wln_client.Wrapper.Fetch()

    def __call__(self, _id):
        self.data['id'] = _id
        return self.fetch.POST(_data=self.data)['data']

    def name(self, _id):
        return self.__call__(_id)['name']

    def series(self, _id):
        return self.__call__(_id)['series']

class Author:
    def __init__(self):
        self.data = {"mode": "get-author-id"}
        self.fetch = wln_client.Wrapper.Fetch()

    def __call__(self, _id):
        self.data['id'] = _id
        return self.fetch.POST(_data=self.data)['data']
    def name(self, _id):
        return self.__call__(_id)['name']

    def series(self, _id):
        return self.__call__(_id)['series']

class Genre:
    def __init__(self):
        self.data = {"mode": "get-genre-id"}
        self.fetch = wln_client.Wrapper.Fetch()

    def __call__(self, _id):
        self.data['id'] = _id
        return self.fetch.POST(_data=self.data)['data']

    def genre(self, _id):
        return self.__call__(_id)['genre']

    def series(self, _id):
        return self.__call__(_id)['series']