import streamlit as st
import numpy as np

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Tip Prediction App",
    page_icon="💰",
    layout="wide"
)

# -----------------------------
# Model Parameters
# -----------------------------
weights = np.array([0.14031483,0.0289143,0.00572452, 0.00871451, 0.00154012 ,0.0031881,
 0.00407141, 0.00787181]
)
bias = 0.01205207459282555


# -----------------------------
# Title Section
# -----------------------------
st.title(" Tip Prediction App")
st.write("Predict restaurant tips using **Linear Regression From Scratch**")

st.divider()


# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.header("Enter Customer Details")

total_bill = st.sidebar.number_input(
    "Total Bill ($)",
    min_value=0.0,
    value=20.0
)

size = st.sidebar.number_input(
    "Party Size",
    min_value=1,
    value=2
)

sex = st.sidebar.selectbox(
    "Sex",
    ["Male", "Female"]
)

smoker = st.sidebar.selectbox(
    "Smoker",
    ["Yes", "No"]
)

day = st.sidebar.selectbox(
    "Day",
    ["Thur", "Fri", "Sat", "Sun"]
)

time = st.sidebar.selectbox(
    "Time",
    ["Lunch", "Dinner"]
)


# -----------------------------
# Feature Encoding
# -----------------------------
sex_Female = 1 if sex == "Female" else 0
smoker_No = 1 if smoker == "No" else 0
day_Fri = 1 if day == "Fri" else 0
day_Sat = 1 if day == "Sat" else 0
day_Sun = 1 if day == "Sun" else 0
time_Dinner = 1 if time == "Dinner" else 0


# Feature vector
X = np.array([
    total_bill,
    size,
    sex_Female,
    smoker_No,
    day_Fri,
    day_Sat,
    day_Sun,
    time_Dinner
], dtype=float)


# -----------------------------
# Prediction Section
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("Predict Tip 💡"):

        prediction = np.dot(X, weights) + bias

        st.success(f"### Predicted Tip: ${prediction:.2f}")

with col2:
    st.info("""
    **Model Information**

    This model predicts the restaurant tip using:
    
    - Total Bill
    - Party Size
    - Customer Gender
    - Smoking Status
    - Day of Visit
    - Meal Time
    
    Built using **Linear Regression from Scratch**.
    """)


st.divider()

st.caption("Built with Python, NumPy and Streamlit")