import streamlit as st

langnu = st.Page("pages/01-langnu.py", title="Mapping làng Nủ", icon="🛖")
home = st.Page("home.py", title="Dự án Yagimapping Việt Nam", icon="🌪️")
pg = st.navigation([home,langnu])
pg.run()