try:
    import httpx
except:
    raise Exception("You must install httpx in order to this library")

import json

class Utils:
    def getSite(self, website):
        r = httpx.get("https://alexa.com/siteinfo/"+website)
        return r.text

    def getInfo(self, website):
        text = self.getSite(website)
        find1 = text.find("dataLayer.push({")+15
        find2 = text.find(");")
        return json.loads(text[find1:find2])

    def parse(self, website, text):
        r = self.getSite(website)
        find1 = r.find(text)+len(text)
        ptext = r[find1:]
        find2 = ptext.find("</script>")
        return json.loads(ptext[:find2])