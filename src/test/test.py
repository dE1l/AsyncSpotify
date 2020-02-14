import asyncio

from async_spotify.API import API
from async_spotify.Preferences import Preferences
from private import token


async def main():
    preferences = Preferences()
    preferences.load_from_env()

    spotify_api = API(preferences)
    # spotify_api.open_oauth_dialog_in_browser()
    await spotify_api.refresh_token(token, grant_type="authorization_code")


asyncio.run(main(), debug=True)
