import streamlit as st

# ===================== HEADER =====================
st.title("⚙️ Mechanical Unit Converter & Density Checker")

st.markdown("### 👤 HAFIZ MUNSARIM BUTT")
st.markdown("### 🎓 Roll Number: 25-ME-91")

st.divider()

# ===================== MENU =====================
option = st.sidebar.selectbox(
    "Select Tool",
    ["Unit Converter", "Density Checker"]
)

# ===================== UNIT CONVERTER =====================
if option == "Unit Converter":
    st.subheader("🔄 Unit Converter")

    unit = st.selectbox(
        "Select Quantity",
        ["Force (N → kN)", "Pressure (Pa → MPa)", "Energy (J → kJ)"]
    )

    value = st.number_input("Enter Value", min_value=0.0)

    if st.button("Convert"):
        if unit == "Force (N → kN)":
            result = value / 1000
            st.success(f"{value} N = {result} kN")

        elif unit == "Pressure (Pa → MPa)":
            result = value / 1_000_000
            st.success(f"{value} Pa = {result} MPa")

        elif unit == "Energy (J → kJ)":
            result = value / 1000
            st.success(f"{value} J = {result} kJ")


# ===================== DENSITY CHECKER =====================
elif option == "Density Checker":
    st.subheader("📦 Material Density Checker")

    mass = st.number_input("Enter Mass (kg)", min_value=0.0)
    volume = st.number_input("Enter Volume (m³)", min_value=0.0)

    if st.button("Calculate Density"):
        if volume == 0:
            st.error("Volume cannot be zero!")
        else:
            density = mass / volume
            st.success(f"Density = {density} kg/m³")
