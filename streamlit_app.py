import streamlit
import requests
import snowflake.connector
import pandas 
from urllib.error import URLError

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


def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return (fruityvice_normalized)
  
streamlit.header('Fruityvice Fruit Advice!')

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
      back_from_function = get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()



#import snowflake.connector



streamlit.header("The fruit load list contains:")
#Snowflake-related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()
 #Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)
  
 #ALLOW THE END USER TO ADD A FRUIT TO THE LIST 
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('" + new_fruit + "')")
    return "Thanks for adding " + new_fruit
  
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.text(back_from_function)

    #Add second button 
    
streamlit.title("View Our Fruit List - Add Your Favorites!")
if streamlit.button('Get Fruit List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)



