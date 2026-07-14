# Delivery workflow contract

Delivery owner keys are trimmed and lowercased. Blank owners use `engineering-ops`.

Owner filters preserve input record order and use the same canonicalization as routing. A missing owner selection means no filtering; an explicitly empty selection returns no records. Duplicate selections do not duplicate results.

Delivery summaries expose owner and status by default. Callers may opt in to source metadata. Opted-in source values are trimmed; missing or blank sources are omitted rather than synthesized.
