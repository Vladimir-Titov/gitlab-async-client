from enum import Enum
from pprint import pprint
from typing import Any
from urllib.parse import urljoin
from . import types
import aiohttp


class GitlabAuthType(str, Enum):
    header = 'header'
    bearer = 'bearer'
    query_params = 'query_params'


class GitlabHTTPClient:
    def __init__(
        self,
        base_url: str,
        access_token: str,
        session: aiohttp.ClientSession,
        auth_type: GitlabAuthType = GitlabAuthType.header,
    ):
        """
        Initialize a GitlabHTTPClient instance.

        This method sets up the client with the necessary authentication and session information
        for making requests to the GitLab API.

        Args:
            base_url (str): The base URL of the GitLab API.
            access_token (str): The access token for authenticating with the GitLab API.
            session (aiohttp.ClientSession): An aiohttp ClientSession object for making HTTP requests.
            auth_type (GitlabAuthType, optional): The type of authentication to use.
                Defaults to GitlabAuthType.header.

        Note:
            Depending on the auth_type, this method will set up either access headers or query parameters
            for authentication in subsequent API requests.
        """

        self.base_url = base_url
        self.session = session
        self.auth_type = auth_type

        if auth_type == GitlabAuthType.bearer:
            self.access_headers = {'Authorization': f'Bearer {access_token}'}
        elif auth_type == GitlabAuthType.header:
            self.access_headers = {'PRIVATE-TOKEN': access_token}
        else:
            self.access_params = {'private_token': access_token}

    async def _request(
        self, method: str, path: str, headers: dict | None = None, params: dict | None = None, *args, **kwargs,
    ) -> Any:
        url = urljoin(self.base_url, path)

        if self.auth_type in (GitlabAuthType.bearer, GitlabAuthType.header):
            headers = {**self.access_headers, **headers} if headers else self.access_headers

        if self.auth_type == GitlabAuthType.query_params:
            params = {**self.access_params, **params} if params else self.access_params

        async with self.session.request(
            method=method, url=url, headers=headers, params=params, *args, **kwargs,
        ) as resp:
            return await resp.json()

    async def get_projects(self) -> types.ProjectList:
        response = await self._request(method='GET', path='api/v4/projects')
        return types.ProjectList.model_validate(response)

    async def get_project_mrs(self, project_id: int):
        pass

    async def get_project_mr(self, project_id: int):
        pass

    async def get_project_mr_diff(self, project_id: int, mr_id: int):
        pass

    async def get_mr_comments(self, project_id: int, mr_id: int):
        pass
