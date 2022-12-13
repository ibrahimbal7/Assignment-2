# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 21:34:17 2022

This is a solution for Applied Data Science 1 lecture Assignment 2

@author: ibrah
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def Reading(df,file):
    """
    Reading the csv files, choosing the countries for the data, creating 
    dataframe, eliminating nan values, making 2 dataframes by having both years
    and countries as columns.
    df: data
    file:name of the csv file
    """
    df = pd.read_csv(file,sep=';', on_bad_lines='skip')
    df = df[(df["Country Name"] == 'Turkiye')
             | (df["Country Name"] == "Japan")
              | (df["Country Name"] == "Russian Federation")
               | (df["Country Name"] == "India")
                | (df["Country Name"] == "China")
                 | (df["Country Name"] == "Pakistan")
                  | (df["Country Name"] == "United States")
                   | (df["Country Name"] == "United Kingdom")
                    | (df["Country Name"] == "Germany")
                     | (df["Country Name"] == "Belgium")                                     
                      ]    
    df=df[["Country Name",  
                      '1990',
                       '2000',
                        '2012' ,
                         '2017' ,
                          '2018' ,
                           '2019' ,                  
                           ]]   
    df=df.dropna(axis=1)
    df1=df.groupby('Country Name').agg('mean')
    df2= df1.transpose()
    df=[df1,df2]
    
    return df

def transposes(df,serie):
    """
    Taking tranpose of a data by choosing spesific serie and making a new 
    dataframe.
    df: new dataframe
    serie: Column that we choose
    """
    df = df_comp[(df_comp["Series Name"] == serie)]
    df=df.groupby('Country Name').agg('mean')
    df =df.transpose()
    return df

def barchart(df,title,a,w,d,fig_name,color):
    """
    Produces a barchart with data to compare a serie for different countries 
    and years.
    df: data to plot
    title: title of the graph
    a: rotation of the x labels
    w: width of the plot
    d: dpi for the png file
    fig_name: name of the png file
    color: colors of the bars
    """
    plt.figure()
    
    df.plot(kind='bar',figsize=(12,6),color=color,width=w)
    plt.xticks(rotation=a)
    plt.title(title)
    plt.legend(title='Year',loc='upper right')
    plt.savefig(fig_name,dpi=d)
    
    plt.show()    

def stacked_bar(df,column1,column2,label1,label2,xlabel,title,file):
    """
    Produces a stacked barchart by having 2 countries
    df: data to creare plot
    column1: first column to plot the first country
    column2: second column to plot the second country
    label1: first countries label for legend
    label2: second countries label for legend
    xlabel: xlabel of the plot,
    title: title of the plot
    file: file name for the png
    """
    plt.figure(figsize=(10,8))    
    
    plt.bar(df,column1,label=label1)
    plt.bar(df,column2,label=label2)        
    plt.title(title)
    plt.xlabel(xlabel)
    #Making the legends on outside of barcharts
    plt.legend(bbox_to_anchor =(1, 1))    
    plt.savefig(file,dpi=180)
    
    plt.show()
    
def lineplot(df,d,fig_name,title,marker,style):
    """
    Produces a dashed line plot with dods on each period from a data.
    df : data to plot
    d: dpi for the png file
    fig_name: name of the png file
    title: title of the plot
    marker: making a mark for each period
    style: choosing the linestyle
    """
    plt.figure(figsize=(13,8))
    
    plt.plot(df,label=df.columns,marker=marker,linestyle=style)
    plt.xlabel('Year')
    plt.title(title)
    #Choosing the minimum and maximum of periods to have bigger plot
    plt.xlim(min(df.index), max(df.index))
    plt.legend(bbox_to_anchor =(1, 1),prop={'size': 7})
    plt.savefig(fig_name,dpi=d)
    
    plt.show()

def piechart(df,label,title,file):
    """
    Produces a piechart to compare countries by percantage.
    df: dataframe to make chart
    label: labels for the graph
    title: title of the chart
    file: name of the file for the png
    """
    plt.figure(figsize=(10,8))
    
    plt.pie(df,labels=label,autopct=('%1.1f%%'))  
    plt.title(title)
    plt.savefig(file,dpi=180)
    
    plt.show()

def average(df,a):
    """
    Taking the average of each row and creating a new dataframe by values
    df: dataframe to make calculation
    a: new dataframe to have table of average values
    """
    #loop to find mean of each raw and making a new dataframe 
    #by adding each value to the next raw.
    for i in df[1].columns:
        a.append(np.average(df[1][i]))
        
    return a

# -----------------------------------------------------------------------------
# first graphs: Making 2 barchart by using 2 different data. They show CO2 
# Emissions and Populations of 10 different countries in the years of 1990,
# 2000,2012,2017,2018,2019.
#Firstly initializing all the values that will be needed 
df_popul,df_CO2,df_renew,df_ener,df_comp= [],[],[],[],[]
df1,df2,df3,av_cons,av_popul = [],[],[],[],[]

# Reading Worldbank Climate Change data in the original format with the series
# of Population and CO2 Emissions in all countries                                        
df_popul = Reading(df_popul,'population.csv')
df_CO2 = Reading(df_CO2,'CO2.csv')

#Defining different colors to make the comparision clearly for two barcharts
color1=['black','red','green','orange','cyan','blue']
color2=['yellow','purple','black','pink','red','orange']

#Calling barchart function for both Population and CO2 emission data
barchart(df_popul[0],'Population',15,0.7,180,'population.png',color1)
barchart(df_CO2[0],'Co2 Emission (kt)',15,0.7,180,'CO2.png',color2)

#Making new dataframes to have averages of CO2 Consumption and Population in
#China and India from previous CO2 and population transposed data
av_cons=pd.DataFrame(average(df_CO2,av_cons),
                     columns=['Average C02 Consumption'],index=df_CO2[0].index)
av_popul= pd.DataFrame(average(df_popul,av_popul),
                       columns=['Average Population'],index=df_CO2[0].index)

#Having a new dataframe to have Average Consumption per person. Dividing 
#Average CO2 Consumption by Average Population columns gives this new column 
av_per= pd.DataFrame(av_cons['Average C02 Consumption']/
                     av_popul['Average Population'],
                     columns=['Average Consumption per person'],
                     index=df_CO2[0].index)

#Calling piechart function and having comparision pf percantages of 
#average CO2 Consumption for 10 countries

piechart(av_per['Average Consumption per person'],av_per.index,
         'Average CO2 Emission per person','compare')

#Reading another files which include Renewable energy consumption 
#(% of total final energy consumption) and Energy use (kg of oil equivalent 
#per capita) data
df_renew = Reading(df_renew,'renewable.csv')
df_ener = Reading(df_ener,'energy.csv')

#Calling line plot function and having to lineplot by renewable and energy use
#data. Making the lines in dashed style and marker with dods.
lineplot(df_renew[1],180,'renewable.png',
         'Renewable energy consumption (% of total final energy consumption)',
         '.','dashed'
             )
lineplot(df_ener[1],180,'energy.png',
                   'Energy use (kg of oil equivalent per capita)','.','dashed'
                   )

#Reading another data for stacked barcharts to compare total,urban and rural
#population between most crowded two countries
df_comp = pd.read_csv('compare.csv',sep=';', on_bad_lines='skip')

#Transposing the data to have countries as columns
df1 = transposes(df1,'Population')
df2 =  transposes(df2,'Urban population')
df3 =  transposes(df3,'Rural population')

#Calling stacked barchart function to have 3 different stacked bar charts with
#the series of Total, Urban and Rural Population  
stacked_bar(df1.index,df1['China'],df1['India'],'China','India',
            'Year','Total Population','Total_pop')
stacked_bar(df2.index,df2['China'],df2['India'],'China','India',
            'Year','Urban Population','Urban_pop')
stacked_bar(df3.index,df3['India'],df3['China'],'India','China',
            'Year','Rural Population','Rural_pop') 



