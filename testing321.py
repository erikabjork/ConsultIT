import streamlit as st
import requests
import json

url = 'https://jobsearch.api.jobtechdev.se'
url_for_search = f"{url}/search"

url2 = 'https://dev-historical-api.jobtechdev.se'
url_for_search2 = f"{url2}/search"

# Merge de två get_ads funktionerna så de är i samma pot. Vid Return är (Response1 = Current APIn) och (Response2 = Historical APIn). 
def get_ads(params1, params2):
    headers = {'accept': 'application/json'}
    response1 = requests.get(url_for_search, headers=headers, params=params1)
    response2 = requests.get(url_for_search2, headers=headers, params=params2)
    response1.raise_for_status()  # check for http errors
    response2.raise_for_status()  # check for http errors
    return json.loads(response1.content.decode('utf8')), json.loads(response2.content.decode('utf8'))

# Sökningen sker i samma function men är separerade efter API sökning. (search params = Response1 vilker ät current) och (search_params2 = response2 vilker är historical).
# Return är två hit nummer utefter current och historical. 

def example_search_return_number_of_hits(query):

    search_params = {'q': query}
    search_params2 = {'q': query}
    json_response1, json_response2 = get_ads(search_params, search_params2)
    number_of_hits_current = json_response1['total']['value']
    number_of_hits_historical = json_response2['total']['value']
    return number_of_hits_current, number_of_hits_historical

# Skapar lista med kompetenser. Vi ska självklart lägga till fler men detta är bara för testing. 
competencies = ['Artificial intelligence', 'Machine learning', 'Deep learning', 'Natural language processing', 'Computer vision', 'Robotics', 'Internet of Things', 'Blockchain technology', 'Augmented reality', 'Virtual reality', 'Quantum computing', 'Big data analytics', 'Cloud computing', 'Edge computing', 'Cybersecurity technologies', 'Predictive analytics', 'Autonomous vehicles', 'Genetic engineering', '3D printing/additive manufacturing', 'Advanced materials science', 'Renewable energy technologies', 'Smart grids', 'Biometrics', 'Wearable technologies', 'Nanotechnology', 'Cognitive computing', 'Swarm intelligence', 'Synthetic biology', 'Human-computer interaction', 'Data visualization, ’Analytics tools']
st.write("List of Competencies:")
for competency in competencies:
    st.write("- " + competency)

if __name__ == '__main__':
    results = {}
    # For loop som går igenom alla kompetenser, var för sig. Lägger in just den kompetensen som query, gör en sökning både historical och current.
    # Precis som input sökning bara att den går igenom en lista full med kompetenser som input. 
    for query in competencies:
        number_of_hits_current, number_of_hits_historical = example_search_return_number_of_hits(query)
        results[query] = (number_of_hits_current, number_of_hits_historical)
    
    # Detta går att gör snyggare men hittade ingen annat sätt. Känns som att vi kommer behöva automatisera det. 





#Just nu funkar bara print i terminalen. Gör så för att det tar tid att öppna app.py hela tiden. 

