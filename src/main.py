import asyncio
from asyncio import sleep

from async_spotify.api import API
from async_spotify.preferences import Preferences


async def main():
    await sleep(1)
    preferences: Preferences = Preferences()
    preferences.load_from_env()
    spotify_api: API = API(preferences)

    spotify_code = await spotify_api.get_code_with_cookie(
        "/home/niclas/IdeaProjects/AsyncSpotify/src/private/cookies.txt")
    t = await spotify_api.refresh_token(reauthorize=False, code=spotify_code)
    print(t)


if __name__ == '__main__':
    asyncio.run(main())
