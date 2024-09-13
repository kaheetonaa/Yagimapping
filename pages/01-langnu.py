import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd


st.title("Mapping lang Nu")


m = leafmap.Map(height=600, center=[22.25, 104.5], zoom=12)

m.add_basemap("HYBRID")

in_geojson = "https://github.com/kaheetonaa/Yagimapping/raw/main/Case01-LangNu/data/langnu-googleopenbuildings.geojson"
dataframe=gpd.read_file(in_geojson)

m.add_data(dataframe, layer_name="Cong trinh",categories=['No', 'Yes',None],colors=['white', 'red','gray'],column = "Destroy", legend_title='Cong trinh', labels=['Khong anh huong','Huy hoai','Chua xac dinh'],
        style = {
            "stroke": True,
            "color": "gray",
            "weight": .5,
            "opacity": .5,
            "fill": True,               
            "fillOpacity": 0.5,           
        })

url = "HYBRID"
url_2= 'https://github.com/kaheetonaa/Yagimapping/raw/main/Case01-LangNu/data/lang-nu-drone-imagery-2.tif'
#104,52751/22,15154

m.split_map(left_layer=url, right_layer=url_2, zoom_control=False)

m.to_streamlit(height=600)