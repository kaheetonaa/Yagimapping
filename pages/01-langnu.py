import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd

st.set_page_config(
    page_title='Mapping Làng Nủ',
    page_icon='🛖',
    layout='wide',
    initial_sidebar_state='collapsed'
)

st.title("Mapping làng Nủ")

col1, col2=st.columns(2)
with col1:
    option_1 = st.selectbox(
    "Dữ liệu bên trái trái",
    (" ", "Ảnh hiện trạng", "Bản đồ lịch sử"),
    index=0
    )
with col2:
    option_2 = st.selectbox(
    "Dữ liệu bên trái phải",
    (" ", "Ảnh hiện trạng", "Bản đồ lịch sử"),
    index=1
    )

layer_url=dict({' ':'SATELLITE','Ảnh hiện trạng':'https://github.com/kaheetonaa/Yagimapping/raw/main/Case01-LangNu/data/lang-nu-drone-imagery-2.tif','Bản đồ lịch sử':'https://github.com/kaheetonaa/Yagimapping/raw/main/Case01-LangNu/data/langnu-geo-fixed.tif'})


m = leafmap.Map(height=600, center=[22.25, 104.5], zoom=12)

m.add_basemap("SATELLITE")

in_geojson = "https://github.com/kaheetonaa/Yagimapping/raw/main/Case01-LangNu/data/langnu-googleopenbuildings.geojson"
df=gpd.read_file(in_geojson)
layer_style=dict({'No':'white','Non detected':'black','Yes':'red'})

df['color']= df.replace({"Destroy": layer_style})['Destroy']


m.add_data(df, layer_name="Công trình",categories=['No','Non detected','Yes'],colors=['white', 'black','red'],column = "Destroy", legend_title='Cong trinh', labels=['Không ảnh hưởng','Chưa xác định','Hủy hoại'],
        style_function = lambda x:({
            "stroke": True,
            "color": x['properties']['color'] ,
            "weight": .5,
            "opacity": 1,             
            "fillOpacity": 0.5,
            "fillColor": x['properties']['color']         
        }))

url = layer_url[option_1]
url_2= layer_url[option_2]
#104,52751/22,15154

m.split_map(left_layer=url, right_layer=url_2, zoom_control=False)

m.to_streamlit(height=600)

st.write("*Nguồn dữ liệu công trình: Google open buildings, Ảnh hiện trạng: Chi cục Kiểm lâm tỉnh Lào Cai, Bản đồ nền: Google Maps Satellite. Tác giả: Nguyễn Quang Huy(GIS-GeoLab,OSMVN,Kaheetonaa)*")