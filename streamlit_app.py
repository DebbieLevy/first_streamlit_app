import streamlit
streamlit.title("My Mom's New Healthy Diner")
streamlit.header('BREAKFAST FAVORITES')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text("🥗Kale,Spinach & Rocket Smoothie")
streamlit.text('🥚Hard Boiled free range Egg')
streamlit.text('🥑Avocado Toast')
streamlit.header('🍌🍎 Create your own fruit Smoothie 🍑🍒')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
