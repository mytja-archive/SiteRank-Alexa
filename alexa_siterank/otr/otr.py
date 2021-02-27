from .otrutils import *

class OTR:
    def __init__(self):
        self.url = None
        self.html = None
        self.info = None
        self.rank = None
        self.topKeywords = None
        self.competitors = None
        self.visitors = None
        self.rankHistory = None
        self.fullRankHistory = None
    
    def get(self, website):
        self.url = website

        html = getSite(website)
        self.html = html

        self.info = getInfo(html)
        self.rank = getRank(html)
        self.topKeywords = getTopKeywords(html)
        self.competitors = getCompetitors(html)
        self.visitors = getVisitors(html)
        self.rankHistory = getRankHistory(html)
        self.fullRankHistory = getFullRankHistory(html)
