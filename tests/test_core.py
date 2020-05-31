import unittest


class LgtmTest(unittest.TestCase):
    @unittest.skip("skip")
    def test_lgtm(self):
        from lgtm.core import lgtm

        self.assertIsNone(lgtm("python", "LGTM"))
