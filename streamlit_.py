#import std libraries
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import plotly.express as px


st.title('Penguin explorer')

st.write('**Little** *app* for exploring `penguin` [datset] (https://allisonhorst.github.io/palmerpenguins/')
st.image('https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/man/figures/lter_penguins.png')
# Write a title
# Write data taken from https://allisonhorst.github.io/palmerpenguins/
# Put image https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/man/figures/lter_penguins.png
# Write heading for Data
# Read csv file and output a sample of 20 data points
# Add a selectbox for species
# Display a sample of 20 data points according to the species selected with corresponding title
# Plotting seaborn
# Plotting plotly
# Bar chart count of species per island
# Maps
# Reference https://deckgl.readthedocs.io/en/latest/
# sidebar comment

st.header('Data')
df = pd.read_csv('penguins_extra.csv')
st.write('Display a sample of data points from penquins df', df.sample(20))
file = st.file_uploader('Upload a file')
file = pd.read_csv(file)
st.write(file.head())
species = st.selectbox('Choose a species', df.species.unique())
df_species = df.loc[df.species == species]
st.write(f'Displaying subset of {species}', df_species.sample(20))
st.subheader('Plotting')
fig,ax = plt.subplots()
ax = sns.scatterplot(data = df, x = 'bill_length_mm', y = 'bill_depth_mm', hue = 'species', size = 'sex')
st.pyplot(fig)


st.subheader('Creating interactive plots with plotly')
fig = px.scatter(df, x = 'bill_length_mm', y = 'flipper_length_mm', color = 'species', animation_frame = 'species', hover_name = 'name', range_x = [30,70], range_y = [150, 300])
st.plotly_chart(fig)

st.bar_chart(df.groupby('species')['island'].count())

st.map(df)

choice = st.sidebar.radio('Hope this was interesting', ['yes', 'no'])