import requests

def getRank(site, toSearch='"global"'):
  html = requests.get('https://www.alexa.com/siteinfo/'+site)

  html = html.text
  #html = html[256:500]

  script = html.find(toSearch)

  #print("Script:")
  return html[script:script+12]
