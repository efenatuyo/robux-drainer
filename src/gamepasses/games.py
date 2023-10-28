async def get(self):
    games = await self.session.get(f"https://games.roblox.com/v2/users/{self.user_id}/games", 
                                   json={"limit": 50})
    
    if games.status == 200:
        self.games = [game['id'] for game in (await games.json())["data"]]
    return games.status != 429, bool(self.games)