import json
from .utils import Utils

utils = Utils()

async def getRank(website):
  r = await utils.getInfo(website)
  return r["siteinfo"]

async def getTopKeywords(website):
  return await utils.parse(website, '<script type="application/json" id="topKeywordsJSON">')

async def getCompetitors(website):
  return await utils.parse(website, '<script type="application/json" id="competitorsJSON">')

async def getVisitors(website):
  return await utils.parse(website, '<script type="application/json" id="visitorPercentage">')

async def getRankHistory(website):
  return await utils.parse(website, '<script type="application/json" id="rankData">')

async def getFullRankHistory(website):
  return await utils.parse(website, '<script type="application/json" id="rankDataWindow">')
