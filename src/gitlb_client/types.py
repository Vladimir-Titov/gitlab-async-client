from pydantic import BaseModel, RootModel


class ProjectList(RootModel[list[dict]]):
    pass
