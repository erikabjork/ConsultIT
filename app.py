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
      
   # querystr = str(query)

    
    #example_search_loop_through_hits(querystr)
   # example_search_return_number_of_hits(querystr)


import streamlit as st
from streamlit_option_menu import option_menu


def main():
    # Add the logo image
       # Add the logo
    logo_path = "https://www.akademiskahogtider.se/digitalAssets/818/c_818170-l_3-k_lo_gu_cen2r294c.png"
    #logo = st.image(logo_path, use_column_width=False)
    logo = f'<img src="{logo_path}" style="position: none; top: 10px; left: 10px; width: 100px; margin-left:32%; margin-top:-30%;">'
    st.sidebar.markdown(logo, unsafe_allow_html=True)

    # Rest of your code...
    with st.sidebar:
        choose = option_menu(" ‎ ‎ ‎Systemvetenskap", ["Beskrivning", "Om ConsultIT", "Om datasetet", "Kontakt"],
                             icons=['book', 'app-indicator', 'gear', 'telephone'],
                             menu_icon="none", default_index=0,
                             styles={
                                 "container": {"padding": "5!important", "background-color": "#fafafa"},
                                 "icon": {"color": "black", "font-size": "20px"},
                                 "nav-link": {"font-size": "13px", "text-align": "left", "margin": "0px",
                                              "--hover-color": "#eee"},
                                 "nav-link-selected": {"background-color": "#0090EA"},
                             })

        if choose == 'Beskrivning':
            st.markdown("<hr>", unsafe_allow_html=True)
            st.write('Applikationen visar vad som kortsiktigt efterfrågas på arbetsmarknaden och utifrån det är tanken att kunna anpassa valbara kurser på det systemvetenskapliga programmet.')
            st.markdown("<hr>", unsafe_allow_html=True)
        elif choose == 'Om ConsultIT':
            st.markdown("<hr>", unsafe_allow_html=True)
            st.write('Vi är ett konsultföretag som hjälper blablablabla')
            st.markdown("<hr>", unsafe_allow_html=True)
        elif choose == 'Om datasetet':
            st.markdown("<hr>", unsafe_allow_html=True)
            st.write('Detta dataset är hämtat från JobTech och visar historiska jobbannonser blablablabla.')
            st.markdown("<hr>", unsafe_allow_html=True)
        elif choose == 'Kontakt':
            st.markdown("<hr>", unsafe_allow_html=True)
            st.write('Kontakta oss på consultIT@outlook.com')
            st.markdown("<hr>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()








    
# Create a beta container for the search box
search_container = st.container()

# Add a search box to the container
search_query = search_container.text_input('Search', value='', key='search' )



# Add some CSS styling to position the search box in the top right corner
search_container.markdown("""
    <style>
        .st-bq {
            position: absolute;
            top: 500;
            right: 10px;
            margin: 10px;
            z-index: 999;
            border: #0090EA;
            border: 2px solid black;
            border-radius: 10px;
             max-width: 300px;
            width: 100%;
            padding: 0.25rem;
            font-size: 14px;
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

import subprocess

import pandas as pd

def main():
    current_page = st.session_state.get("current_page", "page1")

    if current_page == "page1":
        page1()
    elif current_page == "page2":
        page2()
        
def page1():    
   # query = st.text_input("Skriv något här: ")
    clicked = True
    #querystr = str(query)
    #example_search_loop_through_hits(querystr)
    #example_search_return_number_of_hits(querystr)
    col1,col2,col3 = st.columns(3)
    with col1:
        if st.button('Artificial intelligence'):
          
            page2()
            col1.empty()
            st.stop()
            
            

    with col2:
        if st.button("Machine learning"):
            page2()
            col2.empty()
            st.stop()

        

    with col3:
        if st.button('Deep learning'):
            page2()
            col3.empty()
            st.stop()
        
  
  



    
      
    st.markdown(
    """
    <style>
    .custom-button {
        background-color: #0090EA;
        color: white;
        border: none;
        border-radius: 3px;
        font-size: 13px;
        text-align: center;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)
    st.markdown(
    """
    <style>
    .small-header {
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
#import requests
#competencies = ['Artificial intelligence', 'Machine learning', 'Deep learning', 'Natural language processing', 'Computer vision', 'Robotics', 'Internet of Things', 'Blockchain technology', 'Augmented reality', 'Virtual reality', 'Quantum computing', 'Big data analytics', 'Cloud computing', 'Edge computing', 'Cybersecurity technologies', 'Predictive analytics', 'Autonomous vehicles', 'Genetic engineering', '3D printing/additive manufacturing', 'Advanced materials science', 'Renewable energy technologies', 'Smart grids', 'Biometrics', 'Wearable technologies', 'Nanotechnology', 'Cognitive computing', 'Swarm intelligence', 'Synthetic biology', 'Human-computer interaction', 'Data visualization, ’Analytics tools']
#for compenetcy in competencies:
    #st.write(compenetcy)



    col7, col8, col9 = st.columns(3)
  



    with col7:
        
        st.markdown("<h2 class='small-header'>Emergent Technologies</h2>", unsafe_allow_html=True)
        st.text('Natural language processing')
        st.text('Computer vision')
        st.text('Robotics')
        st.text("Internet of Things")
        st.text('Blockchain technology')
        st.text('Augmented reality')
        st.text('Virtual reality')
        st.text('Quantum computing')
        st.text('Big data analytics')
        st.text('Cloud computing')
        st.text('Edge computing')
        st.text('Cybersecurity technologies')
        st.text('Autonomous vehicles')
        st.text('Genetic engineering')
        st.text('3D printing/additive manufacturing')
        st.text('Advanced materials science')
        st.text('Renewable energy technologies')
        st.text('Smart grids')
        st.text('Biometrics')
        st.text('Wearable technologies')
        st.text('Nanotechnology')
        st.text('Cognitive computing')
        st.text('Swarm intelligence')
        st.text('Synthetic biology')
        st.text('Human-computer interaction')
        st.text('Data visualization')
        st.text('Analytics tools')

        


               
        
        



    with col8:
        st.markdown("<h2 class='small-header'>Aktiva annonser</h2>", unsafe_allow_html=True)
        st.text("800")
        st.text("641")
        st.text("234")
        st.text("564")
        st.text("987")
        st.text("234")
        st.text("5644")
        st.text("987")
        st.text("783")
        st.text("274")
        st.text("736")
        st.text("363")
        st.text("333")
        st.text("445")
        st.text("897")
        st.text("678")
        st.text("456")
        st.text("589")
        st.text("345")
        st.text("998")
        st.text("3445")
        st.text("112")
        st.text("334")
        st.text("454")
        st.text("345")
        st.text("254")



    with col9:

        st.markdown("<h2 class='small-header'>Läs mer</h2>", unsafe_allow_html=True)
        link = "<a href='#' onclick='window.open(\"http://localhost:8501/?app=page2\")' class='custom-button' style='color:white; padding:0.1rem 0.2rem;'>Om Java</a>"
        st.markdown(link, unsafe_allow_html=True)
        st.session_state.current_page = "page2"
        st.session_state.current_file = "page2.py"
            #st.session_state.current_page = "page2"
            #st.session_state.current_file = "page2.py"

        link = "<a href='#' onclick='window.open(\"http://localhost:8501/?app=page2\")' class='custom-button' style='color:white; padding:0.1rem 0.2rem;'>Om Cloud</a>"
        st.markdown(link, unsafe_allow_html=True)
        st.session_state.current_page = "page2"
        st.session_state.current_file = "page2.py"

        link = "<a href='#' onclick='window.open(\"http://localhost:8501/?app=page2\")' class='custom-button' style='color:white; padding:0.1rem 0.2rem;'>Om Python</a>"
        st.markdown(link, unsafe_allow_html=True)
        st.session_state.current_page = "page2"
        st.session_state.current_file = "page2.py"


import numpy as np
import altair as alt

should_execute_main = True


   
def page2():
    subprocess.Popen(["streamlit", "run", "page2.py"], shell=True)
    st.title("LineChart")
    if st.button("Back"):
        st.session_state.current_page = "page1"
        st.session_state.current_file = "app.py"




   

def page5():
    
    st.title("LineChart")
    if st.button("Back"):
        st.session_state.current_page = "page1"
        st.session_state.current_file = "app.py"
        import pandas as pd
#import streamlit as st
#from matplotlib import pyplot as plt

def page3():
    st.write("Hej!")



        

main()
