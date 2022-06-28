# !/usr/bin/env python3
import configparser
import smtplib
import ssl

WPE_CNF = '/home/kcarey_/gmail_project/prodAws.cnf'


class SendGmailForServiceDown:

    def __init__(self, service):
        self.service = service

    def send_mail(self):
        config = configparser.ConfigParser()
        config.read(WPE_CNF)

        port = config.get('gmail_alerts', 'port')
        smtp_server = config.get('gmail_alerts', 'smtp_server')
        sender_email = config.get('gmail_alerts', 'sender_email')
        receiver_email = config.get('gmail_alerts', 'receiver_email')
        password = config.get('gmail_alerts', 'pass')
        message = f"""
        Subject: Hi there

        {self.service } is currently down go fix it...."""

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

nginx = SendGmailForServiceDown("Nginx")
nginx.send_mail()

