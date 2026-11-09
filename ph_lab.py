
import streamlit as st
import matplotlib.pyplot as plt

def show_ph_lab():

    st.title("🧪 Virtual pH Testing Lab")

    st.write(
        "Explore acids, bases and neutral solutions "
        "using a virtual pH experiment."
    )

    solutions = {
        "Lemon Juice": 2,
        "Vinegar": 3,
        "Orange Juice": 4,
        "Coffee": 5,
        "Milk": 6,
        "Pure Water": 7,
        "Baking Soda Solution": 8,
        "Soap Solution": 10,
        "Household Ammonia (simulation)": 11
    }

    selected = st.selectbox(
        "Choose a solution",
        list(solutions.keys())
    )

    ph = solutions[selected]

    if ph < 7:
        result = "Acidic"
        color = "red"
        indicator = "Red / Orange"
    elif ph == 7:
        result = "Neutral"
        color = "green"
        indicator = "Green"
    else:
        result = "Basic (Alkaline)"
        color = "blue"
        indicator = "Blue / Purple"

    st.subheader("Experiment Results")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("pH Value", ph)

    with col2:
        st.metric("Nature", result)

    st.markdown(
        f"### Indicator colour: :{color}[{indicator}]"
    )

    fig, ax = plt.subplots(figsize=(9, 1.5))

    ax.barh(
        ["pH Scale"],
        [ph],
        color=color,
        height=0.5
    )

    ax.set_xlim(0, 14)
    ax.set_xticks(range(15))
    ax.set_xlabel("pH Value")
    ax.set_title("pH Measurement")

    st.pyplot(fig)
    plt.close(fig)

    st.info(
        f"{selected} is classified as {result} "
        f"in this educational simulation."
    )

    with st.expander("Learn the science"):
        st.write("""
        - pH below 7: Acidic
        - pH equal to 7: Neutral
        - pH above 7: Basic

        The pH scale generally ranges from 0 to 14.
        """)

    st.subheader("Test Your Knowledge")

    question = st.radio(
        "What is the pH of a neutral solution?",
        ["3", "5", "7", "10"],
        key="ph_quiz"
    )

    if st.button("Check Answer"):
        if question == "7":
            st.success("Correct! A neutral solution has pH 7.")
        else:
            st.error("Try again! Remember that neutral pH is 7.")
