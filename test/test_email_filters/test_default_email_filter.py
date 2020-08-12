import unittest

from extract_emails.email_filters import DefaultEmailFilter


class TestDefaultEmailFilter(unittest.TestCase):
    def test_filter(self):
        e = DefaultEmailFilter()
        self.assertEqual(
            e.filter(
                ["blah@blah.com", "blah@blah.com", "e@gmail.blah", "myemail@gmail.com",]
            ),
            ["blah@blah.com", "myemail@gmail.com"],
        )
