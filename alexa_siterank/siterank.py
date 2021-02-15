import requests
import json

def getSite(website):
  r = requests.get("https://alexa.com/siteinfo/"+website)
  return r.text

def getInfo(website):
  text = getSite(website)
  find1 = text.find("dataLayer.push({")+15
  find2 = text.find(");")
  return json.loads(text[find1:find2])

def parse(website, text):
  r = getSite(website)
  find1 = r.find(text)+len(text)
  ptext = r[find1:]
  find2 = ptext.find("</script>")
  return json.loads(ptext[:find2])

def getRank(website):
  r = getInfo(website)
  return r["siteinfo"]

def getTopKeywords(website):
  return parse(website, '<script type="application/json" id="topKeywordsJSON">')

def getCompetitors(website):
  return parse(website, '<script type="application/json" id="competitorsJSON">')

def getVisitors(website):
  return parse(website, '<script type="application/json" id="visitorPercentage">')

def getRankHistory(website):
  return parse(website, '<script type="application/json" id="rankData">')

def getFullRankHistory(website):
  return parse(website, '<script type="application/json" id="rankDataWindow">')
