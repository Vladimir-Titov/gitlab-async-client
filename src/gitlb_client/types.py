from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, HttpUrl, Field


class Namespace(BaseModel):
    id: int
    name: str
    path: str
    kind: str
    full_path: str
    parent_id: Optional[int] = None
    avatar_url: Optional[HttpUrl] = None
    web_url: HttpUrl


class Project(BaseModel):
    id: int
    description: Optional[str] = None
    name: str
    name_with_namespace: str
    path: str
    path_with_namespace: str
    created_at: datetime
    default_branch: str
    tag_list: List[str]
    topics: List[str]
    ssh_url_to_repo: str
    http_url_to_repo: HttpUrl
    web_url: HttpUrl
    avatar_url: Optional[HttpUrl] = None
    star_count: int
    last_activity_at: datetime
    namespace: Namespace


class ProjectList(BaseModel):
    projects: List[Project]
