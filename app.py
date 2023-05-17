import streamlit as st
import requests
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
    elif not job_ads["hits"]:
        st.write("No job ads found for the specified query and year.")
    else:
        total_hits = job_ads['total']['value']
        #st.write(f"Total job ads found: {total_hits}")
        return total_hits

def plot_linear_regression(x, y, query):
    model = LinearRegression().fit(x, y)
    x_future = np.array(range(2016, 2026)).reshape((-1, 1))
    y_predicted = model.predict(x_future)

    plt.figure()
    plt.scatter(x, y, color='black', label='Hits')
    plt.plot(x_future, y_predicted, color='red', label='Trendline')
    plt.xlabel('Year')
    plt.ylabel('Number of Ads')
    plt.title('Linear Regression of ' + query)
    plt.legend()

    predicted_value_2024 = int(round(y_predicted[8]))  # Predicted value for 2024 (index 8)
    st.write("Predicted value for 2024:", predicted_value_2024)

    return plt

# Streamlit app
def main():
    st.title("Job Ads Explorer")
    query = st.text_input("Enter a query (e.g., python)", max_chars=100)
    if st.button("Search"):
        hits_by_year = {}
        for year in range(2016, 2023):
            job_ads = fetch_job_ads(query, year)
            hits = display_job_ads(job_ads)
            hits_by_year[year] = hits

        #st.write("Hits by Year:")
        for year, hits in hits_by_year.items():
            st.write(f"{year}: {hits}")

        x = np.array(list(hits_by_year.keys())).reshape((-1, 1))
        y = np.array(list(hits_by_year.values()))
        fig = plot_linear_regression(x, y, query)
        st.pyplot(fig)

if __name__ == "__main__":
    main()
