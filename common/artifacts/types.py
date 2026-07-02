from typing import Annotated

from pydantic import Field

GitSha = Annotated[
    str,
    Field(
        pattern=r"^[0-9a-f]{40}$",
        description="Full 40-character Git SHA",
    ),
]

Sha256 = Annotated[
    str,
    Field(
        pattern=r"^[0-9a-f]{64}$",
        description="SHA256 checksum",
    ),
]
