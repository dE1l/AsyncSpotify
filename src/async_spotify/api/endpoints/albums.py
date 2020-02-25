"""
Handle the requests to the albums endpoint
"""

from typing import List

import async_spotify
from async_spotify.api.decorators import get_url


class Albums:
    """
    Wraps the spotify album functions
    """

    def __init__(self, api_object):
        """
        Create a new spotify album query class which handles the queries concerning albums
        :param api_object: The api object the class is assigned to
        """

        self.api_object = api_object  # type: async_spotify.API

    @get_url
    async def get_album(self, album_id: str, **kwargs) -> dict:
        """
        Get the album with the specific spotify album id
        https://developer.spotify.com/documentation/web-api/reference/albums/get-album/
        :param album_id: The album id of the album you want to get
        :param kwargs: Optional arguments as keyword args
        :return: The album json
        """

        required_args = {"id": album_id}
        return {**required_args, **kwargs}

    async def get_album_tracks(self, album_id: str):
        """

        :param album_id:
        :return:
        """
        pass

    async def get_multiple_albums(self, id_list: List[str], market: str = None):
        """

        :param id_list:
        :param market:
        """
        pass
