# importing Liberaries
import pandas as pd
import streamlit as st
import plotly.express as px

# importing dataset
Pre = pd.read_csv("MiniPakistanPreprocessed.csv")
# primary and seconadry list
P = ['Area (Sq. km)','Forest Area (acres)','Total Housing Units','Tehsils','Union Councils','Primary schools','Middle schools','High schools','Road Kilometrage','Motor Vehicles Registered',
          'Health Institutions','Bed Strength','Doctors','Availability of Electricity','Availability of Water']
S = ['Population','Urban Population','Rural Population','Male','Female','Transgender','Population Density per Sq. Km','Ratio Male per hundres females','Number of Cattle',
            'Multi Dimensional Poverty Index','Children fully immunized Urban','Children fully immunized Rural','Urban tap water %','Rural tap water %',
            'Households toilet facility','Learning Score %','Public Toilet %']

# cities and province preprocessing
cities = Pre['City'].tolist()
cities.insert(0,'Overall Pakistan')
provinces = Pre['Province'].unique().tolist()
provinces.insert(0,'Overall Pakistan')

# App building
st.set_page_config(layout="wide",page_title="Pakistan Analysis")
st.header("Pakistan Cities Map")
st.sidebar.title("Pakistan Map")

select = st.sidebar.selectbox("Select Any One",["Province Vise","City Vise"])
if select == "Province Vise":
    selected_province = st.sidebar.selectbox('Select a Province', options=provinces)
    if selected_province == "Overall Pakistan":
        primary = st.sidebar.selectbox("Select Primary Parameter", options=P)
        secondary = st.sidebar.selectbox("Select Secondary", options=S)
        fig = px.scatter_mapbox(Pre, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=4,
                                size_max=35,
                                mapbox_style="carto-positron", width=1200, height=600, hover_name='City')
        st.plotly_chart(fig, use_container_width=True)

    else:
        # Allow the user to select a province
        selected = Pre[Pre['Province'] == selected_province]
        primary = st.sidebar.selectbox("Select Primary Parameter", options=P)
        secondary = st.sidebar.selectbox("Select Secondary", options=S)
        fig = px.scatter_mapbox(selected, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=4, size_max=35,
                                mapbox_style="carto-positron", width=1200, height=600, hover_name='City')
        st.plotly_chart(fig, use_container_width=True)



elif select == "City Vise":
    selected_city = st.sidebar.selectbox("Select a City", options=cities)

    if selected_city == "Overall Pakistan":
        primary = st.sidebar.selectbox("Select Primary Parameter", options=P)
        secondary = st.sidebar.selectbox("Select Secondary", options=S)
        fig = px.scatter_mapbox(Pre, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=4,
                                size_max=35,
                                mapbox_style="carto-positron", width=1200, height=600, hover_name='City')
        st.plotly_chart(fig, use_container_width=True)

    else:
        # Allow the user to select a province
        selected = Pre[Pre['City'] == selected_city]
        primary = st.sidebar.selectbox("Select Primary Parameter", options=P)
        secondary = st.sidebar.selectbox("Select Secondary", options=S)
        fig = px.scatter_mapbox(selected, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=4,
                                size_max=35,
                                mapbox_style="carto-positron", width=1200, height=600, hover_name='City')
        st.plotly_chart(fig, use_container_width=True)
        st.header("About City")
        text = '\n\n'.join(selected['introduction'].values.tolist())
        st.subheader(text)



