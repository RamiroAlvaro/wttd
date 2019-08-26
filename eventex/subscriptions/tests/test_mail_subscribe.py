from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Ramiro Alvaro', cpf='12345678901',
                    email='ramiroalvaro@hotmail.com', phone='31-99138-7178')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'ramiroalvaro@hotmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['Ramiro Alvaro', '12345678901',
                    'ramiroalvaro@hotmail.com', '31-99138-7178']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
