import json
from .utils import Utils

utils = Utils()

def getRank(website):
  r = utils.getInfo(website)
  return r["siteinfo"]

def getTopKeywords(website):
  return utils.parse(website, '<script type="application/json" id="topKeywordsJSON">')

def getCompetitors(website):
  return utils.parse(website, '<script type="application/json" id="competitorsJSON">')

def getVisitors(website):
  return utils.parse(website, '<script type="application/json" id="visitorPercentage">')

def getRankHistory(website):
  return utils.parse(website, '<script type="application/json" id="rankData">')

def getFullRankHistory(website):
  return utils.parse(website, '<script type="application/json" id="rankDataWindow">')
