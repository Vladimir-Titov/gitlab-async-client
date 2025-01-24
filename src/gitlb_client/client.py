import aiohttp


class GitlabHTTPClient:
    def __init__(self, url: str, token: str, session: aiohttp.ClientSession):
        """
        Initialize a GitlabHTTPClient instance.

        Args:
            url (str): The base URL of the Gitlab API.
            token (str): The access token for accessing the Gitlab API.
            session (aiohttp.ClientSession): An aiohttp ClientSession object for making HTTP requests.
        """
        self.url = url
        self.token = token
        self.session = session

    async def get_projects(self):
        pass

    async def get_project_mrs(self, project_id: int):
        pass

    async def get_project_mr(self, project_id: int):
        pass

    async def get_project_mr_diff(self, project_id: int, mr_id: int):
        pass

    async def get_mr_comments(self, project_id: int, mr_id: int):
        pass
