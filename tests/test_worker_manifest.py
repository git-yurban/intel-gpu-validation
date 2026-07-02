from pathlib import Path

import pytest
from uuid import uuid4
from pydantic import ValidationError

from common.artifacts.manifest import (
    load_worker_manifest,
    save_worker_manifest,
)
from common.artifacts.models import WorkerManifest


def create_worker_manifest() -> WorkerManifest:
    """Create a valid WorkerManifest for testing."""

    return WorkerManifest(
        manifest_version=1,
        worker_manifest_id=str(uuid4()),
        build_manifest_id="bm-20260702-000001",
        shard_id="shard-0001",
        environment={
            "LD_LIBRARY_PATH": "/opt/mesa/lib",
            "VK_DRIVER_FILES": "/opt/mesa/share/vulkan/icd.d/intel_icd.x86_64.json",
            "MESA_SHADER_CACHE_DISABLE": "1",
        },
    )


def test_save_and_load_worker_manifest(tmp_path: Path):
    """A WorkerManifest should survive a save/load round-trip."""

    manifest = create_worker_manifest()
    manifest_file = tmp_path / "worker-manifest.json"
    save_worker_manifest(manifest, manifest_file)
    loaded = load_worker_manifest(manifest_file)

    assert loaded == manifest


def test_invalid_manifest_version(tmp_path: Path):
    """Unsupported manifest versions must be rejected."""

    manifest_file = tmp_path / "worker-manifest.json"

    manifest_file.write_text(
        """
{
    "manifest_version": 2,
    "worker_manifest_id": "wm-000001",
    "build_manifest_id": "bm-000001",
    "shard_id": "shard-0001",
    "environment": {}
}
"""
    )

    with pytest.raises(ValidationError):
        load_worker_manifest(manifest_file)

def test_missing_build_manifest_id(tmp_path: Path):
    """Missing build_manifest_id should fail validation."""

    manifest_file = tmp_path / "worker-manifest.json"

    manifest_file.write_text(
        """
{
    "manifest_version": 1,
    "worker_manifest_id": "wm-000001",
    "shard_id": "shard-0001",
    "environment": {}
}
"""
    )

    with pytest.raises(ValidationError):
        load_worker_manifest(manifest_file)


def test_missing_shard_id(tmp_path: Path):
    """Missing shard_id should fail validation."""

    manifest_file = tmp_path / "worker-manifest.json"

    manifest_file.write_text(
        """
{
    "manifest_version": 1,
    "worker_manifest_id": "wm-000001",
    "build_manifest_id": "bm-20260702-000001",
    "environment": {}
}
"""
    )

    with pytest.raises(ValidationError):
        load_worker_manifest(manifest_file)

def test_missing_required_field(tmp_path: Path):
    """Missing required fields should raise a ValidationError."""

    manifest_file = tmp_path / "worker-manifest.json"

    manifest_file.write_text(
        """
{
    "manifest_version": 1,
    "worker_manifest_id": "wm-000001",
    "environment": {}
}
"""
    )

    with pytest.raises(ValidationError):
        load_worker_manifest(manifest_file)


def test_environment_is_optional(tmp_path: Path):
    """The environment section may be omitted."""

    manifest_file = tmp_path / "worker-manifest.json"

    manifest_file.write_text(
        """
{
    "manifest_version": 1,
    "worker_manifest_id": "wm-000001",
    "build_manifest_id": "bm-000001",
    "shard_id": "shard-0001"
}
"""
    )

    manifest = load_worker_manifest(manifest_file)

    assert manifest.environment == {}


def test_environment_variables_are_preserved(tmp_path: Path):
    """Environment variables should survive serialization."""

    manifest = create_worker_manifest()

    manifest.environment["FOO"] = "BAR"

    manifest_file = tmp_path / "worker-manifest.json"

    save_worker_manifest(manifest, manifest_file)

    loaded = load_worker_manifest(manifest_file)

    assert loaded.environment["FOO"] == "BAR"