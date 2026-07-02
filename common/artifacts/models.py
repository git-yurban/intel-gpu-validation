from typing import Literal

from pydantic import BaseModel, ConfigDict

from .enums import Component, Compression
from .types import GitSha, Sha256


class Artifact(BaseModel):
    model_config = ConfigDict(frozen=True)

    component: Component
    git_sha: GitSha
    object_name: str
    sha256: Sha256
    compression: Compression
    size: int