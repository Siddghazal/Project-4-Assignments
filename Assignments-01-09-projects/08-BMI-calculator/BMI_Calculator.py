import streamlit as st

# Set app title
st.set_page_config(page_title="BMI Calculator", layout="centered")
st.title("🧮 BMI Calculator")

# User input
st.subheader("Enter your details:")
weight = st.number_input("Weight (kg)", min_value=1.0, step=0.1)
height = st.number_input("Height (cm)", min_value=1.0, step=0.1)

# Calculate BMI
if st.button("Calculate BMI"):
    height_m = height / 100  # convert cm to meters
    bmi = weight / (height_m ** 2)
    st.success(f"Your BMI is: **{bmi:.2f}**")

    # Interpret BMI
    if bmi < 18.5:
        st.warning("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.info("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")

# Footer
st.markdown("---")
st.caption("Created with ❤️ using Streamlit")
