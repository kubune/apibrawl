

class API:
    def __init__(self, base_url: str = None):
        self.BASE = base_url or "https://api.brawlstars.com/v1"
        self.EVENTS = self.BASE + "/events/rotation"
        self.PLAYER = self.BASE + "/players/%23"
        self.CLUB = self.BASE + "/clubs/%23"
        self.RANKINGS = self.BASE + "/rankings"


def toTag(tag: str) -> str:
    tag = tag.replace("#", " ").replace("o", "0").replace("O", "0").upper()

    allowed = '0289PYLQGRJCUV'

    invalid = [c for c in tag if c not in allowed]
    if invalid:
        raise Exception("Wrong Tag")

    if tag.startswith("%23"):
        tag = tag.replace("%23", "")

    return tag