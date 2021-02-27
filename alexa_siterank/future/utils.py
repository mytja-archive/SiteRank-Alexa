try:
    import httpx
except:
    raise Exception("You must install httpx in order to use async features")

import json

class Utils:
    async def getSite(self, website):
        async with httpx.AsyncClient() as client:
            r = await client.get("https://alexa.com/siteinfo/"+website)
        return r.text

    async def getInfo(self, website):
        text = await self.getSite(website)
        find1 = text.find("dataLayer.push({")+15
        find2 = text.find(");")
        return json.loads(text[find1:find2])

    async def parse(self, website, text):
        r = await self.getSite(website)
        find1 = r.find(text)+len(text)
        ptext = r[find1:]
        find2 = ptext.find("</script>")
        return json.loads(ptext[:find2])