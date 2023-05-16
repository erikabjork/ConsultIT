import streamlit as st
import requests

# JobTech Historical API base URL
BASE_URL = "https://dev-historical-api.jobtechdev.se"

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
        for ad in job_ads["hits"]:
            st.write(f"Publication date: {ad['publication_date']}")
            st.write(f"Headline: {ad['headline']}")
            st.write(f"Matched text: {ad['description']}")
            st.write("---")

# Streamlit app
def main():
    st.title("Job Ads Explorer")
    query = st.text_input("Enter a query (e.g., python)", max_chars=100)
    year = st.number_input("Enter a year", min_value=2016, max_value=2022, step=1)
    if st.button("Search"):
        job_ads = fetch_job_ads(query, year)
        display_job_ads(job_ads)

if __name__ == "__main__":
    main()
