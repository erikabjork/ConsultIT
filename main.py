import streamlit as st
import requests
import json
import subprocess
import numpy as np
import altair as alt
import pandas as pd
from streamlit_option_menu import option_menu
import page2
from page2 import get_content

import streamlit as st
import requests
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# JobTech Historical API base URL
BASE_URL = "https://dev-historical-api.jobtechdev.se"

def fetch_job_ads(query, year):
    endpoint = f"/search?limit=100&offset=0&q={query}&published-after={year}-01-01T00:00:00&published-before={year}-12-31T00:00:00"
    url = BASE_URL + endpoint
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def display_job_ads(job_ads):
    if job_ads is None:
        st.write("Error fetching job ads. Please try again.")
    else:
        total_hits = job_ads['total']['value']
        #st.write(f"Total job ads found: {total_hits}")
        return total_hits
    
current = 'https://jobsearch.api.jobtechdev.se'
current_search = f"{current}/search"

def get_ads(params):
    headers = {'accept': 'application/json'}
    response = requests.get(current_search, headers=headers, params=params)
    response.raise_for_status()  # check for http errors
    return json.loads(response.content.decode('utf8'))

def example_search_return_number_of_hits(query):
    search_params = {'q': query}
    try:
        json_response = get_ads(search_params)
        number_of_hits_current = json_response['total']['value']
        return number_of_hits_current
    except (requests.HTTPError, json.JSONDecodeError) as e:
        print(f"Error retrieving number of hits for '{query}': {str(e)}")

def plot_linear_regression(x, y, items):
    plt.figure(figsize=(8, 6))

    # Plot the scatter plot points
    plt.scatter(x, y, color='#26abff', label='Hits', zorder=3)

    # Plot the trend line
    plt.plot(x, y, color='#f40000', label='Trendline', linewidth=2, zorder=2)

    # Plot the last predicted point
    x_future = np.array(range(2019, 2025)).reshape((-1, 1))
    model = LinearRegression().fit(x, y)
    y_predicted = model.predict(x_future)
    predicted_value_2024 = int(round(y_predicted[5]))  # Predicted value for 2024 (index 5)
    plt.scatter(2024, y_predicted[5], color='#50c878', label='Prediction', zorder=1)
    plt.plot(x_future, y_predicted, color='#50c878', linewidth=2, zorder=1)

    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Number of Ads', fontsize=12)
    plt.title('Trend Chart of ' + items, fontsize=14)
    plt.legend(fontsize=10)

    plt.annotate(
        f'Prediction 2024: {predicted_value_2024}',
        xy=(2024, y_predicted[5]),
        xytext=(2024, y_predicted[5]),  # Adjusted y-coordinate for the text
        fontsize=10,  # Adjust the font size
        ha='center',
        va='bottom',  # Adjust the vertical alignment of the text
        bbox=dict(boxstyle='round', facecolor='white', edgecolor='white')  # Add a white background to the annotation text
    )

    return plt



# Streamlit app

            

    

if __name__ == "__main__":


#FRONTEND

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


button_styles = f'''
    color: white;
    background-color: #1cb2f5;
    padding: 0.1rem 0.2rem;
    width:70%;
    text-align: center;
    font-size: 14px
    float:right;
    text-align:center;
    overflow:hidden;  
    margin-left:27%;
    display:block;       


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

def main_2():
    current_page = st.session_state.get("current_page", "page1")

    if current_page == "page1":
        page1()
    if current_page == "page2":
        page2()



def page1():    
    #clicked = True
    #querystr = str(query)
    #example_search_loop_through_hits(querystr)
    #example_search_return_number_of_hits(querystr)

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

def onclicked():   
    st.session_state.current_page = 'page2'
    st.session_state.current_file = 'page2.py'

import streamlit as st

def page2():
    technology = st.session_state.technology
    hits_by_year = {}
    for year in range(2019, 2023):
        job_ads = fetch_job_ads(technology, year)
        hits = display_job_ads(job_ads)
        if hits is None:
            hits = 0
        hits_by_year[year] = hits

    x = np.array(list(hits_by_year.keys())).reshape((-1, 1))
    y = np.array(list(hits_by_year.values()))
    fig = plot_linear_regression(x, y, technology)

    st.pyplot(fig)

    if technology == 'python':
        st.write("Python is a popular programming language known for its simplicity and readability. It is widely used in various domains, including web development, data analysis, machine learning, and more. Python has a large standard library and a vast ecosystem of third-party packages, making it a versatile language for different applications.")
        st.write("Python works by interpreting the code written by the developer and executing it line by line. It uses an automatic memory management system and supports object-oriented programming, functional programming, and procedural programming paradigms.")
    
    # Add your back button code here



#MARKDOWN
st.write("""
    <div style='display: flex; align-items: center; margin-bottom: 10px; font-size: 12px;'>
        <div style='width: 30%;'>
            <h2 class='' style="font-size:18px;">Emergent Technology</h2>
        </div>
        <div style='width: 20%; margin-left: 5%;'>
            <h2 class='' style="font-size:18px;">Aktiva annonser</h2>
        </div>
        <div style='width: 30%; margin-left: 15%;'>
            <h2 class='' style="font-size:18px;">Läs mer och se trend</h2>
        </div>
    </div>
""", unsafe_allow_html=True)



# Individual div for "IoT"

technologies = ['python', 'Augmented Reality', 'Virtual Reality', 'Iot', 'Blockchain', 'Artificiell Intelligens',
                'Cloud', 'Web3', 'Quantum Computing', 'Cyber Security', '5G', '3D Printing', 'Edge Computing',
                'Big data', 'Autonomous vehicles', 'Smart grids', 'Wearable technologies', 'Nanotechnology',
                 'Cognitive computing','Human-computer interaction', 'Data visualization', 'Analytics tool'
                  ]

# Create a list to store the tuples (technology, num)
results = []

for technology in technologies:
    num = example_search_return_number_of_hits(technology)
    results.append((technology, num))

# Sort the results based on the num value in descending order
results.sort(key=lambda x: x[1], reverse=True)

for technology, num in results:
    co1, co2 = st.columns([1, 1])
    with co1:
        st.markdown("<div style='display: flex; align-items: center; margin-bottom: 10px;'>"
                    "<div style='width: 700px;'>"
                    "<p style='font-size: 14px; margin: 0;'>{}</p>"
                    "</div>"
                    "<div style='width: 20%;'>"
                    "<p style='font-size: 14px; margin: 0;'>{}</p>"
                    "</div>"
                    "<div style='width: 40%; display: flex; justify-content: center;'>"
                    "</div>"
                    "</div>"
                    "<hr style='margin-top: 5px; margin-bottom: 5px;'>".format(technology, num),
                    unsafe_allow_html=True)

    with co2:
        if st.button(label="Om {}".format(technology), key="button_{}".format(technology)):
            # Code to execute when the button is pressed
            st.session_state.current_page = 'page2'
            st.session_state.current_file = 'page2.py'
            st.session_state.technology = technology





            # Perform additional actions or computations

#commmitchange
main_2()
