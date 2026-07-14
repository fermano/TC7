# Delivery workflow contract

Delivery owner keys are trimmed and lowercased. Blank owners use `engineering-ops`.

Owner filters preserve input record order and use the same canonicalization as routing. A missing owner selection means no filtering; an explicitly empty selection returns no records. Duplicate selections do not duplicate results.

Delivery summaries expose owner and status. Source metadata may be added as an opt-in field; behavior for blank or missing source values is not yet recorded here.
