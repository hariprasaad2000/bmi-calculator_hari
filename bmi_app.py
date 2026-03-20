import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title('BMI Calculator')
st.write('Enter your height and weight below to calculate your BMI.')

st.divider()

height = st.number_input('Height (cm)', min_value=100, max_value=250, value=170, step=1)
weight = st.number_input('Weight (kg)', min_value=30, max_value=200, value=70, step=1)

st.divider()

def draw_gauge(bmi):
    fig, ax = plt.subplots(figsize=(8, 4), subplot_kw={'projection': 'polar'})

    # Background zones
    zones = [
        (0, 18.5, '#d6eaf8', 'Underweight'),
        (18.5, 25, '#d5f5e3', 'Normal'),
        (25, 30, '#fdebd0', 'Overweight'),
        (30, 40, '#fadbd8', 'Obese')
    ]

    for start, end, color, label in zones:
        theta_start = np.pi * (1 - start / 40)
        theta_end = np.pi * (1 - end / 40)
        ax.barh(1, theta_start - theta_end, left=theta_end,
                height=0.5, color=color, edgecolor='white')

    # Needle
    bmi_clamped = min(max(bmi, 0), 40)
    needle_angle = np.pi * (1 - bmi_clamped / 40)
    ax.annotate('', xy=(needle_angle, 0.9),
                xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='black', lw=2))

    # BMI value in centre
    ax.text(0, 0, f'{bmi:.1f}', ha='center', va='center',
            fontsize=20, fontweight='bold')

    ax.set_ylim(0, 1.5)
    ax.set_theta_zero_location('W')
    ax.set_theta_direction(-1)
    ax.axis('off')

    fig.patch.set_facecolor('none')
    return fig

if st.button('Calculate BMI', use_container_width=True):

    # Calculate
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    # Gauge
    fig = draw_gauge(bmi)
    st.pyplot(fig)

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
```

---

Also update your `requirements.txt` to just:
```
streamlit
matplotlib
numpy
