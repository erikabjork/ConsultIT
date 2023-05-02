import streamlit as st

import requests
import json

url = 'https://historical.api.jobtechdev.se'
url_for_search = f"{url}/search"


def _get_ads(params):
    headers = {'accept': 'application/json'}
    response = requests.get(url_for_search, headers=headers, params=params)
    response.raise_for_status()  # check for http errors
    return json.loads(response.content.decode('utf8'))


def example_search_return_number_of_hits(query):
    # limit: 0 means no ads, just a value of how many ads were found.
    search_params = {'q': query, 'limit': 100}
    json_response = _get_ads(search_params)
    number_of_hits = json_response['total']['value']
    print(f"\nNumber of hits = {number_of_hits}")
    st.write(number_of_hits)



def example_search_loop_through_hits(querystr):
    # limit = 100 is the max number of hits that can be returned.
    # If there are more (which you find with ['total']['value'] in the json response)
    # you have to use offset and multiple requests to get all ads.
    search_params = {'q': querystr, 'limit': 100}
    json_response = _get_ads(search_params)
    hits = json_response['hits']
    #print(hits)
    word = "2017"
    for hit in hits:
            headline = hit['headline']
            pub = hit['publication_date']
            if word in pub:
            #print(f"{hit['headline']}")
                print(headline)
        #st.write(f"{['headline']}, {['year']['name']}")
                st.write(f"{hit['publication_date']}, {hit['headline']}")
        #st.write(f"{hit['headline']}")


if __name__ == '__main__':
    query = st.text_input("Skriv något här: ")
    querystr = str(query)
    example_search_loop_through_hits(querystr)
    example_search_return_number_of_hits(querystr)
