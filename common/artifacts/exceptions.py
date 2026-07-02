class ArtifactError(Exception):
    pass


class ManifestError(ArtifactError):
    pass


class VerificationError(ArtifactError):
    pass


class CacheError(ArtifactError):
    pass

class DownloadError(ArtifactError):
    pass