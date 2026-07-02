from pathlib import Path

import pytest
from pydantic import ValidationError

from common.artifacts.manifest import (
    load_build_manifest,
    save_build_manifest,
)
from common.artifacts.models import (
    Artifact,
    Build,
    BuildManifest,
)
from common.artifacts.enums import (
    Component,
    Compression,
)