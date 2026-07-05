import asyncio
from services.rick_morty_api import RickMortyAPI

async def main():
    api = RickMortyAPI()
    results = await api.search_by_name("Rick")
    print(type(results))      # какой тип?
    print(len(results))       # сколько элементов?
    print(results[0].keys())  # какие ключи у первого?

asyncio.run(main())