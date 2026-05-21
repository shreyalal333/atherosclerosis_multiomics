import streamlit as st

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Multi-Omics Atherosclerosis Platform",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# CUSTOM STYLING
# ---------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f8fbff;
}

h1, h2, h3 {
    color: #8B0000;
}

.stMetric {
    background-color: white;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
}

[data-testid="stSidebar"] {
    background-color: #f0f6ff;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HERO SECTION
# ---------------------------------------------------

st.title("🫀 Multi-Omics Atherosclerosis Platform")

st.markdown("""
## AI-Powered Early Atherosclerosis Risk Interpretation

This platform integrates:

- 🧬 Transcriptomics
- 🧪 Metabolomics
- 🧍 Lifestyle Risk Factors
- 🤖 AI-Based Interpretation

to identify biological and lifestyle-associated
signals linked with early atherosclerosis progression.
""")

st.image(
    "https://images.unsplash.com/photo-1576091160550-2173dba999ef?q=80&w=1400&auto=format&fit=crop",
    use_container_width=True
)

# ---------------------------------------------------
# OVERVIEW
# ---------------------------------------------------

st.markdown("---")

st.header("📌 Platform Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    ### 🧬 Introduction

    Learn:
    - What atherosclerosis is
    - Why early detection matters
    - Major cardiovascular risk factors
    """)

with col2:
    st.success("""
    ### 📊 Risk Dashboard

    Analyze:
    - Transcriptomic risk
    - Metabolomic risk
    - Lifestyle-associated risk
    """)

with col3:
    st.warning("""
    ### ❤️ Prevention & Doctors

    Explore:
    - Prevention strategies
    - Healthy lifestyle tips
    - Nearby cardiologists
    """)

# ---------------------------------------------------
# MULTI-OMICS EXPLANATION
# ---------------------------------------------------

st.markdown("---")

st.header("🧬 What is Multi-Omics?")

st.markdown("""
Multi-omics integrates multiple biological data layers
to improve disease understanding and early risk prediction.

### Omics Layers Used

| Omics Layer | Purpose |
|---|---|
| Transcriptomics | Gene expression analysis |
| Metabolomics | Metabolic pathway interpretation |
| Lifestyle Data | Behavioral risk assessment |

Combining these layers provides a systems-level understanding
of cardiovascular disease progression.
""")

# ---------------------------------------------------
# FEATURES
# ---------------------------------------------------

st.markdown("---")

st.header("✨ Key Features")

features = [
    "Integrated multi-omics risk analysis",
    "AI-based cardiovascular interpretation",
    "Interactive visual analytics",
    "Lifestyle-associated risk assessment",
    "Biomarker exploration",
    "Personalized recommendations",
    "Nearby cardiologist finder",
    "Clinical-style dashboard interface"
]

for feature in features:
    st.write("✅", feature)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("🫀 Navigation")

st.sidebar.info("""
Use the sidebar pages to navigate through the platform.

### Pages
- Introduction
- Risk Dashboard
- Prevention & Doctors
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
