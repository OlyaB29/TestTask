from drf_pydantic import BaseModel


class ArticleSchema(BaseModel):
    article: int
    brand: str
    title: str
    class Config:
        max_anystr_length = 500



