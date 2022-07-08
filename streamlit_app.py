import streamlit

streamlit.header('LA FEA BISTRO')

streamlit.header('Dinner Menu')

streamlit.subheader('Appetizers')
streamlit.text('🧀 Charcuterie Board 🍓')

streamlit.subheader('Entrees')
streamlit.text('🥣 Chefs Choice 👨‍🍳')

streamlit.header('Drink Menu')
streamlit.text('🍇 Chefs Choice Red Wine')
streamlit.text('🥂 Chefs Choice White Wine')
streamlit.text('🍾 Chefs Choice Champagne')
streamlit.text('🥃 Chefs Choice Bourbon')

streamlit.header('Dessert Menu')
streamlit.text('🍨 Chefs Choice')

streamlit.header('Fruityvice Fruit Advice!')
 
import requests

fruityvice_repsonse = requests.get("https://fruityvice.com/api/fruit/kiwi")

fruityvice_normalized = json_normalize(fruityvice_normalized.json())
streamlit.dataframe(fruityvice_normalized)
