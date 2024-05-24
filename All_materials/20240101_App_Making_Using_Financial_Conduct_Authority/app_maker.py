import streamlit as st

#st.write('Enter institution')
x = st.text_input('Enter institution')

if st.button("Click Me"):
    st.write(f"Your favorite movie is `{x}`")