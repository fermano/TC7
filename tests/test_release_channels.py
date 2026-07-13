import unittest

from src.release_channels import DEFAULT_RELEASE_CHANNEL, resolve_release_channel


class ReleaseChannelTests(unittest.TestCase):
    def test_blank_channel_uses_internal_default(self):
        self.assertEqual(resolve_release_channel("   "), DEFAULT_RELEASE_CHANNEL)

    def test_channel_is_normalized(self):
        self.assertEqual(resolve_release_channel(" Canary "), "canary")


if __name__ == "__main__":
    unittest.main()
