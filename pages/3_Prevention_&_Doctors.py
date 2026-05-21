import streamlit as st
import requests
import pandas as pd
from streamlit_geolocation import streamlit_geolocation
import folium
from streamlit_folium import st_folium

st.title("❤️ Prevention & Cardiologist Finder")

st.markdown("---")

st.header("🛡️ Prevention Strategies")

prevention = [
    "Quit smoking",
    "Exercise regularly",
    "Reduce salty and processed foods",
    "Maintain healthy cholesterol",
    "Manage blood sugar",
    "Improve sleep quality",
    "Reduce stress",
    "Monitor blood pressure"
]

for item in prevention:
    st.write("✅", item)

st.markdown("---")

st.header("🥗 Heart Healthy Foods")

foods = [
    "Leafy vegetables",
    "Whole grains",
    "Fish rich in omega-3",
    "Olive oil",
    "Nuts and seeds",
    "Berries"
]

cols = st.columns(3)

for i, food in enumerate(foods):
    cols[i % 3].info(food)

st.markdown("---")

st.header("📍 Nearby Cardiologist Finder")

st.info("Allow browser location access.")

location = streamlit_geolocation()

API_KEY = st.secrets["GOOGLE_MAPS_API_KEY"]

if location and location["latitude"]:

    lat = location["latitude"]
    lon = location["longitude"]

    url = (
        "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        f"?location={lat},{lon}"
        "&radius=5000"
        "&keyword=cardiologist"
        f"&key={API_KEY}"
    )

    response = requests.get(url)
    data = response.json()

    m = folium.Map(location=[lat, lon], zoom_start=12)

    folium.Marker(
        [lat, lon],
        tooltip="Your Location",
        icon=folium.Icon(color="blue")
    ).add_to(m)

    doctors = []

    for place in data.get("results", []):

        name = place["name"]
        address = place.get("vicinity", "No address")

        p_lat = place["geometry"]["location"]["lat"]
        p_lon = place["geometry"]["location"]["lng"]

        doctors.append({
            "Hospital": name,
            "Address": address
        })

        folium.Marker(
            [p_lat, p_lon],
            tooltip=name,
            icon=folium.Icon(color="red")
        ).add_to(m)

    st_folium(m, width=1000, height=500)

    st.subheader("🏥 Nearby Cardiologists")

    st.dataframe(pd.DataFrame(doctors))

else:
    st.warning("Please allow location access.")
