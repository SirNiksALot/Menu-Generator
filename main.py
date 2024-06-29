import streamlit as st
import langchain_helper
st.title("Menu generator , type in your cuisine now!")
cuisine=st.sidebar.selectbox("Pick a cuisine",
                    ("Indian","Italian","Mexican","Chinese"))
response=langchain_helper.get_response(cuisine)
st.header(response['restaurant_name'])

items=response['menu_items'].split(",")
for item in items:
    if item:
        print(item)
        st.write(item).strip()
