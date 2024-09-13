import streamlit as st
import leafmap.foliumap as leafmap


st.title("Mapping lang Nu")


m = leafmap.Map(height=600, center=[22.25, 104.5], zoom=12)
url = "https://github.com/kaheetonaa/Yagimapping/raw/main/Case01-LangNu/langnu-geo-fixed.tif"
#104,52751/22,15154

m.split_map(left_layer=url, right_layer="Esri.WorldImagery", zoom_control=False)

m.to_streamlit(height=600)