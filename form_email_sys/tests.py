from django.test import TestCase

# Create your tests here.
from django.core.mail import send_mail
from django.test import TestCase

class EmailTest(TestCase):
    def test_send_email(self):
        send_mail(
            'Test Email',
            'This is a test email.',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )
        # Assert that an email was sent
        self.assertEqual(len(mail.outbox), 1)
        # Check email details
        self.assertEqual(mail.outbox[0].subject, 'Test Email')
