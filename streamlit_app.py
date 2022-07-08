import streamlit
import snowflake.connector
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

import pandas

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

streamlit.text(fruityvice_response.json())

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)



