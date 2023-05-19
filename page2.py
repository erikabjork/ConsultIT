import streamlit as st
import requests
import matplotlib as mpl

# JobTech Historical API base URL
BASE_URL = "https://dev-historical-api.jobtechdev.se"

technologies = [
            'Natural language processing', 'Computer vision', 'Robotics', 'Internet of Things',
            'Blockchain technology', 'Augmented reality', 'Virtual reality', 'Quantum computing',
            'Big data analytics', 'Cloud computing', 'Edge computing', 'Cybersecurity technologies',
            'Autonomous vehicles', 'Genetic engineering', '3D printing/additive manufacturing',
            'Advanced materials science', 'Renewable energy technologies', 'Smart grids', 'Biometrics',
            'Wearable technologies', 'Nanotechnology', 'Cognitive computing', 'Swarm intelligence',
            'Synthetic biology', 'Human-computer interaction', 'Data visualization', 'Analytics tools'
        ]

def fetch_job_ads(query, year):
    endpoint = f"/search?limit=100&offset=0&q={query}&published-after={year}-01-01T00:00:00&published-before={year}-12-31T00:00:00"
    url = BASE_URL + endpoint
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_job_ads(job_ads):
    if job_ads is None:
        st.write("Error fetching job ads. Please try again.")
    elif not job_ads["hits"]:
        st.write("No job ads found for the specified query and year.")
    else:
        st.write(f"Total job ads found: {job_ads['total']['value']}")
        return job_ads['total']['value']

# Streamlit app
def main():
    st.title("Job Ads Explorer")
    query = st.text_input("Enter a query (e.g., python)", max_chars=100)
    if st.button("Search"):
        hits_by_year = {}
        for y in range(2016, 2023):
            job_ads = fetch_job_ads(query, y)
            hits_by_year[y] = display_job_ads(job_ads)
        
        st.write("Hits by Year:")
        for year, hits in hits_by_year.items():
            st.write(f"{year}: {hits}")
        st.write(hits_by_year)

emergent_tech = [
        "Artificial intelligence",
        "Machine learning",
        "Deep learning",
        "Natural language processing",
        "Computer vision",
        "Robotics",
        "Internet of Things",
        "Blockchain technology",
        "Augmented reality",
        "Virtual reality",
        "Quantum computing",
        "Big data analytics",
        "Cloud computing",
        "Edge computing",
        "Cybersecurity technologies"]

if __name__ == "__main__":
    main()
