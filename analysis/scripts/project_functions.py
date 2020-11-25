import pandas as pd
import numpy as np
import html
import warnings
import random
warnings.filterwarnings("ignore")

#Process the anime.csv file
def load_and_process_anime(path):
    #Deal with unnecessary data and missing values
    df1 = pd.read_csv(path)
    df1 = df1.drop(columns='members').loc[~((df1['episodes'] == 'Unknown') | (df1['episodes'] == 'NaN') | (df1['rating'].isna()))].dropna(axis=0)
    #Process some data, and remove any rows with the 'Hentai' to keep things family-friendly
    df1 = df1.assign(genre = lambda x: x.genre.str.split(",")).sort_values("anime_id").loc[~(df1['genre'].isin(['Hentai']))].reset_index(drop=True)
    df1['genre'] = df1['genre'].map(lambda x: random.sample(x,len(x)))
    df1['episodes'] = pd.to_numeric(df1['episodes'])
    df1['name'] = df1['name'].map(html.unescape) #using a deprecated method, but it converts the names that are encoded with HTML entities into unicode
    return df1

#process the rating.csv file
def load_and_process_ratings(path,whitelist):
    #Deal with unnecessary data and missing values
    df1 = pd.read_csv(path)
    df1 = df1.loc[~((df1['rating'] == -1 ) | (df1['rating'].isna()))].dropna(axis=0) #Ditch the rows with a rating of -1 which means the user watched it but didn't rate it
    
    #Process some data, and remove any rows with the 'Hentai' to keep things family-friendly
    df1 = df1.loc[(df1['anime_id'].isin(whitelist))].reset_index(drop=True)
    return df1