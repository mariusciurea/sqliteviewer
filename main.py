"""main module - home page for streamlit"""

import streamlit as st
from database import Database

st.title('sqlite viewer')

file = st.file_uploader('your db here')


if file:
    file_1 = file.getvalue()
    with open('data.db', 'wb') as fw:
        fw.write(file_1)
    query_command = st.text_input('Write your SQL command here')
    db = Database('data.db')

    tables = db.get_tables()

    option = st.selectbox(label='SQL Tables', options=[item[0] for item in tables])

    query = st.button('Query all')

    if query:
        df = db.get_df(option)
        st.table(df)

    try:
        query_info = db.query()
    except Exception:
        st.error('Cannot fetch data!')