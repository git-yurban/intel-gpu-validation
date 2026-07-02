from pathlib import Path

from .models import BuildManifest, WorkerManifest


def load_build_manifest(path: Path) -> BuildManifest:
    return BuildManifest.model_validate_json(path.read_text())


def load_worker_manifest(path: Path) -> WorkerManifest:
    return WorkerManifest.model_validate_json(path.read_text())