import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# ---------------------------------------------------
# LOAD DATASETS
# ---------------------------------------------------

excel_file = "multiomics_scores.xlsx"

gene_df = pd.read_excel(
    excel_file,
    sheet_name="Transcriptomics score"
)

met_df = pd.read_excel(
    excel_file,
    sheet_name="Metabolomics score"
)

life_df = pd.read_excel(
    excel_file,
    sheet_name="Lifestyle score"
)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("🫀 Multi-Omics Based Early Atherosclerosis Framework")

st.image(
    "https://images.unsplash.com/photo-1628348068343-c6a848d2b6dd?q=80&w=1200&auto=format&fit=crop",
    use_container_width=True
)

st.markdown("""
This framework integrates:
- Transcriptomic biomarkers
- Metabolomic signatures
- Lifestyle-associated risk factors
""")

st.markdown("---")

# ---------------------------------------------------
# COMPUTE RISKS
# ---------------------------------------------------

gene_mean = gene_df["Gene_score"].mean()
gene_min = gene_df["Gene_score"].min()
gene_max = gene_df["Gene_score"].max()

base_gene_risk = (
    (gene_mean - gene_min) /
    (gene_max - gene_min)
) * 0.3

met_mean = met_df["Metabolite_score"].mean()
met_min = met_df["Metabolite_score"].min()
met_max = met_df["Metabolite_score"].max()

base_met_risk = (
    (met_mean - met_min) /
    (met_max - met_min)
) * 0.2

# ---------------------------------------------------
# SIDEBAR INPUTS
# ---------------------------------------------------

st.sidebar.header("🧍 Lifestyle Inputs")

smoking = st.sidebar.selectbox(
    "Smoking Habit",
    ["No", "Occasional", "Frequent"]
)

exercise = st.sidebar.selectbox(
    "Exercise Frequency",
    ["Regular", "Sometimes", "Rare"]
)

diet = st.sidebar.selectbox(
    "Diet Quality",
    ["Healthy", "Moderate", "Poor"]
)

sleep = st.sidebar.slider(
    "Sleep Hours",
    3, 10, 7
)

bmi = st.sidebar.slider(
    "BMI",
    15.0, 40.0, 24.0
)

cholesterol = st.sidebar.slider(
    "Cholesterol Level",
    100, 350, 180
)

diabetes = st.sidebar.selectbox(
    "Diabetes",
    ["No", "Yes"]
)

# ---------------------------------------------------
# LIFESTYLE SCORE
# ---------------------------------------------------

personal_lifestyle = 0

if smoking == "Frequent":
    personal_lifestyle += 3
elif smoking == "Occasional":
    personal_lifestyle += 1

if exercise == "Rare":
    personal_lifestyle += 3
elif exercise == "Sometimes":
    personal_lifestyle += 1

if diet == "Poor":
    personal_lifestyle += 3
elif diet == "Moderate":
    personal_lifestyle += 1

if sleep < 6:
    personal_lifestyle += 2

if bmi > 30:
    personal_lifestyle += 3
elif bmi > 25:
    personal_lifestyle += 1

if cholesterol > 240:
    personal_lifestyle += 3
elif cholesterol > 200:
    personal_lifestyle += 1

if diabetes == "Yes":
    personal_lifestyle += 3

personal_lifestyle = personal_lifestyle / 15

# ---------------------------------------------------
# FINAL RISKS
# ---------------------------------------------------

gene_risk = (
    base_gene_risk *
    (1 + personal_lifestyle)
)

met_risk = (
    base_met_risk *
    (1 + (0.8 * personal_lifestyle))
)

overall_risk = (
    gene_risk +
    met_risk +
    (0.7 * personal_lifestyle)
)

# ---------------------------------------------------
# RISK LABEL
# ---------------------------------------------------

if overall_risk < 0.40:
    risk_label = "LOW RISK"
    risk_color = "green"

elif overall_risk < 0.65:
    risk_label = "MODERATE RISK"
    risk_color = "orange"

else:
    risk_label = "HIGH RISK"
    risk_color = "red"

# ---------------------------------------------------
# METRICS
# ---------------------------------------------------

st.header("📊 Integrated Risk Summary")

m1, m2, m3 = st.columns(3)

m1.metric("Transcriptomic Risk", f"{gene_risk:.2f}")
m2.metric("Metabolomic Risk", f"{met_risk:.2f}")
m3.metric("Lifestyle Risk", f"{personal_lifestyle:.2f}")

# ---------------------------------------------------
# GAUGE
# ---------------------------------------------------

gauge_fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=float(overall_risk),
    title={'text': "Integrated Risk Score"},
    gauge={
        'axis': {'range': [0, 1]},
        'bar': {'color': risk_color}
    }
))

st.plotly_chart(gauge_fig, use_container_width=True)

st.markdown(
    f"<h2 style='color:{risk_color};'>{risk_label}</h2>",
    unsafe_allow_html=True
)

# ---------------------------------------------------
# BAR CHART
# ---------------------------------------------------

omics_df = pd.DataFrame({
    "Omics Layer": [
        "Transcriptomics",
        "Metabolomics",
        "Lifestyle"
    ],
    "Risk Score": [
        gene_risk,
        met_risk,
        personal_lifestyle
    ]
})

bar_fig = px.bar(
    omics_df,
    x="Omics Layer",
    y="Risk Score",
    text="Risk Score"
)

st.plotly_chart(bar_fig, use_container_width=True)

# ---------------------------------------------------
# BIOMARKERS
# ---------------------------------------------------

st.header("🔬 Key Biomarkers")

biomarker_df = pd.DataFrame({
    "Biomarker": [
        "H2AFV",
        "CYTH4",
        "ADAP2",
        "SERPINA1",
        "JAK3"
    ],
    "Role": [
        "Chromatin regulation",
        "Immune signaling",
        "Cell signaling",
        "Inflammatory response",
        "Cytokine signaling"
    ]
})

st.dataframe(biomarker_df, use_container_width=True)
