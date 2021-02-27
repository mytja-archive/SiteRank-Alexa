from alexa_siterank import OTR

def printAll(otr):
    print("HTML: " + str(otr.html))
    print("URL: " + str(otr.url))
    print("Top keywords: " + str(otr.topKeywords))
    print("Visitors: " + str(otr.visitors))
    print("Rank: " + str(otr.rank))
    print("Rank history: " + str(otr.rankHistory))
    print("Full rank history: " + str(otr.fullRankHistory))

otr = OTR()

printAll(otr)

otr.get("google.com")
printAll(otr)