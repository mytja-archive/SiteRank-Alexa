# SiteRank-Alexa
This is vanilla Python library for gathering data about website ranks from Alexa!

It is ultra customizable.

# Usage

## Import
```py
from alexa_siterank.future import *
```

## Get PageRank
```py
await getRank("google.com")
```

<br><p><br>

## Get Top keywords
```py
await getTopKeywords("google.com")
```

<br><p><br>

# Get visitors
```py
await getVisitors("google.com")
```

<br><p><br>

# Get competitors
```py
await getCompetitors("google.com")
```

<br><p><br>

# Get SiteRank 3 month history
```py
await getRankHistory("google.com")
```
