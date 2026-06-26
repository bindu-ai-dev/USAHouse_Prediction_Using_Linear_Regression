import streamlit as st
import pandas as pd
import joblib

# --------------------------
# Page Configuration
# --------------------------
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏡",
    layout="wide"
)

# --------------------------
# Load Model
# --------------------------
model = joblib.load("house_model.pkl")

# --------------------------
# Header
# --------------------------
st.title("🏡 House Price Prediction System")

st.markdown("""
Predict the estimated price of a house using **Machine Learning**.

This application uses a **Linear Regression** model trained on the **USA Housing Dataset**.
""")

st.markdown("---")

# --------------------------
# Sidebar
# --------------------------

st.sidebar.header("🏠 Enter House Details")

income = st.sidebar.number_input(
    "Average Area Income ($)",
    min_value=10000.0,
    max_value=150000.0,
    value=70000.0,
    step=1000.0
)

house_age = st.sidebar.number_input(
    "Average Area House Age (Years)",
    min_value=1.0,
    max_value=10.0,
    value=5.0,
    step=0.1
)

rooms = st.sidebar.number_input(
    "Average Area Number of Rooms",
    min_value=2.0,
    max_value=12.0,
    value=7.0,
    step=0.1
)

bedrooms = st.sidebar.number_input(
    "Average Area Number of Bedrooms",
    min_value=1.0,
    max_value=10.0,
    value=4.0,
    step=0.1
)

population = st.sidebar.number_input(
    "Area Population",
    min_value=1000.0,
    max_value=100000.0,
    value=30000.0,
    step=100.0
)

# --------------------------
# Input Summary
# --------------------------

st.subheader("📋 House Details")

input_df = pd.DataFrame({
    "Feature": [
        "Average Area Income",
        "Average Area House Age",
        "Average Number of Rooms",
        "Average Number of Bedrooms",
        "Area Population"
    ],
    "Value": [
        income,
        house_age,
        rooms,
        bedrooms,
        population
    ]
})

st.dataframe(input_df, use_container_width=True)

# --------------------------
# Prediction
# --------------------------

if st.button("🏡 Predict House Price"):

    input_data = pd.DataFrame(
        [[income,
          house_age,
          rooms,
          bedrooms,
          population]],

        columns=[
            "Avg. Area Income",
            "Avg. Area House Age",
            "Avg. Area Number of Rooms",
            "Avg. Area Number of Bedrooms",
            "Area Population"
        ]
    )

    prediction = model.predict(input_data)

    st.success("Prediction Completed Successfully!")

    st.metric(
        "Estimated House Price",
        f"${prediction[0]:,.2f}"
    )

# --------------------------
# Information
# --------------------------

st.markdown("---")

st.subheader("📊 Features Used")

st.write("""
- Average Area Income
- Average Area House Age
- Average Area Number of Rooms
- Average Area Number of Bedrooms
- Area Population
""")

st.subheader("🤖 Machine Learning Model")

st.write("""
- Algorithm: Linear Regression
- Dataset: USA Housing Dataset
- Problem Type: Regression
""")

st.info(
    "Note: This prediction is based only on the numerical features available in the USA Housing dataset. The Address column is not used because it contains text values and was excluded during model training."
)

st.markdown("---")

st.caption("Developed by Bindu | QSkill AI & Machine Learning Internship")