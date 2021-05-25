from alexa_siterank.future import *
import asyncio

async def alexa():
    print("Rank: ")
    print(await getRank("google.com"))
    print("Rank history: ")
    print(await getRankHistory("google.com"))
    print("Visitors: ")
    print(await getVisitors("google.com"))
    print("Top keywords: ")
    print(await getTopKeywords("google.com"))
    print("Competitors: ")
    print(await getCompetitors("google.com"))
    print("Full rank history: ")
    print(await getFullRankHistory("google.com"))

asyncio.run(alexa())