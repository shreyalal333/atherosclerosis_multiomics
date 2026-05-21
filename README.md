# Multi-Omics Early Biomarker Detection of Atherosclerosis
## Overview
This project focuses on the identification of early-stage biomarkers associated with atherosclerosis using a multi-omics computational framework integrating transcriptomics, metabolomics, and lifestyle-associated risk factors.
Differential gene expression analysis, machine learning-based feature selection, pathway enrichment analysis, and interactive visualization techniques were used to identify biologically significant molecular signatures associated with vascular inflammation and disease progression.
An interactive Streamlit dashboard was additionally developed to demonstrate biomarker-guided computational risk interpretation.

---
## Objectives

- Identify early transcriptomic biomarkers associated with atherosclerosis
- Analyze metabolomic alterations linked to disease progression
- Perform pathway enrichment analysis for biological interpretation
- Develop a multi-omics risk interpretation framework
- Create an interactive Streamlit-based visualization platform

---
## Technologies Used

- Python
- Google Colab
- Streamlit
- Pandas
- Scikit-learn
- GEO2R
- Plotly
- Matplotlib
- Seaborn

---
## Datasets Used

### Transcriptomics
Public GEO microarray datasets containing early vs advanced atherosclerotic plaque samples.

### Metabolomics
Public metabolomics datasets associated with cardiovascular disease progression.

### Lifestyle Data
Hospital-derived lifestyle-associated risk factor dataset including smoking, BMI, exercise, sleep, cholesterol, and diabetes-related parameters.

---
## Workflow

```text
Public Omics Datasets
        ↓
Preprocessing
        ↓
Differential Expression Analysis
        ↓
Machine Learning Feature Selection
        ↓
Biomarker Identification
        ↓
Pathway Enrichment Analysis
        ↓
Risk Scoring Framework
        ↓
Interactive Streamlit Dashboard
