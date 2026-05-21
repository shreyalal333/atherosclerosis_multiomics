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

st.header("📍 Nearby Cardiologist Finder")

st.info("""
Enter your city or area name to locate nearby
cardiologists and heart hospitals.
""")

location = st.text_input(
    "📌 Enter Location",
    placeholder="Example: Bangalore"
)

# ---------------------------------------------------
# SEARCH BUTTON
# ---------------------------------------------------

if st.button("🔍 Find Cardiologists"):

    if location.strip() == "":

        st.warning("Please enter a location.")

    else:

        # ---------------------------------------------------
        # GEOCODING USING OPENSTREETMAP
        # ---------------------------------------------------

        geocode_url = (
            f"https://nominatim.openstreetmap.org/search"
            f"?q={location}&format=json&limit=1"
        )

        headers = {
            "User-Agent": "streamlit-app"
        }

        geo_response = requests.get(
            geocode_url,
            headers=headers
        )

        geo_data = geo_response.json()

        # ---------------------------------------------------
        # LOCATION NOT FOUND
        # ---------------------------------------------------

        if len(geo_data) == 0:

            st.error("Location not found.")

        else:

            lat = float(geo_data[0]["lat"])
            lon = float(geo_data[0]["lon"])

            st.success(f"Location Found: {location}")

            # ---------------------------------------------------
            # OVERPASS QUERY
            # ---------------------------------------------------

            overpass_query = f"""
            [out:json];
            (
              node
                [amenity=hospital]
                (around:5000,{lat},{lon});

              node
                [healthcare=doctor]
                (around:5000,{lat},{lon});
            );
            out;
            """

            overpass_url = "https://overpass-api.de/api/interpreter"

            response = requests.get(
                overpass_url,
                params={'data': overpass_query}
            )

            data = response.json()

            # ---------------------------------------------------
            # CREATE MAP
            # ---------------------------------------------------

            m = folium.Map(
                location=[lat, lon],
                zoom_start=12
            )

            # User location marker

            folium.Marker(
                [lat, lon],
                tooltip="Search Location",
                icon=folium.Icon(color="blue")
            ).add_to(m)

            hospitals = []

            # ---------------------------------------------------
            # ADD HOSPITALS
            # ---------------------------------------------------

            for element in data.get("elements", []):

                tags = element.get("tags", {})

                name = tags.get(
                    "name",
                    "Unnamed Hospital"
                )

                hospital_lat = element.get("lat")
                hospital_lon = element.get("lon")

                hospitals.append({
                    "Hospital / Clinic": name,
                    "Latitude": hospital_lat,
                    "Longitude": hospital_lon
                })

                # Add marker

                folium.Marker(
                    [hospital_lat, hospital_lon],
                    tooltip=name,
                    icon=folium.Icon(color="red")
                ).add_to(m)

            # ---------------------------------------------------
            # DISPLAY MAP
            # ---------------------------------------------------

            st.subheader("🗺️ Nearby Hospitals & Cardiologists")

            st_folium(
                m,
                width=1000,
                height=500
            )

            # ---------------------------------------------------
            # DISPLAY TABLE
            # ---------------------------------------------------

            st.subheader("🏥 Nearby Medical Centers")

            if len(hospitals) > 0:

                hospital_df = pd.DataFrame(hospitals)

                st.dataframe(
                    hospital_df,
                    use_container_width=True
                )

            else:

                st.warning("No nearby hospitals found.")

st.markdown("---")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.caption("""
OpenStreetMap-powered nearby hospital finder.

Educational and research-use platform only.
""")
