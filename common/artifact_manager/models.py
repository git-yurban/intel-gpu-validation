from pathlib import Path

from pydantic import BaseModel


class Artifact(BaseModel):
    component: str
    git_sha: str
    object_name: str
    sha256: str
    compression: str = "tar.zst"


class Manifest(BaseModel):
    manifest_version: int = 1
    artifacts: list[Artifact]
    environment: dict[str, str] = {}


class ArtifactLocation(BaseModel):
    artifact: Artifact
    local_path: Path