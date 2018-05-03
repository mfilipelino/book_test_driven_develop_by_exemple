from unittest import TestCase
from mocks import email_util


class SendEmailTestCase(TestCase):
    def test_send_email(self):
        # Prepare
        body = 'body'
        subject = 'subject'
        from_email = 'my@email.com'
        destination_email = 'you@email.com'

        # mocks
        self.send_email_false = False

        def fake_send_mail(subject, body, from_email, destination_email):
            self.send_email_called = True
            self.subject = subject
            self.body = body
            self.from_email = from_email
            self.destination_email = destination_email

        email_util._send_email = fake_send_mail

        # Act
        result = email_util.send_email(
            body=body,
            subject=subject,
            from_email=from_email,
            destination_email=destination_email,
        )

        # Asserts
        self.assertTrue(self.send_email_called)
        self.assertTrue(result)