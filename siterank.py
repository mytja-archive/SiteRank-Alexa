import requests
import json

def getRank(site, toSearch='"global"'):
  html = requests.get('https://www.alexa.com/siteinfo/'+site)

  html = html.text
  #html = html[256:500]

  script = html.find(toSearch)

  #print("Script:")
  toParse = html[script:script+20].replace("\n", "")
  parsed = toParse.replace(" ", "")
    
  return parsed
