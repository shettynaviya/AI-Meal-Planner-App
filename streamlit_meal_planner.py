import streamlit as st
import pandas as pd
import openai
import random
import time
from data import food_items_breakfast, food_items_lunch, food_items_dinner

example_response = """
This is just an example but use your creativity: You can start with, 
Hello {name}! I'm thrilled to be your meal planner for the day, and I've crafted 
a delightful and flavorful meal plan just for you. But fear not, this isn't your ordinary, 
run-of-the-mill meal plan. It's a culinary adventure designed to keep your taste buds excited 
while considering the calories you can intake. So, get ready!
"""

# Access API keys from secrets.toml
openai.api_key = st.secrets["openai_apikey"]

UNITS_CM_TO_IN = 0.393701
UNITS_KG_TO_LB = 2.20462
UNITS_LB_TO_KG = 1 / UNITS_KG_TO_LB
UNITS_IN_TO_CM = 1 / UNITS_CM_TO_IN

st.set_page_config(page_title="AI - Meal Planner", page_icon="🍴")

st.title("AI Meal Planner")
st.divider()

st.write(
    "This is an AI-based meal planner that uses a person's information. The planner can be used to find a meal plan that satisfies the user's calorie and macronutrient requirements.")
st.markdown("*Powered by OpenAI's GPT model*")

st.divider()

st.write("Enter your information:")
name = st.text_input("Enter your name")
age = st.number_input("Enter your age", step=1)

unit_preference = st.radio("Preferred units:", ["Metric (kg, cm)", "Imperial (lb, ft + in)"])

if unit_preference == "Metric (kg, cm)":
    weight = st.number_input("Enter your weight (kg)")
    height = st.number_input("Enter your height (cm)")
else:
    weight_lb = st.number_input("Enter your weight (lb)")
    col1, col2 = st.columns(2)
    with col1:
        height_ft = st.number_input("Enter your height (ft)")
    with col2:
        height_in = st.number_input("Enter your height (in)")

    weight = weight_lb * UNITS_LB_TO_KG
    height = (height_ft * 12 + height_in) * UNITS_IN_TO_CM

gender = st.radio("Choose your gender:", ["Male", "Female"])

def calculate_bmr(weight, height, age, gender):
    if gender == "Male":
        bmr = 9.99 * weight + 6.25 * height - 4.92 * age + 5
    else:
        bmr = 9.99 * weight + 6.25 * height - 4.92 * age - 161
    return bmr

def knapsack(target_calories, food_groups):
    items = []
    for group, foods in food_groups.items():
        for item, calories in foods.items():
            items.append((calories, item))

    n = len(items)
    dp = [[0 for _ in range(target_calories + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(target_calories + 1):
            value, _ = items[i - 1]
            if value > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - value] + value)

    selected_items = []
    j = target_calories
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            _, item = items[i - 1]
            selected_items.append(item)
            j -= items[i - 1][0]

    return selected_items, dp[n][target_calories]

bmr = calculate_bmr(weight, height, age, gender)
round_bmr = round(bmr, 2)
st.subheader(f"Your daily intake needs to have: {round_bmr} calories")

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

st.button("Create a Basket", on_click=click_button)

if 'clicked' in st.session_state and st.session_state.clicked:
    # Calculate the calorie values and meal items after button click
    calories_breakfast = round((bmr * 0.5), 2)
    calories_lunch = round((bmr * (1 / 3)), 2)
    calories_dinner = round((bmr * (1 / 6)), 2)

    meal_items_morning, cal_m = knapsack(int(calories_breakfast), food_items_breakfast)
    meal_items_lunch, cal_l = knapsack(int(calories_lunch), food_items_lunch)
    meal_items_dinner, cal_d = knapsack(int(calories_dinner), food_items_dinner)

    st.header("Your Personalized Meal Plan")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Calories for Morning: " + str(calories_breakfast))
        st.dataframe(pd.DataFrame({"Morning": meal_items_morning}))
        st.write("Total Calories: " + str(cal_m))

    with col2:
        st.write("Calories for Lunch: " + str(calories_lunch))
        st.dataframe(pd.DataFrame({"Lunch": meal_items_lunch}))
        st.write("Total Calories: " + str(cal_l))

    with col3:
        st.write("Calories for Dinner: " + str(calories_dinner))
        st.dataframe(pd.DataFrame({"Dinner": meal_items_dinner}))
        st.write("Total Calories: " + str(cal_d))

# Hide Streamlit branding
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
footer:after {
    content: 'Built by Naviya and Anuja';
    visibility: visible;
    display: block;
    position: relative;
    padding: 15px;
    top: 2px;
}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
