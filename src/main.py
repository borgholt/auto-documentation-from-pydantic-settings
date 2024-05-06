from pydantic_settings import BaseSettings
from pydantic import Field


class TestSettings(BaseSettings):
    use_repo: bool = Field(
        validation_alias="USE_REPO",
        description="Whether to use this repo for anything.",
        default=False,
    )
    language: str = Field(
        validation_alias="LANGUAGE",  # can be overwritten with the new co-pilot protobuf
        description="Language of this README file.",
        default="en",
    )
    rating: int = Field(
        validation_alias="RATING",
        description="Rating given to this repo from 1 to 10.",
        default=6,
    )