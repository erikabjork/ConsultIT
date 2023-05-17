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

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def plot_linear_regression(x, y, items):
    model = LinearRegression().fit(x, y)
    x_future = np.array(range(2016, 2026)).reshape((-1, 1))
    y_predicted = model.predict(x_future)

    plt.figure(figsize=(8, 6))

    # Plot the red line first to ensure it's behind the scatter plot
    plt.plot(x_future, y_predicted, color='#f40000', label='Trendline', linewidth=2)

    # Plot the blue scatter plot points
    plt.scatter(x, y, color='#26abff', label='Hits', zorder=9)

    # Plot the green dot above the red line
    plt.scatter(2024, y_predicted[8], color='#50c878', label='Predicted', zorder=10)

    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Number of Ads', fontsize=12)
    plt.title('Linear Regression of ' + items, fontsize=14)
    plt.legend(fontsize=10)

    predicted_value_2024 = int(round(y_predicted[8]))  # Predicted value for 2024 (index 8)
    plt.annotate(
        f'Prediction 2024: {predicted_value_2024}',
        xy=(2024, y_predicted[8]),
        xytext=(2024, y_predicted[8] + 200),
        fontsize=10,
        ha='center',
        va='bottom',  # Adjust the vertical alignment of the text
        bbox=dict(boxstyle='round', facecolor='white', edgecolor='white')  # Add a white background to the annotation text
    )

    return plt





# Streamlit app
def main():
    st.title("Job Ads Explorer")
    query = ['cloud', 'artificiell intelligens', 'big data', 'iot']
    if st.button("Search"):
        for items in query:
            hits_by_year = {}
            for year in range(2016, 2023):
                job_ads = fetch_job_ads(items, year)
                hits = display_job_ads(job_ads)
                hits_by_year[year] = hits

            #st.write("Hits by Year:")
            for year, hits in hits_by_year.items():
                st.write(f"{year}: {hits}")

            x = np.array(list(hits_by_year.keys())).reshape((-1, 1))
            y = np.array(list(hits_by_year.values()))
            fig = plot_linear_regression(x, y, items)
            st.pyplot(fig)

if __name__ == "__main__":
    main()
