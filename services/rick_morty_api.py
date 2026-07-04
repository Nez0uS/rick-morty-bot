import random
import aiohttp


class RickMortyAPI:
    BASE_URL = "https://rickandmortyapi.com/api"

    def __init__(self):
        self.session = None

    async def _get_session(self) -> aiohttp.ClientSession:
        if self.session is None or self.session.closed:
            connector = aiohttp.TCPConnector(ssl=False)
            self.session = aiohttp.ClientSession(connector=connector)
        return self.session

    async def get_character(self, character_id: int) -> dict:
        session = await self._get_session()
        url = f"{self.BASE_URL}/character/{character_id}"
        async with session.get(url) as response:
            return await response.json()

    async def get_random_character(self) -> dict:
        session = await self._get_session()
        url = f"{self.BASE_URL}/character"
        async with session.get(url) as response:
            data = await response.json()
        total = data["info"]["count"]
        random_id = random.randint(1, total)
        return await self.get_character(random_id)

    async def search_by_name(self, name: str) -> list:
        session = await self._get_session()
        url = f"{self.BASE_URL}/character?name={name}"
        async with session.get(url) as response:
            data = await response.json()
        return data["results"]

    async def get_by_status(self, status: str) -> list:
        session = await self._get_session()
        url = f"{self.BASE_URL}/character?status={status}"
        async with session.get(url) as response:
            data = await response.json()
        return data["results"]