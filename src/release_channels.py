DEFAULT_RELEASE_CHANNEL = "internal"


def resolve_release_channel(channel: str | None) -> str:
    """Return a normalized release channel, defaulting blank values."""
    normalized = (channel or "").strip().lower()
    return normalized or DEFAULT_RELEASE_CHANNEL
