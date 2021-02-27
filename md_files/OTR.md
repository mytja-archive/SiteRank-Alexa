# SiteRank-Alexa
This is vanilla Python library for gathering data about website ranks from Alexa!

It is ultra customizable.

# OTR
OTR (or One-Time Request) is a very efficient and fast way of gathering your data. It requests everytime `.get()` function is called, and then uses this HTML to directly parse it. It is up to 5 times faster than normal function

# Usage
```py
from alexa_siterank import OTR

otr = OTR()

otr.get("google.com")

print("HTML: " + str(otr.html))
print("URL: " + str(otr.url))
print("Top keywords: " + str(otr.topKeywords))
print("Visitors: " + str(otr.visitors))
print("Rank: " + str(otr.rank))
print("Rank history: " + str(otr.rankHistory))
print("Full rank history: " + str(otr.fullRankHistory))
```