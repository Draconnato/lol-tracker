import requests
import json

def getCurrentGame(token,summonerId):

    endPoint = f'https://br1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{summonerId}'

    response = requests.get(endPoint,headers={'X-Riot-Token':token})
    
    print (response)
    return json.loads(response.content.decode('utf8'))