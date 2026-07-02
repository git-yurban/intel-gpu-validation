class ArtifactManager:

    def __init__(self, config):
        self.config = config

    async def prepare(self, manifest):
        raise NotImplementedError()

    def path(self, component):
        raise NotImplementedError()