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
import matplotlib
import matplotlib.pyplot as plt
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


#Start app
if __name__ == "__main__":

#FRONTEND

    # Add the logo image
       # Add the logo
    logo_path = "https://www.akademiskahogtider.se/digitalAssets/818/c_818170-l_3-k_lo_gu_cen2r294c.png"
    #logo = st.image(logo_path, use_column_width=False)
    logo = f'<img src="{logo_path}" style="position: none; top: 10px; left: 10px; width: 100px; margin-left:32%; margin-top:-30%;">'
    st.sidebar.markdown(logo, unsafe_allow_html=True)

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

    st.write(
    "<div style='width 800px;'>"
    "<h1>Om trendlinjen</h1>"
    "<p>Denna trendlinjen är baserad på den andra API:n som innehåller historiska annonser på den svenska jobbmarknaden. Vi har skapat en trendlinje genom att tillämpa maskininlärning och programmering för att ge den mest precisa förutsägelsen. Genom att analysera data och mönster har vi lyckats framgångsrikt skapa en linje som förutser trenderna. Det finns små missar i API:n, men trots detta har vi ändå lyckats bra med resultatet. Vi fortsätter att förbättra och finslipa vår trendlinje för att erbjuda bästa möjliga resultat. </p>"
    "</div>",
    unsafe_allow_html=True
)

    st.subheader('Om ' + technology)

    #Vi gör såhär för varenda tech som är med i listan. Så det är en liten sammanfattning. :)
    if technology == 'Augmented Reality':
        st.write('Augmented reality är en ny teknologi som gör det möjligt att överlägga digitala objekt och information på den fysiska världen, vilket skapar en förstärkt synupplevelse.')
        st.write('')

    elif technology == 'Virtual Reality':
        st.write('Virtual reality är en teknologi som skapar en simulerad, datorgenererad miljö som användaren kan interagera med och uppleva som om den vore verklig.')
        st.write('')

    elif technology == 'Internet of Things':
        st.write('Internet of Things (IoT) innebär att fysiska enheter och objekt är anslutna till internet och kan samla in och utbyta data. Det möjliggör smarta och automatiserade lösningar.')
        st.write('')

    elif technology == 'Blockchain':
        st.write('Blockchain är en decentraliserad och distribuerad teknik som används för att lagra och verifiera transaktioner. Den ger ökad säkerhet och transparens inom exempelvis digitala valutor och avtalsprocesser.')
        st.write('')

    elif technology == 'Artificiell Intelligens':
        st.write('Artificiell intelligens (AI) är en teknologi som fokuserar på att skapa datorer och system som kan utföra uppgifter som normalt kräver mänsklig intelligens. Det inkluderar områden som maskininlärning, naturlig språkbearbetning och bildigenkänning.')
        st.write('')

    elif technology == 'Cloud':
        st.write('Cloud computing är en teknik som tillåter tillgång till datalagring, beräkningsresurser och programvara över internet. Det gör det möjligt att snabbt skalas upp eller ner efter behov och undvika behovet av att hantera egna fysiska servrar.')
        st.write('')

    elif technology == 'Web3':
        st.write('Web3 representerar den nästa generationens webb, där decentraliserade applikationer (DApps) och blockchain-teknik används för att skapa en mer öppen, censurresistent och autonom webbmiljö.')
        st.write('')

    elif technology == 'Quantum Computing':
        st.write('Kvantdatorer är en ny typ av datorer som använder sig av kvantmekaniska principer för att utföra beräkningar. De kan lösa komplexa problem avsevärt snabbare än traditionella datorer inom områden som kryptografi och optimering.')
        st.write('')

    elif technology == 'Cyber Security':
        st.write('Cybersäkerhet omfattar teknologier, processer och metoder för att skydda datorsystem, nätverk och data mot digitala hot och attacker. Det inkluderar bland annat brandväggar, antivirusprogram, kryptering och säkerhetsprotokoll.')
        st.write('')

    elif technology == '5G':
        st.write('5G är den femte generationens trådlösa kommunikationsteknik. Den ger betydligt högre hastighet, lägre fördröjning och större kapacitet än tidigare generationer av mobilnätverk, vilket möjliggör snabbare dataöverföring och stöd för en mängd nya applikationer och enheter.')
        st.write('')

    elif technology == '3D Printing':
        st.write('3D-utskrift, eller additiv tillverkning, är en teknik som skapar fysiska objekt genom att lägga till material i lager istället för att ta bort det från ett block av material. Det möjliggör snabb prototyptillverkning, anpassade produkter och mer effektiv produktion.')
        st.write('')

    elif technology == 'Edge Computing':
        st.write('Edge computing är en modell för datalagring och bearbetning där data hanteras nära källan istället för att skickas till en central molntjänst. Det ger snabbare responstider, minskad belastning på nätverket och möjliggör realtidsapplikationer.')
        st.write('')

    elif technology == 'Big data':
        st.write('Big data hänvisar till stora och komplexa datamängder som är för stora för att bearbetas med traditionella databearbetningsmetoder. Det handlar om att samla in, lagra, hantera och analysera data för att extrahera insikter och mönster för bättre beslutsfattande.')
        st.write('')

    elif technology == 'Autonomous vehicles':
        st.write('Autonoma fordon, eller självkörande fordon, är fordon som kan navigera och köra utan mänsklig inblandning. De använder sensorer, kameror, radarteknik och avancerade algoritmer för att upptäcka och reagera på omgivningen.')
        st.write('')

    elif technology == 'Smart grids':
        st.write('Smart grids är moderna elnät som använder digital teknik och kommunikationsprotokoll för att optimera distributionen och användningen av elektricitet. De möjliggör smart mätning, fjärrstyrning av enheter och bättre hantering av energiflöden.')
        st.write('')

    elif technology == 'Wearable technologies':
        st.write('Wearable technologies refererar till tekniska enheter och datorer som kan bäras på kroppen, vanligtvis i form av smycken, kläder eller accessoarer. De används för att övervaka hälsa och fitness, ge tillgång till information eller möjliggöra interaktion med digitala system.')
        st.write('')

    elif technology == 'Nanotechnology':
        st.write('Nanoteknik är studien och användningen av material och strukturer på nanometerskala. Den möjliggör framsteg inom olika områden som materialvetenskap, medicin, energi och elektronik genom att manipulera materialet på atomnivå.')
        st.write('')

    elif technology == 'Cognitive computing':
        st.write('Kognitiv databehandling är en gren inom AI som syftar till att replikera mänskliga kognitiva funktioner, såsom tänkande, resonemang och problemlösning. Den använder avancerade algoritmer och modeller för att bearbeta och förstå komplexa data och mönster.')
        st.write('')

    elif technology == 'Human-computer interaction':
        st.write('Human-computer interaction (HCI) handlar om designen och interaktionen mellan människor och datorer. Det fokuserar på att skapa användarvänliga och effektiva gränssnitt, inklusive röststyrning, gestigenkänning och naturlig användarinteraktion.')
        st.write('')

    elif technology == 'Data visualization':
        st.write('Data visualisering innebär att presentera data på ett visuellt och lättförståeligt sätt. Det hjälper till att identifiera mönster, trender och insikter från stora datamängder genom att använda diagram, grafer, kartor och andra visuella representationer.')
        st.write('')

    elif technology == 'Analytics tool':
        st.write('Analytics tool refererar till mjukvaruverktyg och tekniker som används för att samla in, hantera och analysera data för att extrahera insikter och fatta datadrivna beslut. Det kan inkludera verktyg för datahantering, visualisering, prediktiv analys och maskininlärning.')
        st.write('')
    
    else:
        st.write('')


st.write(
    "<div style='width 800px;'>"
    "<h1>Emerging Technologies</h1>"
    "<p>Det här verktyget är utformat för att analysera hur utbredda framväxande teknologier är på den svenska arbetsmarknaden. Applikationen är ansluten till två olika API:er från JobTechDev. "
    "<b>Aktiva annonser</b> är kopplat till det första API:et och visar aktuella annonser som söker kunskaper inom respektive teknologi. "
    "När du klickar på den <b>blå knappen</b> hittar du informationen längst ner på sidan, vilket ger dig möjlighet att undersöka trender och historiska jobbannonser.</p>"
    "</div>",
    unsafe_allow_html=True
)

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

technologies = ['Augmented Reality', 'Virtual Reality', 'Internet of Things', 'Blockchain', 'Artificiell Intelligens',
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
                    "<div style='width: 30%;'>"
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
