import requests
import pandas as pd


response = requests.get('https://eu.api.riotgames.com/val/ranked/v1/leaderboards/by-act/7a85de9a-4032-61a9-61d8-f4aa2b4a84b6?size=10&startIndex=0&api_key=RGAPI-42f42892-8832-4e52-a220-8201d7969feb')

valorant_stats = response.json()

position_array = []
name_array = []
tag_array = []


data = {'Position':position_array,
        'Name':name_array,
        'TagLine':tag_array}



for stat in valorant_stats["players"]:
        #print("Name: ",stat["gameName"], "#"+stat["tagLine"])
        position_array.append(stat["leaderboardRank"])
        name_array.append(stat["gameName"])
        tag_array.append("#"+stat["tagLine"])


df = pd.DataFrame(data)
print(df)



