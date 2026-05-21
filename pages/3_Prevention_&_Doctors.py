import streamlit as st
import requests
import pandas as pd
import folium
from streamlit_folium import st_folium

# ---------------------------------------------------
# PAGE TITLE
# ---------------------------------------------------

st.title("❤️ Prevention & Cardiologist Finder")

st.markdown("---")

# ---------------------------------------------------
# PREVENTION STRATEGIES
# ---------------------------------------------------

st.header("🛡️ Prevention Strategies")

prevention = [
    "Quit smoking",
    "Exercise regularly",
    "Reduce processed and salty foods",
    "Maintain healthy cholesterol",
    "Control blood sugar",
    "Improve sleep quality",
    "Manage stress effectively",
    "Monitor blood pressure regularly"
]

col1, col2 = st.columns(2)

for i, item in enumerate(prevention):
    if i % 2 == 0:
        col1.success(item)
    else:
        col2.success(item)

st.markdown("---")

# ---------------------------------------------------
# HEART HEALTHY FOODS
# ---------------------------------------------------

st.header("🥗 Recommended Heart-Healthy Foods")

foods = [
    "Leafy vegetables",
    "Whole grains",
    "Omega-3 rich fish",
    "Olive oil",
    "Nuts and seeds",
    "Berries",
    "Green tea",
    "Fresh fruits"
]

food_cols = st.columns(4)

for i, food in enumerate(foods):
    food_cols[i % 4].info(food)

st.markdown("---")

# ---------------------------------------------------
# CARDIOLOGIST FINDER
# ---------------------------------------------------

import urllib.parse

location = st.text_input(
    "Enter your city"
)

if st.button("Find Cardiologists"):

    if location:

        encoded_location = urllib.parse.quote(location)

        maps_url = (
            "https://www.google.com/maps/search/"
            f"cardiologist+near+{encoded_location}"
        )

        st.success("Click below to view nearby cardiologists.")

        st.markdown(
            f"[Open Google Maps]({maps_url})"
        )
