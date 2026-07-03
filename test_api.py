import asyncio
from services.rick_morty_api import RickMortyAPI


async def main():
    api = RickMortyAPI()

    character = await api.get_random_character()
    print(f"Случайный: {character['name']}")

    results = await api.search_by_name("Rick")
    print(f"Найдено Риков: {len(results)}")

    alive = await api.get_by_status("alive")
    print(f"Живых персонажей на странице: {len(alive)}")

    await api.session.close()


asyncio.run(main())