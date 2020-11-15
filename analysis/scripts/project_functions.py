import pandas as pd
import numpy as np
import csv

#Process the anime.csv file
def load_and_process_anime(path):
    #Deal with unnecessary data and missing values
    df1 = pd.read_csv(path)
    df1 = df1.drop(columns='members').loc[~((df1['episodes'] == 'Unknown') | (df1['episodes'] == 'NaN') | (df1['rating'].isna()))]
    #Process some data, and remove any rows with the 'Hentai' to keep things family-friendly
    df1 = df1.assign(genre = lambda x: x.genre.str.split(",")).sort_values("anime_id").loc[~(df1['genre'].isin(['Hentai']))].reset_index(drop=True)
    return df1

#process the rating.csv file
def load_and_process_ratings(path,whitelist):
    #Deal with unnecessary data and missing values
    df1 = pd.read_csv(path)
    df1 = df1.loc[~((df1['rating'] == -1 ) | (df1['rating'].isna()))] #Ditch the rows with a rating of -1 which means the user watched it but didn't rate it
    
    #Process some data, and remove any rows with the 'Hentai' to keep things family-friendly
    df1 = df1.loc[(df1['anime_id'].isin(whitelist))].reset_index(drop=True)
    return df1