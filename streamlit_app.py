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
streamlit.dataframe(my_fruit_list)
