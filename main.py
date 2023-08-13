# token RGAPI-d6d684b0-cfd5-445d-acd1-fcab11b614a1''

from summoner import getSummoner
from spectator import getCurrentGame

from pprint import pprint

token = 'RGAPI-d6d684b0-cfd5-445d-acd1-fcab11b614a1'

summonerData = getSummoner(token,'gambe zambe')

currentGame = getCurrentGame(token,summonerData['id'])

participants = currentGame['participants']