from enum import StrEnum


class Component(StrEnum):
    MESA = "mesa"
    VULKAN_CTS = "vulkancts"
    PIGLIT = "piglit"
    IGT = "igt"

    KERNEL = "kernel"
    FIRMWARE = "firmware"
    TOOLS = "tools"