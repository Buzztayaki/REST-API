import shortuuid as uid
import datetime as dt
import pandas as pd
import numpy as np
import os
from tqdm.auto import tqdm

#Codes and names for ALL LEAGUES
leagues = {
        'E0':['England', 'Premier_League'],
        'SP1':['Spain', 'LaLiga'],
        'I1':['Italy', 'Serie_A'],
        'D1':['Germany', 'Bundesliga'],
        'F1':['France', 'Ligue_1']}

#Explanation:
"""
link to a csv file for English Premier League:
https://www.football-data.co.uk/mmz4281/1011/E0.csv
                                      season/league   <-- 
                                      
In the link, '2122' means season 2021-2022
E0 is English Premier league, SP1 is Spanish La Liga, etc."""


#generating a list of lists for ALL desired season

start = 20201                  #starting year
now = dt.date.today().year     #current year
ly = int(str(start)[2:])       #equals to the last 2 digits of start year
years = []                     #will be populated with lists like the example

for x in range(1, now-start+1):
    season = start + x
    seasons = [str(ly)+str(ly+1), str(season-1)+"-"+str(season)]
    ly += 1
    years.append(seasons)

#list of target columns and list of main columns
#check metadata for more info 

wanted = ['Div', 'Date', 'HomeTeam', 'AwayTeam', 'borrar0',
          'FTHG', 'FTAG', 'FTR', 'borrar1', 'borrar2', 'borrar3', 'HS', 'AS', 'HST', 'AST', 'HF', 'AF', 'HC', 'AC', 'HY', 'AY', 'HR', 'AR']

base_attributes = ['id', 'Country', 'League', 'Div', 'Season', 'Date', 'HomeTeam', 'AwayTeam', 'borrar0',
                   'FTHG', 'FTAG', 'FTR', 'borrar1', 'borrar2', 'borrar3', 'HS', 'AS', 'HST', 'AST', 'HF', 'AF', 'HC', 'AC', 'HY', 'AY', 'HR', 'AR']

# older_attributes = ['Div', 'Date', 'HomeTeam', 'AwayTeam', 
#                    'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR']

data = pd.DataFrame(columns=base_attributes)   #creating empty table with the main attributes

#getting the data
links = []
for league in tqdm(leagues.keys(), desc=f"Extracting data"):
    for i in tqdm(years, desc=f'{leagues[league][0]} - {leagues[league][1]}'):
        year = i[0]
        links.append(f'https://www.football-data.co.uk/mmz4281/{year}/{league}.csv')
        temp = pd.read_csv(links[-1], encoding='windows-1252')
#         print(f'{year}/{league}')
        try:
            temp = temp[wanted]
        except:
            for col in wanted:
                if col not in temp.columns:
                    temp[col] = np.nan
            
        temp['Country'] = leagues[league][0]
        temp['League'] = leagues[league][1]
        temp['Season'] = i[1]
        temp['id'] = 0
        temp = temp[base_attributes]
        data = pd.concat([data, temp],ignore_index=True)

#creating ids for all matches
data['id'] = [uid.uuid() for x in data['id']] 

#exporting data into the location of the script
#data.to_excel(f'Euro-Football_{start}-{now}.xlsx', sheet_name= 'Euro_Football', index=False)
data.to_csv(f'matchesdata{start}-{now}.csv', index=False)

print(f"Data extracted and saved here ---> '{os.getcwd()}' \n")
data.info()
