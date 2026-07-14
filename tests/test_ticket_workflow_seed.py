import unittest

from src.ticket_workflow_seed import (
    DEFAULT_OWNER,
    delivery_summary,
    filter_delivery_records,
    normalize_delivery_owner,
)


class TicketWorkflowSeedTests(unittest.TestCase):
    def test_blank_owner_uses_default(self):
        self.assertEqual(normalize_delivery_owner(None), DEFAULT_OWNER)

    def test_owner_is_trimmed_and_lowercased(self):
        self.assertEqual(normalize_delivery_owner(" Billing-Ops "), "billing-ops")

    def test_repeated_whitespace_is_collapsed(self):
        self.assertEqual(normalize_delivery_owner(" Billing   Ops "), "billing ops")

    def test_unicode_whitespace_is_collapsed(self):
        self.assertEqual(normalize_delivery_owner("Billing\u00a0\tOps"), "billing ops")

    def test_punctuation_is_preserved(self):
        self.assertEqual(normalize_delivery_owner(" Billing/OnCall "), "billing/oncall")

    def test_missing_owner_selection_returns_all_records(self):
        records = [{"owner": "billing-ops"}, {"owner": "platform-ops"}]
        self.assertEqual(filter_delivery_records(records, None), records)

    def test_empty_owner_selection_returns_no_records(self):
        records = [{"owner": "billing-ops"}]
        self.assertEqual(filter_delivery_records(records, []), [])

    def test_owner_filter_normalizes_selection_and_preserves_record_order(self):
        records = [
            {"id": "first", "owner": "Billing  Ops"},
            {"id": "other", "owner": "platform-ops"},
            {"id": "second", "owner": " billing\u00a0ops "},
        ]

        self.assertEqual(
            filter_delivery_records(records, [" BILLING OPS ", "billing\tops"]),
            [records[0], records[2]],
        )

    def test_summary_contains_existing_fields(self):
        self.assertEqual(
            delivery_summary({"owner": " Billing-Ops ", "status": "queued"}),
            {"owner": "billing-ops", "status": "queued"},
        )

    def test_summary_default_shape_ignores_source(self):
        self.assertEqual(
            delivery_summary(
                {"owner": "billing-ops", "status": "queued", "source": "csv"}
            ),
            {"owner": "billing-ops", "status": "queued"},
        )

    def test_summary_includes_trimmed_source_when_requested(self):
        self.assertEqual(
            delivery_summary(
                {"owner": "billing-ops", "status": "queued", "source": " csv "},
                include_source=True,
            ),
            {"owner": "billing-ops", "status": "queued", "source": "csv"},
        )

    def test_summary_omits_missing_or_blank_source_when_requested(self):
        for source in (None, "", "   "):
            with self.subTest(source=source):
                record = {"owner": "billing-ops", "status": "queued"}
                if source is not None:
                    record["source"] = source
                self.assertEqual(
                    delivery_summary(record, include_source=True),
                    {"owner": "billing-ops", "status": "queued"},
                )


if __name__ == "__main__":
    unittest.main()
