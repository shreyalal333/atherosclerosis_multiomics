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
# PREVENTION SECTION
# ---------------------------------------------------

st.header("🛡️ How to Reduce Atherosclerosis Risk")

prevention = [
    "Quit smoking",
    "Exercise regularly",
    "Reduce salty and processed foods",
    "Maintain healthy cholesterol levels",
    "Control blood sugar",
    "Manage stress effectively",
    "Improve sleep quality",
    "Monitor blood pressure regularly"
]

cols = st.columns(2)

for i, item in enumerate(prevention):
    cols[i % 2].success(item)

st.markdown("---")

# ---------------------------------------------------
# HEART HEALTHY FOODS
# ---------------------------------------------------

st.header("🥗 Recommended Heart-Healthy Foods")

foods = [
    "Leafy vegetables",
    "Oats and whole grains",
    "Fish rich in omega-3",
    "Nuts and seeds",
    "Olive oil",
    "Berries",
    "Green tea",
    "Fruits rich in antioxidants"
]

food_cols = st.columns(4)

for i, food in enumerate(foods):
    food_cols[i % 4].info(food)

st.markdown("---")

# ---------------------------------------------------
# DOCTOR FINDER
# ---------------------------------------------------

st.header("📍 Find Nearby Cardiologists")

st.info("""
Enter your city or area name to find nearby cardiologists and heart hospitals.
""")

# ---------------------------------------------------
# LOCATION INPUT
# ---------------------------------------------------

location = st.text_input(
    "📌 Enter Location",
    placeholder="Example: Bangalore"
)

# ---------------------------------------------------
# GOOGLE API KEY
# ---------------------------------------------------

API_KEY = st.secrets["GOOGLE_MAPS_API_KEY"]

# ---------------------------------------------------
# SEARCH BUTTON
# ---------------------------------------------------

if st.button("🔍 Search Cardiologists"):

    if location.strip() == "":

        st.warning("Please enter a location.")

    else:

        # ---------------------------------------------------
        # GEOCODING
        # ---------------------------------------------------

        geo_url = (
            "https://maps.googleapis.com/maps/api/geocode/json"
            f"?address={location}"
            f"&key={API_KEY}"
        )

        geo_response = requests.get(geo_url)
        geo_data = geo_response.json()

        if geo_data["status"] != "OK":

            st.error("Location not found.")

        else:

            lat = geo_data["results"][0]["geometry"]["location"]["lat"]
            lng = geo_data["results"][0]["geometry"]["location"]["lng"]

            # ---------------------------------------------------
            # FIND CARDIOLOGISTS
            # ---------------------------------------------------

            places_url = (
                "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
                f"?location={lat},{lng}"
                "&radius=5000"
                "&keyword=cardiologist"
                f"&key={API_KEY}"
            )

            places_response = requests.get(places_url)
            places_data = places_response.json()

            # ---------------------------------------------------
            # CREATE MAP
            # ---------------------------------------------------

            m = folium.Map(
                location=[lat, lng],
                zoom_start=12
            )

            folium.Marker(
                [lat, lng],
                tooltip="Search Location",
                icon=folium.Icon(color="blue")
            ).add_to(m)

            hospitals = []

            # ---------------------------------------------------
            # RESULTS
            # ---------------------------------------------------

            for place in places_data.get("results", []):

                name = place["name"]

                address = place.get(
                    "vicinity",
                    "Address unavailable"
                )

                rating = place.get(
                    "rating",
                    "N/A"
                )

                p_lat = place["geometry"]["location"]["lat"]
                p_lng = place["geometry"]["location"]["lng"]

                google_maps_link = (
                    f"https://www.google.com/maps/search/?api=1&query="
                    f"{p_lat},{p_lng}"
                )

                hospitals.append({
                    "Hospital / Doctor": name,
                    "Address": address,
                    "Rating": rating,
                    "Google Maps": google_maps_link
                })

                # ---------------------------------------------------
                # MAP MARKERS
                # ---------------------------------------------------

                folium.Marker(
                    [p_lat, p_lng],
                    tooltip=name,
                    popup=address,
                    icon=folium.Icon(color="red")
                ).add_to(m)

            # ---------------------------------------------------
            # DISPLAY MAP
            # ---------------------------------------------------

            st.subheader("🗺️ Nearby Cardiologists Map")

            st_folium(
                m,
                width=1000,
                height=500
            )

            # ---------------------------------------------------
            # DISPLAY TABLE
            # ---------------------------------------------------

            st.subheader("🏥 Cardiologists & Heart Hospitals")

            if len(hospitals) > 0:

                hospital_df = pd.DataFrame(hospitals)

                st.dataframe(
                    hospital_df,
                    use_container_width=True
                )

            else:

                st.warning("No cardiologists found nearby.")

st.markdown("---")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.caption("""
This feature uses Google Maps Places API
to identify nearby cardiologists and hospitals.

Not intended for emergency medical use.
""")
