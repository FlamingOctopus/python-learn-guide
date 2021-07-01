import requests
import json

episode_dict = dict()

deaths = json.loads(requests.get('https://www.breakingbadapi.com/api/deaths').text)
id_info = max(deaths, key=lambda i_dict: i_dict['number_of_deaths'])
episodes = json.loads(requests.get('https://www.breakingbadapi.com/api/episodes').text)

season = str(id_info['season'])
episode = str(id_info['episode'])

for i_data in episodes:
    if i_data['episode'] == episode and i_data['season'] == season:
        episode_dict['episode_id'] = i_data['episode_id']
        break

episode_dict['Season_number'] = id_info['season']
episode_dict['Episode_number_episode'] = id_info['episode']
episode_dict['Total_of_deaths'] = id_info['number_of_deaths']
episode_dict['List_of_dead'] = id_info['death']

with open('data.json', 'w') as file:
    json.dump(episode_dict, file, indent=4)

with open('data.json', 'r') as file:
    print(json.load(file))
