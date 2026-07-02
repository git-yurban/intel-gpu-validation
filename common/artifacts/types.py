from typing import Annotated, Literal

from pydantic import Field

GitSha = Annotated[
    str,
    Field(pattern=r"^[0-9a-f]{40}$")
]

Sha256 = Annotated[
    str,
    Field(pattern=r"^[0-9a-f]{64}$")
]