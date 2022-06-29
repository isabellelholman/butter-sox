import streamlit

from Downloads import ('La_Fea_Bistro.jpg')
image = Image.open('La_Fea_Bistro.jpg')

st.image(image, caption='La Fea Bistro')

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


