import streamlit as st

#Application title
st.title('Simple twitter app')

#Text input
post_content = st.text_input('Please input your post content')

#Post button
st.button('Post')