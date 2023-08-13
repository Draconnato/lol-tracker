import requests
import json
from urllib.parse import quote

def getSummoner (token,playerName):

    playerName = quote(playerName)

    endPoint = f'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{playerName}'

    response = requests.get(endPoint,headers={'X-Riot-Token':token})

    return json.loads(response.content.decode('utf8'))
