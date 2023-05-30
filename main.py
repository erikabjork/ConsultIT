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

    x_future = np.array(range(2016, 2025)).reshape((-1, 1))
    model = LinearRegression().fit(x, y)
    y_predicted = model.predict(x_future)
    predicted_value_2024 = int(round(y_predicted[8])) 
 

    residuals = y - model.predict(x)
    std_residuals = np.std(residuals)
    upper_bound = y_predicted + 0.5 * std_residuals
    lower_bound = y_predicted - 0.5 * std_residuals
    

    plt.plot(x_future, upper_bound, color='#50c878', linestyle='--', linewidth=1, zorder=1, label='Upper prediction')
    plt.plot(x_future, lower_bound, color='#A91B0D', linestyle='--', linewidth=1, zorder=1, label='Lower prediction')
    plt.fill_between(x_future.flatten(), y_predicted, upper_bound, color='#50c878', alpha=0.1, hatch='/', edgecolor='none')
    plt.fill_between(x_future.flatten(), y_predicted, lower_bound, color='#A91B0D', alpha=0.1, hatch='\\', edgecolor='none')
    
    plt.scatter(2024, y_predicted[8], color='#50c878', label='Prediction', zorder=1)
    plt.plot(x_future, y_predicted, color='#50c878', linewidth=2, zorder=1)

    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Number of Ads', fontsize=12)
    plt.title('Trend Chart of ' + items, fontsize=14)
    plt.legend(fontsize=10)

    plt.annotate(
        f'Prediction 2024: {predicted_value_2024}',
        xy=(2024, y_predicted[8]),
        xytext=(2024, y_predicted[8]),  # Adjusted y-coordinate for the text
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
        choose = option_menu(" ‎ ‎ ‎Systemvetenskap", ["Beskrivning", "Om ConsultIT", "Om API:erna", "Kontakt"],
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
            st.markdown("<hr style='width:100px; height:1px; background-color:black'>", unsafe_allow_html=True)
            st.write('<span style="font-size:14px">Applikationen visar de emergent technologies som efterfrågas på arbetsmarknaden från år 2016 till 2023. Applikationen syfte är att agera som hjälpmedel för programansvarig på systemvetenskapliga program på universitet att enklare anpassa utbudet på de valbara kurserna som erbjuds till studenter. Med hjälp av linjediagram kan användaren få en överblick om trendutveckling och se prognos för kommande år.</span>', unsafe_allow_html=True)
            st.markdown("<hr style='width:100px; height:1px; background-color:black'>", unsafe_allow_html=True)
        elif choose == 'Om ConsultIT':
            st.markdown("<hr style='width:100px; height:1px; background-color:black'>", unsafe_allow_html=True)
            st.write('<span style="font-size:14px">Vi är en konsultfirma specialiserad på att stödja universitet och högre utbildningsinstitutioner. Med vår erfarenhet och djupa förståelse för utmaningarna inom den akademiska världen erbjuder vi skräddarsydda lösningar och expertis för att hjälpa universitet att nå sina strategiska mål.</span>', unsafe_allow_html=True)
            st.markdown("<hr style='width:100px; height:1px; background-color:black'>", unsafe_allow_html=True)
        elif choose == 'Om API:erna':
            st.markdown("<hr style='width:100px; height:1px; background-color:black'>", unsafe_allow_html=True)
            st.write('<span style="font-size:14px">Applikationen använder data från källan https://jobtechdev.se, specifikt dataseten "Historiska annonser" och "JobSearch Trends", för att genomföra en noggrann analys. Dessa dataset ger både historiska och aktuella jobbannonser, vilket möjliggör en relevant analys. Datan sträcker sig från år 2016 till 2023.</span>', unsafe_allow_html=True)
            st.markdown("<hr style='width:100px; height:1px; background-color:black'>", unsafe_allow_html=True)
        elif choose == 'Kontakt':
            st.markdown("<hr style='width:100px; height:1px; background-color:black'>", unsafe_allow_html=True)
            st.write('<span style="font-size:14px">Kontakta oss på info@consultit.com</span>', unsafe_allow_html=True)
            st.markdown("<hr style='width:100px; height:1px; background-color:black'>", unsafe_allow_html=True)



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
    for year in range(2016, 2023):
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
    if technology == 'Python':
        st.write('Python är ett populärt programmeringsspråk känt för sin enkelhet och läsbarhet. Det har en omfattande ekosystem av bibliotek och ramverk som gör det lämpligt för olika ändamål.')

    elif technology == 'C+':
        st.write('C+ (C Plus Plus) är ett programmeringsspråk som bygger på C-språket och erbjuder funktioner för objektorienterad programmering. Det används ofta för systemprogrammering och resurskrävande applikationer.')

    elif technology == 'C++':
        st.write('C++ är ett mångsidigt programmeringsspråk som bygger på C-språket och tillhandahåller stöd för objektorienterad programmering. Det används i en mängd olika applikationsområden.')

    elif technology == 'Flutter':
        st.write('Flutter är ett ramverk utvecklat av Google för att bygga användargränssnitt för mobilapplikationer. Det använder sig av Dart-programmeringsspråket och erbjuder snabb utveckling och enkel plattformsoberoende.')

    elif technology == 'Java':
        st.write('Java är ett kraftfullt och populärt programmeringsspråk som används för att utveckla olika typer av applikationer, inklusive webbapplikationer, mobila appar och stora system.')

    elif technology == 'Cloud':
        st.write('Cloud, eller molnet, är en term som används för att hänvisa till datalagring och databehandling på distans via internet. Det möjliggör skalbarhet, tillgänglighet och flexibilitet för att hantera data och köra applikationer.')

    elif technology == 'Web3':
        st.write('Web3 syftar på den tredje generationen av webbapplikationer där decentraliserade och blockchain-baserade teknologier används för att skapa och distribuera applikationer och tjänster.')

    elif technology == 'Javascript':
        st.write('Javascript är ett populärt programmeringsspråk som används för att skapa interaktiva och dynamiska webbsidor. Det är en av de mest använda teknologierna för frontend-utveckling.')

    elif technology == 'PHP':
        st.write('PHP är ett server-side programmeringsspråk som främst används för att skapa dynamiska webbsidor och webbapplikationer. Det är en av de mest använda teknologierna för webbutveckling.')

    elif technology == 'React':
        st.write('React är ett populärt JavaScript-baserat ramverk för att bygga användargränssnitt. Det används för att utveckla snabba och skalbara webbapplikationer med en komponentbaserad arkitektur.')

    elif technology == 'Angular':
        st.write('Angular är ett kraftfullt TypeScript-baserat ramverk för att bygga webbapplikationer. Det erbjuder en omfattande uppsättning verktyg och funktioner för att underlätta utveckling och underhåll av stora projekt.')

    elif technology == 'Next.js':
        st.write('Next.js är ett ramverk för server-side rendering och statisk webbplatsgenerering med React. Det används för att bygga snabba och SEO-vänliga webbapplikationer med enkelhet.')

    elif technology == 'HTML':
        st.write('HTML (Hypertext Markup Language) är standardmärkspråket för att skapa webbsidor och webbapplikationer. Det definierar strukturen och layouten för innehållet på en webbsida.')

    elif technology == 'CSS':
        st.write('CSS (Cascading Style Sheets) är språket som används för att definiera utseendet och layouten av webbsidor. Det används tillsammans med HTML för att styla och formatera webbplatsinnehåll.')

    elif technology == 'MongoDB':
        st.write('MongoDB är en dokumentdatabas som används för att lagra och hantera strukturerade data. Det erbjuder skalbarhet, flexibilitet och snabb dataåtkomst och används ofta inom webbutveckling och molntjänster.')

    elif technology == 'SQL':
        st.write('SQL (Structured Query Language) är ett programmeringsspråk som används för att kommunicera med och hantera relationella databaser. Det används för att hämta, infoga, uppdatera och ta bort data i databaser.')

    elif technology == 'Django':
        st.write('Django är ett Python-baserat ramverk för webbutveckling som fokuserar på snabb utveckling och enkelhet. Det erbjuder en robust uppsättning verktyg och funktioner för att bygga skalbara och säkra webbapplikationer.')

    elif technology == 'Swift':
        st.write('Swift är ett programmeringsspråk utvecklat av Apple för att skapa applikationer för iOS, macOS och andra Apple-plattformar. Det är känt för sin säkerhet, prestanda och enkelhet att använda.')

    elif technology == 'Projektledning':
        st.write('Projektledning är disciplinen att planera, organisera och styra resurserna för att slutföra ett projekt framgångsrikt. Det omfattar att definiera mål, schemaläggning, resurshantering och kommunikation.')

    elif technology == 'NFT':
        st.write('NFT (Non-Fungible Token) är en typ av digital tillgång som representerar ägandeskap eller äganderätt till ett unikt objekt eller tillgång. Det används främst inom blockchain-teknologi.')

    elif technology == 'Maskininlärning':
        st.write('Maskininlärning är en gren av artificiell intelligens som fokuserar på att utveckla algoritmer och tekniker som gör att datorer kan lära sig och fatta beslut baserat på data utan att vara explicit programmerade.')

    elif technology == 'UX':
        st.write('UX (User Experience) syftar på användarupplevelsen av en produkt eller tjänst. Det inkluderar alla interaktioner och intryck som användaren har när de använder produkten och fokuserar på att skapa en positiv och tillfredsställande upplevelse.')

    elif technology == 'UI':
        st.write('UI (User Interface) syftar på det visuella gränssnittet för en produkt eller tjänst. Det inkluderar layout, designelement och interaktiva funktioner som användaren interagerar med.')

    elif technology == 'Programmering':
        st.write('Programmering är processen att skapa och utveckla instruktioner (kod) som en dator kan följa för att utföra specifika uppgifter eller lösa problem. Det finns olika programmeringsspråk och tekniker för att skriva kod.')

    elif technology == 'Git':
        st.write('Git är ett distribuerat versionshanteringssystem som används för att spåra ändringar i källkoden under utvecklingsprocessen. Det möjliggör samarbete, spårning av ändringar och återställning av tidigare versioner.')

    elif technology == 'Systemutveckling':
        st.write('Systemutveckling syftar på processen att skapa och implementera programvara eller system för att möta specifika behov eller lösa problem. Det omfattar analys, design, implementering och testning av systemet.')

    elif technology == 'Databaser':
        st.write('Databaser är strukturerade samlingar av data som kan hanteras, lagras och åtkommas på ett organiserat sätt. De används för att lagra och hantera stora mängder data i olika applikationer och system.')

    elif technology == 'Big data':
        st.write('Big data hänvisar till stora och komplexa datamängder som är för stora för att hanteras med traditionella databas- och analysverktyg. Det involverar analys av stora dataset för att få insikter och möjliga användningar.')

    elif technology == 'Visualization':
        st.write('Visualization handlar om att presentera data och information på ett visuellt sätt för att underlätta förståelse och upptäckt av mönster. Det inkluderar användning av diagram, diagram, interaktiva kartor och andra visuella representationer.')

    elif technology == 'AI':
        st.write('AI (Artificiell Intelligens) syftar på datorer och system som kan utföra uppgifter som normalt kräver mänsklig intelligens. Det involverar användning av algoritmer och maskininlärningstekniker för att möjliggöra självlärande och beslutsfattande.')
    
    else:
        st.write('Beskrivning saknas för ' + technology)

st.write(
    "<div style='width 800px;'>"
    "<h1>Teknologier</h1>"
    "<p>Det här verktyget är utformat för att analysera hur utbredda framväxande teknologier och kunskapsområden är på den svenska arbetsmarknaden. Applikationen är ansluten till två olika API:er från JobTechDev. "
    "<b>Aktiva annonser</b> är kopplat till det första API:et och visar aktuella annonser som söker kunskaper inom respektive område. "
    "När du klickar på den <b>blå knappen</b> hittar du <b>informationen längst ner på sidan</b>, vilket ger dig möjlighet att undersöka trender och historiska jobbannonser.</p>"
    "</div>",
    unsafe_allow_html=True
)

#MARKDOWN
st.write("""
    <div style='display: flex; align-items: center; margin-bottom: 10px; font-size: 12px;'>
        <div style='width: 30%;'>
            <h2 class='' style="font-size:18px;">Teknologier</h2>
        </div>
        <div style='width: 20%; margin-left: 5%;'>
            <h2 class='' style="font-size:18px;">Aktiva annonser</h2>
        </div>
        <div style='width: 30%; margin-left: 15%;'>
            <h2 class='' style="font-size:18px;">Läs mer och se trend</h2>
        </div>
    </div>
""", unsafe_allow_html=True)

technologies = ['Python', 'C+', 'C++', 'Flutter', 'Java',
                'Cloud', 'Web3', 'Javascript', 'PHP', 'React', 'Angular', 'Next.js',
                'HTML', 'CSS', 'MongoDB', 'SQL','Django', 'Swift',
                'Projektledning','NFT', 'Maskininlärning', 'UX', "UI", "Programmering", "Git", "Systemutveckling", 
                'Databaser', 'Big data', 'Visualization', 'AI'
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
