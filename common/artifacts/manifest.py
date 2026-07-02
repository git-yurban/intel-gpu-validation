from pathlib import Path

from .models import BuildManifest
from .models import WorkerManifest


def load_build(path: Path) -> BuildManifest:
    return BuildManifest.model_validate_json(path.read_text())


def load_worker(path: Path) -> WorkerManifest:
    return WorkerManifest.model_validate_json(path.read_text())