import requests
import json

def getSite(website):
    r = requests.get("https://alexa.com/siteinfo/"+website)
    return r.text

def getInfo(html):
    text = html
    find1 = text.find("dataLayer.push({")+15
    find2 = text.find(");")
    return json.loads(text[find1:find2])

def parseHTML(html, text):
    r = html
    find1 = r.find(text)+len(text)
    ptext = r[find1:]
    find2 = ptext.find("</script>")
    return json.loads(ptext[:find2])

def getRank(html):
    r = getInfo(html)
    return r["siteinfo"]

def getTopKeywords(html):
    return parseHTML(html, '<script type="application/json" id="topKeywordsJSON">')

def getCompetitors(html):
    return parseHTML(html, '<script type="application/json" id="competitorsJSON">')

def getVisitors(html):
    return parseHTML(html, '<script type="application/json" id="visitorPercentage">')

def getRankHistory(html):
    return parseHTML(html, '<script type="application/json" id="rankData">')

def getFullRankHistory(html):
    return parseHTML(html, '<script type="application/json" id="rankDataWindow">')