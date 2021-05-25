from alexa_siterank import *

class AlexaException(Exception):
    def __init__(self, exception):
        super().__init__("Exception in main module test: " + str(exception))

r = getRank("google.com")
print(type(r))
if not type(r) is dict:
    raise AlexaException("Rank is not dict")
print(r)

r = getRankHistory("google.com")
print(type(r))
if not type(r) is dict:
    raise AlexaException("Rank history is not dict")
print(r)

r = getVisitors("google.com")
print(type(r))
if not type(r) is list:
    raise AlexaException("Visitors is not list")
print(r)

r = getTopKeywords("google.com")
print(type(r))
if not type(r) is dict:
    raise AlexaException("Top keywords is not dict")
print(r)

r = getCompetitors("google.com")
print(type(r))
if not type(r) is dict:
    raise AlexaException("Competitors are not dict")
print(r)

r = getFullRankHistory("google.com")
print(type(r))
if not type(r) is dict:
    raise AlexaException("Rank history is not dict")
print(r)

