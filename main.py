# token RGAPI-d6d684b0-cfd5-445d-acd1-fcab11b614a1''

import source.summoner as summoner 
import source.league as league
from source.spectator import getCurrentGame
from credentials import credentials

from pprint import pprint

token = credentials.TOKEN

summonerData = summoner.getSummoner(token,'Bojji')

currentGame = getCurrentGame(token,summonerData['id']) # the getCurrentGame is limitated by region

participants = currentGame['participants']

print(f"########################################\n\n You are current tracking\n {summonerData['name']} - level {summonerData['summonerLevel']}\n\n########################################")

summonerBlueSide = []
summonerRedSide = []

for summonerInGame in participants:
    if summonerInGame["teamId"]==100:
        summonerBlueSide.append(summonerInGame["summonerId"])
    else:
        summonerRedSide.append(summonerInGame["summonerId"])
"""
print("Blue")

pprint(summonerBlueSide)
print("Red")
pprint(summonerRedSide)
"""
winRate = {}
tierRank = {}

for summonerInGame in summonerBlueSide:
    
    leagueData = league.getLeague(token,summonerInGame)[0]
    
    wins = leagueData["wins"]
    losses = leagueData["losses"]
    tier = leagueData.get("tier",None)
    rank = leagueData.get("rank",None)

    winRate.update({summonerInGame: wins/(wins+losses)})
    tierRank.update({summonerInGame: tier+rank})
    # usar if tier in league data then tierrank update para evitar que não ter dado vai crashar

pprint(winRate)
pprint(tierRank)