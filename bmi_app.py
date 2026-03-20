import streamlit as st

st.title('BMI Calculator')
st.write('Enter your height and weight below to calculate your BMI.')

st.divider()

height = st.number_input('Height (cm)', min_value=100, max_value=250, value=170, step=1)
weight = st.number_input('Weight (kg)', min_value=30, max_value=200, value=70, step=1)

st.divider()

if st.button('Calculate BMI', use_container_width=True):

    # Calculate
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    # Display BMI
    st.subheader(f'Your BMI is {bmi:.1f}')

    # Progress bar as visual indicator
    bmi_normalised = min(bmi / 40, 1.0)
    st.progress(bmi_normalised)

    st.divider()

    # Colour coded result
    if bmi < 18.5:
        st.warning('Underweight — consider eating more nutritious meals')
    elif bmi < 25:
        st.success('Normal weight — great job keeping healthy')
    elif bmi < 30:
        st.warning('Overweight — consider more physical activity')
    else:
        st.error('Obese — please consult a doctor for guidance')

    st.divider()

    # Summary columns
    col1, col2, col3 = st.columns(3)
    col1.metric('Height', f'{height} cm')
    col2.metric('Weight', f'{weight} kg')
    col3.metric('BMI', f'{bmi:.1f}')

st.divider()
st.caption('BMI Calculator — built with Streamlit')
