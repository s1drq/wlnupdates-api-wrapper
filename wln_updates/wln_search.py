from wln_updates import wln_client
class Search:
    def __init__(self):
        self.fetch = wln_client.Wrapper.Fetch()

    def title_search(self,
                     _name,
                     _matchmin=0,
                     _listAll=True):

        self.data = {"mode": "search-title"}
        self.data['title'] = _name


        json_data = self.fetch.POST(_data=self.data)['data']['results']

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
                       _sort_mode=None,
                       _extra_metadata=True):

        params = {"mode": "search-advanced"}

        if _name:
            params['title-search-text'] = _name

        if _chapter_limits:
            params['chapter-limits'] = _chapter_limits

        if _sort_mode:
            params['sort-mode'] = _sort_mode

        if _include_results:
            params['include-results'] = _include_results

        if _tag_category:
            params['tag-category'] = _tag_category

        if _genre_category:
            params['genre-category'] = _genre_category

        else:
            pass

        json_data = self.fetch.POST(_data=params)['data']


        json_parsed = []

        #   _series_type parameter does give accurate results.
        #   This is just a work around till it get fixed.

        for i in range(len(json_data)):
            if _series_type == "translated":
                if json_data[i]['tl_type'] == "translated":
                    json_parsed.append(json_data[i])

            elif _series_type == "oel":
                if json_data[i]['tl_type'] == "oel":
                    json_parsed.append(json_data[i])

            elif _series_type != "oel" and _series_type != "translated" and _series_type != None:
                raise Exception("InputError: _series_type parameter only accepts 'translated' or 'oel.'")
                return json_data

            else:
                json_parsed.append(json_data[i])

        return json_parsed
