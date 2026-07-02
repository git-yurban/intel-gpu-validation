from pathlib import Path

from pydantic import BaseModel


class ArtifactConfig(BaseModel):

    cache_root: Path

    endpoint: str

    bucket: str

    access_key: str

    secret_key: str