from enum import StrEnum


class Component(StrEnum):
    MESA = "mesa"
    VULKAN_CTS = "vulkancts"
    PIGLIT = "piglit"
    IGT = "igt"


class Compression(StrEnum):
    TAR_ZST = "tar.zst"
