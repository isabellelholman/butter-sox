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

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
 
import requests

fruityvice_repsonse = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

fruityvice_normalized = json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
