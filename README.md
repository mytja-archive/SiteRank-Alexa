# SiteRank-Alexa
This is vanilla Python library for gathering data about website ranks from Alexa!

It is ultra customizable.

# Installation
You can use `pip install alexa-siterank` or `pip install git+https://github.com/mytja/SiteRank-Alexa`

# ⚡️ Wanna try out [new OTR function](https://github.com/mytja/SiteRank-Alexa/blob/main/md_files/OTR.md)! It is up to 5 times faster than current functions
# ⚡️ Wanna try out [new asynchronous function](https://github.com/mytja/SiteRank-Alexa/blob/main/md_files/async.md)! It requires httpx

# Usage

## Get PageRank
```py
from alexa_siterank import *

print(getRank("google.com"))
```

Output:
```json
{
   "rank":{
      "global":1,
      "us":1
   },
   "rating":false
}
```

<br><p><br>

## Get Top keywords
```py
from alexa_siterank import *

print(getTopKeywords("google.com"))
```

Output:
```json
{
   "titles":[
      "keyword",
      "metric_one",
      "metric_two"
   ],
   "google.com":[
      [
         {
            "title":"keyword",
            "value":"gmail"
         },
         {
            "title":"metric_one",
            "value":"5.11%"
         },
         {
            "title":"metric_two",
            "value":"83.27%"
         }
      ],
      [
         {
            "title":"keyword",
            "value":"google translate"
         },
         {
            "title":"metric_one",
            "value":"3.84%"
         },
         {
            "title":"metric_two",
            "value":"59.46%"
         }
      ],
      [
         {
            "title":"keyword",
            "value":"google maps"
         },
         {
            "title":"metric_one",
            "value":"1.93%"
         },
         {
            "title":"metric_two",
            "value":"55.67%"
         }
      ],
      [
         {
            "title":"keyword",
            "value":"translate"
         },
         {
            "title":"metric_one",
            "value":"1.72%"
         },
         {
            "title":"metric_two",
            "value":"51.89%"
         }
      ],
      ...
```

<br><p><br>

# Get visitors
```py
from alexa_siterank import *

print(getVisitors("google.com"))
```

Output:
```json
[
   {
      "pageviews_per_user":"25.22",
      "code":"US",
      "visitors_percent":"19.5",
      "name":"United States",
      "pageviews_percent":"27.7"
   },
   {
      "pageviews_per_user":"28.07",
      "code":"IN",
      "visitors_percent":"10.4",
      "name":"India",
      "pageviews_percent":"16.5"
   },
   {
      "pageviews_per_user":"26.3",
      "code":"JP",
      "visitors_percent":"5.2",
      "name":"Japan",
      "pageviews_percent":"7.8"
   }
]
```

<br><p><br>

# Get competitors
```py
from alexa_siterank import *

print(getCompetitors("google.com"))
```

Output:
```json
{
   "site":"google.com",
   "competitors":[
      "youtube.com",
      "wikipedia.org",
      "facebook.com",
      "vk.com"
   ]
}
```

<br><p><br>

# Get SiteRank 3 month history
```py
from alexa_siterank import *

print(getRankHistory("google.com"))
```

Output:
```json
{
   "3mrank":{
      "20201116":"1",
      "20201117":"1",
      "20201118":"1",
      "20201119":"1",
      "20201120":"1",
      "20201121":"1",
      "20201122":"1",
      "20201123":"1",
      "20201124":"1",
      "20201125":"1",
      "20201126":"1",
      ...
   }
}
```

<br><p><br>

# Disclaimer
## Developer
The developer(s) of this project aren't responsible for any code usage in non-intended ways!

## Community / People using this project
With downloading any modified and/or original code from this repository, from any source, you agree, that you will use it only for non-production, non-commercial, private uses and for educational purposes, and in monthly limits! If not, you are responsible for non-legal usage of this project!

If you want to use commercial version, then you have to get API token from AWIS.

## This project
This project can only be used for private, non-commercial, non-production uses, and for educational uses.
