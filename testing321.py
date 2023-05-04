import streamlit as st
import requests
import json

url = 'https://jobsearch.api.jobtechdev.se'
url_for_search = f"{url}/search"

url2 = 'https://dev-historical-api.jobtechdev.se'
url_for_search2 = f"{url2}/search"


def _get_ads(params):
    headers = {'accept': 'application/json'}
    response = requests.get(url_for_search, headers=headers, params=params)
    response.raise_for_status()  # check for http errors
    return json.loads(response.content.decode('utf8'))

def _get_ads2(params2):
    headers = {'accept': 'application/json'}
    response = requests.get(url_for_search2, headers=headers, params=params2)
    response.raise_for_status()  # check for http errors
    return json.loads(response.content.decode('utf8'))

def example_search_return_number_of_hits(query):
    # limit: 0 means no ads, just a value of how many ads were found.
    search_params = {'q': query}
    json_response = _get_ads(search_params)
    number_of_hits = json_response['total']['value']
    #print(f"\nNumber of hits = {number_of_hits}")
    #st.write("CURRENT")
    #st.write(number_of_hits)
    return number_of_hits

def example_search_return_number_of_hits2(query):
    # limit: 0 means no ads, just a value of how many ads were found.
    search_params2 = {'q': query}
    json_response = _get_ads2(search_params2)
    number_of_hits2 = json_response['total']['value']
    #print(f"\nNumber of hits = {number_of_hits}")
    #st.write("HISTORICAL")
    #st.write(number_of_hits)
    return number_of_hits2

#def example_search_loop_through_hits(querystr):
    # limit = 100 is the max number of hits that can be returned.
    # If there are more (which you find with ['total']['value'] in the json response)
    # you have to use offset and multiple requests to get all ads.
    search_params = {'q': querystr}
    json_response = _get_ads(search_params)
    hits = json_response['hits']
    ord = "säljare"
    lagra = []
    for hit in hits:
            headline = hit['headline']
            if ord in headline:
                lagra.append(headline)
                st.write(lagra)
    print(lagra)


        #st.write(f"{hit['publication_date']}, {hit['headline']}")
        #print(f"{hit['headline']}, {hit['employer']['name']}")

#def example_search_loop_through_hits2(query):
    # limit = 100 is the max number of hits that can be returned.
    # If there are more (which you find with ['total']['value'] in the json response)
    # you have to use offset and multiple requests to get all ads.
    search_params = {'q': query, 'limit': 100}
    json_response = _get_ads2(search_params)
    hits = json_response['hits']
    #for hit in hits:



if __name__ == '__main__':
    query = st.text_input("Sök på en kompetens: ")
    querystr = str(query)
    #example_search_loop_through_hits(query)
    #example_search_loop_through_hits2(query)
    #example_search_return_number_of_hits(query)
    #example_search_return_number_of_hits2(query)
    number_of_hits = example_search_return_number_of_hits(query)
    number_of_hits2 = example_search_return_number_of_hits2(query)
    st.title("Du har sökt på: " + query)
    st.write("CURRENT")
    st.write(number_of_hits)
    st.write("_____________________")
    st.write("HISTORICAL")
    st.write(number_of_hits2)
