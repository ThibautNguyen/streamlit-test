import streamlit as st

st.set_page_config(
    page_title='Metadata Manager',
    page_icon='??',
    layout='wide'
)

st.title('Metadata Management System')
st.write('Welcome to the metadata management application!')

col1, col2 = st.columns(2)

with col1:
    st.info('### ?? Metadata Entry')
    st.write('Create and modify metadata records easily.')
    st.page_link('pages/entry.py', label='Go to Entry Form', icon='??')

with col2:
    st.info('### ?? Search')
    st.write('Search through existing metadata records.')
    st.page_link('pages/search.py', label='Go to Search', icon='??')

st.markdown('---')
st.write('? 2025 - Metadata Management App v1.0')

