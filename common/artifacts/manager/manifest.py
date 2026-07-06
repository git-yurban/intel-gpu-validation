from pathlib import Path

from .models import Manifest


def load(path: Path) -> Manifest:
    return Manifest.model_validate_json(path.read_text())