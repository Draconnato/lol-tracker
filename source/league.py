import requests
import json

def getLeague (token,summonerId):

    endPoint = f'https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/{summonerId}'

    response = requests.get(endPoint,headers={'X-Riot-Token':token})

    return json.loads(response.content.decode('utf8'))