from random import randrange

import streamlit as st

st.title('Food Close to Campus')

restaurants = []
info_names = ["name", "location", "phone number", "website"]


with open('restaurants.txt') as f:
    lines = f.readlines()

for restaurant in lines:
    restaurant_info = restaurant.split('—')
    info = {}
    for i, information in enumerate(restaurant_info):
        info[info_names[i]] = information
    
    restaurants.append(info)


if st.button('Go!'):
    restaurant = restaurants[randrange(len(restaurants))]
    for info_name in restaurant:
        st.write(restaurant[info_name])
