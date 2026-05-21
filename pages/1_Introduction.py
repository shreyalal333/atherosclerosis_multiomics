import streamlit as st

st.title("🧬 Understanding Atherosclerosis")

st.image(
    "https://images.unsplash.com/photo-1584515933487-779824d29309?q=80&w=1200&auto=format&fit=crop",
    use_container_width=True
)

st.markdown("---")

st.header("What is Atherosclerosis?")

st.markdown("""
Atherosclerosis is a chronic cardiovascular disease where fatty deposits,
cholesterol, inflammatory cells, and fibrous materials accumulate inside arteries.

These plaques narrow blood vessels and reduce blood flow,
leading to serious cardiovascular complications.
""")

st.markdown("---")

st.header("⚠️ Why Early Detection Matters")

st.markdown("""
Early atherosclerosis develops silently without obvious symptoms.

Early detection helps:
- Prevent plaque progression
- Reduce heart attack risk
- Improve treatment outcomes
- Enable personalized medicine approaches
""")

st.markdown("---")

st.header("🧬 Multi-Omics Approach")

st.markdown("""
This platform combines:

### Transcriptomics
Gene expression changes linked to inflammation.

### Metabolomics
Metabolic signatures associated with cardiovascular disease.

### Lifestyle Data
Smoking, diet, exercise, BMI, cholesterol, and diabetes status.

Integrating these improves early risk interpretation.
""")

st.markdown("---")

st.header("🩺 Major Risk Factors")

risk_factors = [
    "Smoking",
    "High cholesterol",
    "Obesity",
    "Sedentary lifestyle",
    "Stress",
    "Poor diet",
    "Diabetes",
    "Hypertension"
]

for factor in risk_factors:
    st.write("✅", factor)

st.markdown("---")

st.success("Early intervention significantly reduces cardiovascular risk.")
