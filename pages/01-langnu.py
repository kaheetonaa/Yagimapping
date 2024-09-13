import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd


st.title("Mapping lang Nu")


m = leafmap.Map(height=600, center=[22.25, 104.5], zoom=12)

m.add_basemap("SATELLITE")

in_geojson = "https://github.com/kaheetonaa/Yagimapping/raw/main/Case01-LangNu/data/langnu-googleopenbuildings.geojson"
df=gpd.read_file(in_geojson)
layer_style=dict({'No':'white','Non detected':'black','Yes':'red'})

df['color']= df.replace({"Destroy": layer_style})['Destroy']


m.add_data(df, layer_name="Cong trinh",categories=['No','Non detected','Yes'],colors=['white', 'black','red'],column = "Destroy", legend_title='Cong trinh', labels=['Khong anh huong','Chua xac dinh','Huy hoai'],
        style_function = lambda x:({
            "stroke": True,
            "color": "white",
            "weight": 1,
            "opacity": 1,             
            "fillOpacity": 0.5,
            "fillColor": x['properties']['color']         
        }))

url = "SATELLITE"
url_2= 'https://github.com/kaheetonaa/Yagimapping/raw/main/Case01-LangNu/data/lang-nu-drone-imagery-2.tif'
#104,52751/22,15154

m.split_map(left_layer=url, right_layer=url_2, zoom_control=False)

m.to_streamlit(height=600)