import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

#PAGE_CONFIG = {"page_title":"StColab.io","page_icon":":smiley:","layout":"centered"}
#st.beta_set_page_config(**PAGE_CONFIG)

# set page layout
st.set_page_config(
    page_title="WOMER",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

#reducing space 
st.markdown("""
    <style>
    .css-1aumxhk {
        padding: 0em 1em;
    }
    </style>
""", unsafe_allow_html=True)


  #background-color: blue !important;

st.markdown("""
<style>
.sidebar .sidebar-content {
    background-color: blue ;
   
}
</style> 
""",
    unsafe_allow_html=True,
)


#TEMPLATE DASHBOARDS

#SIDEBAR

#IMAGE IN THE SIDEBAR
from PIL import Image
st.sidebar.image('https://github.com/merlynjocol/WOMER/blob/main/Images/WOMERLOGO_NOT_BACKGROUND_GREE-removebg-preview.png?raw=true', width=160)

st.sidebar.header('''📈 This App makes visible the climate actions by Indigenous Women''') 
st.sidebar.subheader('''Explore ⬇️''') 


#CREATE A NAVIGATION BAR (check link)
#https://www.youtube.com/watch?v=hoPvOIJvrb8


# MULTIPAGES SELECTOR 
# create your radio button with the index that we loaded
choice = st.sidebar.radio(" ", ('Main page','Right to Land', 'Access to Natural Resources','Climate Impact', 'Participation in decision-making', 'Climate Actions'))


# Footer
st.sidebar.markdown ('---')
st.sidebar.markdown('''Designed by: **Merlyn J. Hurtado**  ''')
st.sidebar.markdown(''' Supported by ''')

# Logos in columns
col1, col2, col3 = st.sidebar.columns([1.4, 0.8, 0.8])

with col1:
  st.image('https://github.com/merlynjocol/WOMER/blob/main/Images/Crowd4SDG-removebg-preview.png?raw=true', width=120)
            
with col2:
  st.image('https://github.com/merlynjocol/WOMER/blob/main/Images/CERN_ideasSquare-removebg-preview.png?raw=true', width=60)

with col3:
  st.image('https://github.com/merlynjocol/WOMER/blob/main/Images/LPI-sm.png?raw=true', width=60)


# THE DATA 

# DATA-Right to land
url_land= "https://five.epicollect.net/api/export/entries/rights-to-land?form_ref=c7b07eb4f023484296cd833f958005d4_61f3e06e5cbb9&format=csv&per_page=1000&page=1"
data_land= pd.read_csv(url_land)

#change the columns names
dict = {'1_What_are_you_indig': "community", '2_What_is_the_area_y': "area", '3_Do_you_own_a_produ':"land_productive",
       '4___Are_you_the_owne':"house", '5_Do_you_have_rights':'rights'}


# call rename () method
data_land.rename(columns=dict,
                 inplace=True)

#Change the name NaN to Wayuu
data_land['community'] = data_land['community'].replace(np.nan, 'Wayuu People ')



# CODING THE PAGES

# MAIN PAGE
if choice == 'Main page':

  #First container
  #Title
  st.image('https://raw.githubusercontent.com/merlynjocol/WOMER/main/Images/WOMER_LOGO_VERDE.png', width=160)
  st.write ('''WOMER is an easy way to collect, monitor, visualize, generate and share data of climate actions led by indigenous women. 
It combines a mobile App for data collection, a this Web Platform to monitor and generate reports.''')

#Second container 
  st.subheader ('''Why Is Important To Generate Gender & Ethinicity Data for the 🌍?''')
  st.write ('''⬜ Indigenous Women are key to addres the climate change. They protect the 82% of biodiversity worldwide ''')
  st.write ('''⬜ Gender data make more gender responsive and fair public policy''')
  st.write ('''⬜ Empower indigenous women and make them visible in their communities and countries''') 
  st.write ('''⬜ Accelerate progress towards the Sustainable Development Goals (SDGs)''')


  st.markdown ('---')


elif choice == 'Right to Land':
   
  #CONTAINER:HEADER
  st.markdown ('<h1 style= "font-family:Verdana; color:Black; font-size: 40px;"> 🌱Right to Land</h1>', unsafe_allow_html=True)
  #st.text('this is app')
  st.write (''' 
  The dashboards represents the ownership and right to land''')
  st.markdown ('---')


  # SELECTING THE COMMUNITY
  community= st.multiselect("SELECT A INDIGENOUS COMMUNITY", data_land['community'].unique())

  #Create dataframe for barchart   
  data_community= data_land[data_land['community'].isin(community)].groupby(['area']).count().reset_index()
  df_community= data_community[["area", "community"]]
  #bar chart with streamlit    
  fig1 = px.bar(df_community, x="area", y="community",  
                #title="Size of the productive Lan work by women", 
                width=600, height=300, 
                labels={ # replaces default labels by column name
                'area': 'Land Area (ha)',  'community': 'Total of Women'
                }, template = "simple_white"
                 )
  fig1.update_traces(marker_color='#00aae6', opacity = 0.8)
  #fig1.update_yaxes(showgrid=True)
  #fig1.update_layout(template = "simple_white")
  #fig1.update_traces(marker_color='A3C') 

  fig1.update_layout(title = "Size of the Land Where Produce Women",  title_font_size = 30)
  fig1.update_layout(template = "simple_white")
  st.plotly_chart(fig1, unsafe_allow_html=True)


#CHART PIE Year 2018
  #Create dataframe for barchart  
  land_productive = data_land[data_land['community'].isin(community)].groupby(['land_productive']).count().reset_index()
  df_land_productive= land_productive[["land_productive", "community"]]
  
  #bar chart with streamlit  
  fig_pie = px.pie(df_land_productive, values='community', names='land_productive', color='land_productive',
                 #color_discrete_map={'Agriculture':"#2a2b5a",  'Forest land':'#0bca9b', "Other land':'#e51858'},
                                    width = 700, height = 400, color_discrete_sequence=px.colors.sequential.Turbo)
  fig_pie.update_layout(title="% of Women with Productive Land",  title_font_size = 30)
  st.plotly_chart(fig_pie, unsafe_allow_html=True)


  # chart onwershio land
  #Create dataframe for barchart   
  data_ownership = data_land[data_land['community'].isin(community)].groupby(['house']).count().reset_index()
  house_ownership= data_ownership[["house", "community"]]
  #bar chart with streamlit    

  house_sorted= house_ownership.sort_values(by= "house", ascending=False)
  fig3 = px.bar(house_sorted, x="community", y="house",  
                 
                width=700, height=400, 
                #labels={ # replaces default labels by column name
                #'house': 'Land Area (ha)',  'community': 'Total of Women'
                #},
                 )
  fig3.update_layout(title = "Do I own the house?",  title_font_size = 30)
  fig3.update_yaxes(tickmode="array", title_text= " ")                 
  fig3.update_yaxes(showgrid=True)
  fig3.update_traces(marker_color='#00aae6', opacity = 0.8)
  fig3.update_layout(template = "simple_white")
  st.plotly_chart(fig3, unsafe_allow_html=True)

  # chart rights
  data_rights= data_land[data_land['community']== "Nasa People"].groupby(['rights']).count().reset_index()
  rights= data_rights[["rights", "community"]]
  #pie chart with streamlit    
  rights_pie = px.pie(rights, values='community', names='rights', color='rights',
                 #color_discrete_map={'Agriculture':"#2a2b5a",  'Forest land':'#0bca9b', "Other land':'#e51858'},
                                    width = 800, height = 400, color_discrete_sequence=px.colors.sequential.Turbo)
  rights_pie.update_layout(title="Do I have rights on the Land?",  title_font_size = 30)
  st.plotly_chart(rights_pie, unsafe_allow_html=True)


elif choice == 'Access to Natural Resources':
   
  #CONTAINER:HEADER
  st.markdown ('<h1 style= "font-family:Verdana; color:Black; font-size: 40px;"> 🌱Access to Natural Resources</h1>', unsafe_allow_html=True)
  #st.text('this is app')
  st.write (''' 
  The dashboards represents the access to Natural Resources in time and type, include water, land and energy sources''')
  st.markdown ('---')


elif choice == 'Time invested caring nature':

  #CONTAINER:HEADER
  st.markdown ('<h1 style= "font-family:Verdana; color:Black; font-size: 40px;"> ⏱️Time invested caring nature</h1>', unsafe_allow_html=True)
  #st.text('this is app')
  st.write (''' 
  The dashboards represents the Time investment in regenerating and preserving nature''')
  st.markdown ('---')


elif choice == 'Climate Actions':

  #CONTAINER:HEADER
  st.markdown ('<h1 style= "font-family:Verdana; color:Black; font-size: 40px;"> 🌍 Climate Actions </h1>', unsafe_allow_html=True)
  #st.text('this is app')
  st.write (''' 
  The dashboards show the Climate Actions are all the practices of conservation and proteccion of land, water, biodiversity, ecosystem services''')
  st.markdown ('---')

  st.write('''Adaptation actions can be grouped into three categories: 
  * Structural and physical adaptation
  * Social adaptation
  * Institutional adaptation ''')

elif choice == 'Power decision-making':

  #CONTAINER:HEADER
  st.markdown ('<h1 style= "font-family:Roboto; color:Black; font-size: 40px;"> ☝🏼 Power decision-making </h1>', unsafe_allow_html=True)
  #st.text('this is app')
  st.write (''' 
  The dashboards show the level of participation of women in environmental decision making''')
  st.markdown ('---')

