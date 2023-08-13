# token RGAPI-d6d684b0-cfd5-445d-acd1-fcab11b614a1''

from source.summoner import getSummoner
from source.spectator import getCurrentGame
from credentials import credentials

from pprint import pprint

token = credentials.TOKEN

summonerData = getSummoner(token,'hard')

currentGame = getCurrentGame(token,summonerData['id']) # the getCurrentGame is limitated by region

participants = currentGame['participants']

print(f"########################################\n\n You are current tracking\n {summonerData['name']} - level {summonerData['summonerLevel']}")