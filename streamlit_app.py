import streamlit

streamlit.title('La Fea Bistro')

streamlit.header('Dinner Menu')

streamlit.header('Appetizers')
streamlit.text('🥗 Speacialty Salad')

streamlit.header('Entrees')
streamlit.text('🥣 Chefs Choice')

streamlit.header('Desserts')
streamlit.text('🥭 Chefs Choice')

streamlit.header('Drink Menu')
streamlit.text('🍇 Chefs Choice Red Wine')
streamlit.text('🍇 Chefs Choice White Wine')
streamlit.text('🥃 Chefs Choice Bourbon')

import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

