
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
# COMPUTE BASELINE RISKS
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

baseline_life_risk = (
    life_df["Lifestyle_score"].mean() /
    life_df["Lifestyle_score"].max()
)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("🫀 Multi-Omics Based Early Atherosclerosis Framework")

st.markdown("""
This framework integrates:

- Transcriptomic biomarkers
- Metabolomic signatures
- Lifestyle-associated risk factors

to interpret biological signals related to
early atherosclerosis.
""")

st.markdown("---")

# ---------------------------------------------------
# SIDEBAR USER INPUTS
# ---------------------------------------------------

st.sidebar.header("🧍 Personalized Lifestyle Inputs")

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
# PERSONALIZED LIFESTYLE SCORE
# ---------------------------------------------------

personal_lifestyle = 0

# Smoking
if smoking == "Frequent":
    personal_lifestyle += 3
elif smoking == "Occasional":
    personal_lifestyle += 1

# Exercise
if exercise == "Rare":
    personal_lifestyle += 3
elif exercise == "Sometimes":
    personal_lifestyle += 1

# Diet
if diet == "Poor":
    personal_lifestyle += 3
elif diet == "Moderate":
    personal_lifestyle += 1

# Sleep
if sleep < 6:
    personal_lifestyle += 2

# BMI
if bmi > 30:
    personal_lifestyle += 3
elif bmi > 25:
    personal_lifestyle += 1

# Cholesterol
if cholesterol > 240:
    personal_lifestyle += 3
elif cholesterol > 200:
    personal_lifestyle += 1

# Diabetes
if diabetes == "Yes":
    personal_lifestyle += 3

# Normalize
personal_lifestyle = personal_lifestyle / 15

# ---------------------------------------------------
# FINAL LIFESTYLE RISK
# ---------------------------------------------------

final_lifestyle_risk = personal_lifestyle 
# Lifestyle dynamically affects omics

gene_risk = (
    base_gene_risk *
    (1 + final_lifestyle_risk)
)

met_risk = (
    base_met_risk *
    (1 + (0.8 * final_lifestyle_risk))
)


# ---------------------------------------------------
# OVERALL MULTI-OMICS RISK
# ---------------------------------------------------

overall_risk = (
    gene_risk +
    met_risk +
    (0.7 * final_lifestyle_risk)
)
# ---------------------------------------------------
# RISK CATEGORY
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
# DATASET OVERVIEW
# ---------------------------------------------------

st.header("📂 Dataset Overview")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Transcriptomics Samples",
    len(gene_df)
)

c2.metric(
    "Metabolomics Samples",
    len(met_df)
)

c3.metric(
    "Lifestyle Samples",
    len(life_df)
)

st.markdown("---")

# ---------------------------------------------------
# RISK SUMMARY
# ---------------------------------------------------

st.header("📊 Integrated Risk Summary")

m1, m2, m3 = st.columns(3)

m1.metric(
    "Transcriptomic Risk",
    f"{gene_risk:.2f}"
)

m2.metric(
    "Metabolomic Risk",
    f"{met_risk:.2f}"
)

m3.metric(
    "Lifestyle Risk",
    f"{final_lifestyle_risk:.2f}"
)

# ---------------------------------------------------
# GAUGE CHART
# ---------------------------------------------------

st.subheader("🧭 Overall Risk Gauge")

gauge_fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=float(overall_risk),
    title={'text': "Integrated Risk Score"},
    gauge={
        'axis': {'range': [0, 1]},
        'bar': {'color': risk_color},
        'steps': [
            {'range': [0, 0.33], 'color': "lightgreen"},
            {'range': [0.33, 0.66], 'color': "gold"},
            {'range': [0.66, 1], 'color': "salmon"}
        ]
    }
))

st.plotly_chart(gauge_fig, use_container_width=True)

st.markdown(
    f"<h2 style='color:{risk_color};'>{risk_label}</h2>",
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------------------------------------------
# RADAR CHART
# ---------------------------------------------------

st.header("📈 Multi-Omics Risk Profile")

radar_categories = [
    "Transcriptomics",
    "Metabolomics",
    "Lifestyle"
]

radar_values = [
    gene_risk,
    met_risk,
    final_lifestyle_risk
]

radar_fig = go.Figure()

radar_fig.add_trace(go.Scatterpolar(
    r=radar_values,
    theta=radar_categories,
    fill='toself'
))

radar_fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 1]
        )
    ),
    showlegend=False
)

st.plotly_chart(radar_fig, use_container_width=True)

# ---------------------------------------------------
# OMICS CONTRIBUTION PLOT
# ---------------------------------------------------

st.header("📊 Omics Contribution Plot")

omics_df = pd.DataFrame({
    "Omics Layer": [
        "Transcriptomics",
        "Metabolomics",
        "Lifestyle"
    ],
    "Risk Score": [
        gene_risk,
        met_risk,
        final_lifestyle_risk
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
# HEATMAP
# ---------------------------------------------------

st.header("🔥 Integrated Risk Heatmap")

heatmap_df = pd.DataFrame({
    "Transcriptomics": [gene_risk],
    "Metabolomics": [met_risk],
    "Lifestyle": [final_lifestyle_risk]
})

heatmap_fig = px.imshow(
    heatmap_df,
    text_auto=True,
    aspect="auto"
)

st.plotly_chart(
    heatmap_fig,
    use_container_width=True
)

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
    "Biological Role": [
        "Chromatin regulation",
        "Immune signaling",
        "Cell signaling",
        "Inflammatory response",
        "Cytokine signaling"
    ]
})

st.dataframe(
    biomarker_df,
    use_container_width=True
)

# ---------------------------------------------------
# PATHWAY INTERPRETATION
# ---------------------------------------------------

st.header("🧬 Biological Pathway Interpretation")

st.info("""
### Significant pathways identified

• Complement activation  
• Acute inflammatory response  
• B-cell receptor signaling  
• Immune signaling pathways  
• Vascular inflammatory mechanisms  

These pathways indicate inflammatory
and immune-associated molecular
signatures involved in atherosclerosis.
""")

st.markdown("---")

# ---------------------------------------------------
# RECOMMENDATIONS
# ---------------------------------------------------

st.header("💡 Personalized Recommendations")

recommendations = []

if smoking != "No":
    recommendations.append("Reduce smoking")

if exercise != "Regular":
    recommendations.append("Increase physical activity")

if diet != "Healthy":
    recommendations.append("Improve dietary quality")

if sleep < 6:
    recommendations.append("Improve sleep duration")

if cholesterol > 200:
    recommendations.append("Monitor cholesterol levels")

if bmi > 25:
    recommendations.append("Maintain healthy BMI")

if diabetes == "Yes":
    recommendations.append("Monitor blood glucose regularly")

if len(recommendations) == 0:

    st.success("""
    Current lifestyle profile appears favorable.
    """)

else:

    for rec in recommendations:
        st.write("✅", rec)

# ---------------------------------------------------
# AI INTERPRETATION
# ---------------------------------------------------

st.header("🧠 AI-Based Interpretation")

if risk_label == "LOW RISK":

    st.success("""
    Integrated biological signals suggest
    relatively low atherosclerotic activity.
    """)

elif risk_label == "MODERATE RISK":

    st.warning("""
    Moderate inflammatory and metabolic
    signatures associated with early
    atherosclerotic progression detected.
    """)

else:

    st.error("""
    Elevated inflammatory and metabolic
    signatures associated with vascular
    dysfunction and plaque progression detected.
    """)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("---")

st.caption("""
Educational computational framework for
multi-omics-based early atherosclerosis
risk interpretation.

Not intended for clinical diagnosis.
""")
