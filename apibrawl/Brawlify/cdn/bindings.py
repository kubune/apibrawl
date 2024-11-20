class Bindings:
    def __init__(self, base_url: str = None):
        self.BASE = base_url or "https://cdn.brawlify.com"
        self.ICONS = self.BASE + "/profile-icons/regular/"
        self.MAPS = self.BASE + "/maps/regular/"
        self.GAMEMODES = self.BASE + "/game-modes/regular/"

    def image(self, id):
        if str(id).startswith("15"):
            # Map ID
            return self.MAPS + str(id) + ".png"
