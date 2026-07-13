from datetime import datetime, timedelta


def is_review_stale(
    updated_at: datetime,
    now: datetime,
    stale_after_days: int = 5,
) -> bool:
    """Return whether a review has reached the configured stale threshold."""
    if stale_after_days < 0:
        raise ValueError("stale review threshold cannot be negative")
    if (updated_at.utcoffset() is None) != (now.utcoffset() is None):
        raise ValueError("review timestamps must use matching timezone awareness")
    return now - updated_at >= timedelta(days=stale_after_days)
