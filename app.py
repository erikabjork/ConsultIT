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




#if __name__ == '__main__':

    #query = st.text_input("Skriv något här: ")
      
    #querystr = str(query)

    
    #example_search_loop_through_hits(querystr)
    #example_search_return_number_of_hits(querystr)


import streamlit as st
from streamlit_option_menu import option_menu


with st.sidebar:
    choose = option_menu("ConsultIT", ["Beskrivning", "Om ConsultIT", "Om datasetet", "Kontakt"],
                         icons=['book', 'app-indicator', 'gear', 'telephone'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#0090EA"},
        
    
    }
    )
    if choose == 'Beskrivning':
        st.write('Applikationen visar vad som kortsiktigt efterfrågas på arbetsmarknaden och utifrån det är tanken att kunna anpassa valbara kurser på det systemvetenskapliga programmet.')
    elif choose == 'Om ConsultIT':
        st.write('Vi är ett konsultföretag som hjälper blablablabla')
    elif choose== 'Om datasetet':
        st.write ('Detta dataset är hämtat från JobTech och visar historiska jobbannonser blablablabla.')
    elif choose == 'Kontakt':
        st.write('Kontakta oss på consultIT@outlook.com')

# Create a beta container for the search box
search_container = st.container()

# Add a search box to the container
search_query = search_container.text_input('Search', value='', key='search')

# Add some CSS styling to position the search box in the top right corner
search_container.markdown("""
    <style>
        .st-bq {
            position: none;
            top: 300;
            right: 500;
            margin: 10px;
            z-index: 999;
            border: #0090EA;
            border: 2px solid black;
            border-radius: 10px;
            padding: 5px;
            transition: border-color 0.3s ease-in-out;

        }
          .st-bq:hover {
            border-color: #0090EA;
        }
        
        .st-bq:active {
            border-color:#0090EA;
        }
    </style>
""", unsafe_allow_html=True)

search_container_styles_active = '''
    border-color: 2px solid #0090EA;
    '''
search_container_styles_hover = '''
    border-color: 2px solid #0090EA;
    '''
st.write("<style>div.row-widget.stsearch_container > search_container:first-child:active { %s }</style>" % search_container_styles_active, unsafe_allow_html=True)
st.write("<style>div.row-widget.stsearch_container > search_container:first-child:hover { %s }</style>" % search_container_styles_hover, unsafe_allow_html=True)


import streamlit as st

#from streamlit_image_coordinates import streamlit_image_coordinates

#value = streamlit_image_coordinates("")


#st.write(value)


  
import streamlit as st



# Increase the size of the button using custom CSS styles
button_styles = f'''
    height: 100px;
    width: 200px;
    font-size: 20px;
    color:black;
    border: 2px solid black;
    transition: border-color 0.3s ease-in-out;
       


    '''
button_clicked_styles = f'''
    height: 100px;
    width: 200px;
    font-size: 20px;
    color:white;
    background-color: white;
    border: #0090EA;
'''

button_styles_hover = '''
    border: 2px solid #0090EA;
    '''
button_styles_active = '''
    background-color: white;
    '''

st.write("<style>div.row-widget.stButton > button:first-child:hover { %s }</style>" % button_styles_hover, unsafe_allow_html=True)
st.write("<style>div.row-widget.stButton > button:first-child:active{ %s }</style>" % button_styles_active, unsafe_allow_html=True)
st.write("<style>div.row-widget.stButton > button:first-child { %s }</style>" % button_styles, unsafe_allow_html=True)

def page1():
    
    st.title(" ")
    st.write("Presenterad data:")
   # query = st.text_input("Skriv något här: ")
      
    #querystr = str(query)

    
    #example_search_loop_through_hits(querystr)
    #example_search_return_number_of_hits(querystr)
    col1,col2,col3 = st.columns(3)
    with col1:
        st.button("Data1")
        

    with col2:
        st.button("Data2")
        

    with col3:
        st.button("Data 3")
        
    
  
    st.markdown(
    """
    <div style='border-bottom:2px solid #ccc'>
        <h1 style='text-align:left; padding:10px; font-size: 20px; '>Emergent technologies</h1>
    </div>
    """,
    unsafe_allow_html=True
)

    if st.button("se trend"):
        st.session_state.current_page = "page2"
        st.session_state.current_file = "page2.py"
      

    

import numpy as np
import altair as alt


   

   

def page2():
    
    st.title("LineChart")
    if st.button("Back"):
        st.session_state.current_page = "page1"
        st.session_state.current_file = "app.py"
        import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt





        

if "current_page" not in st.session_state:
    st.session_state.current_page = "page1"
    

if st.session_state.current_page == "page1":
    page1()
elif st.session_state.current_page == "page2":
    page2()