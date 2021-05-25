from alexa_siterank import OTR

class AlexaException(Exception):
    def __init__(self, exception):
        super().__init__("Exception in OTR test: " + str(exception))

otr = OTR()

def printAll():
    r = otr.html
    print(type(r))
    if not type(r) is str:
        raise AlexaException("HTML is not str")
    print(r)

    r = otr.url
    print(type(r))
    if not type(r) is str:
        raise AlexaException("URL is not str")
    print(r)

    r = otr.topKeywords
    print(type(r))
    if not type(r) is dict:
        raise AlexaException("Top keywords are not dict")
    print(r)

    r = otr.visitors
    print(type(r))
    if not type(r) is list:
        raise AlexaException("Visitors are not dict")
    print(r)

    r = otr.rank
    print(type(r))
    if not type(r) is dict:
        raise AlexaException("Rank is not dict")
    print(r)

    r = otr.rankHistory
    print(type(r))
    if not type(r) is dict:
        raise AlexaException("Rank history is not dict")
    print(r)

    r = otr.fullRankHistory
    print(type(r))
    if not type(r) is dict:
        raise AlexaException("Full rank history is not dict")
    print(r)

try:
    otr.get("google.com")
    printAll()

    exit(0)
except Exception as e:
    raise AlexaException(e)