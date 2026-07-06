from pathlib import Path

from pydantic import BaseModel


class ArtifactConfig(BaseModel):
    cache_root: Path

    minio_endpoint: str

    bucket: str

    access_key: str

    secret_key: str