import streamlit as st
import pandas as pd

# Load data from the CSV file
data = pd.read_csv("manga.csv")

# Set the number of manga items to display in one column
items_per_column = 5

# Split the data into multiple columns
num_manga = len(data)
num_columns = (num_manga + items_per_column - 1) // items_per_column

st.write("List of Manga")

# Create a dictionary to store manga details
manga_details = {}

# Create columns for manga display
for column_idx in range(num_columns):
    manga_column = st.columns(items_per_column)

    start_idx = column_idx * items_per_column
    end_idx = min((column_idx + 1) * items_per_column, num_manga)

    for manga_idx in range(start_idx, end_idx):
        manga = data.iloc[manga_idx]
        with manga_column[manga_idx % items_per_column]:
            st.image(manga["Link"], use_column_width=True)  # Display the image from the link
            manga_link = f"<a href='http://localhost:8501/manga/{manga_idx}' style='text-decoration: none; color: white;'>{manga['Manga series']}</a>"
            st.markdown(f"<p style='text-align: center;'>{manga_link}</p>", unsafe_allow_html=True)  # Center-align the text
