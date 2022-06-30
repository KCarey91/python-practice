# !/usr/bin/env python3
import configparser
import smtplib
import ssl

WPE_CNF = '/home/kcarey_/gmail_project/prodAws.cnf'

class Message():
    def __init__(self, config):
        self.port = config.get('gmail_alerts', 'port')
        self.smtp_server = config.get('gmail_alerts', 'smtp_server')
        self.sender_email = config.get('gmail_alerts', 'sender_email')
        self.receiver_email = config.get('gmail_alerts', 'receiver_email')
        self.password = config.get('gmail_alerts', 'pass')

    def get_attrs(self) -> dict:
        my_attrs: dict = {"port": self.port, "smtp_server": self.smtp_server}
    
my_message = Message(config)
my_message.port

all_attrs = my_message.get_attrs()

my_port = all_attrs.get("port")


class SendGmailForServiceDown:
    def create_mesage(service):
        #set variables that will be used to send the mail
        message = f"""
        Subject: Hi there

        { service } is currently down go fix it...."""

        context = ssl.create_default_context()

        return context

    def send_mail(message_context, message_body):
        """Send Mail for down server

        :param container_name: the name of the container
        :return: None
        """
        # Read the config and pull variables needed for sending mail
        

        with smtplib.SMTP_SSL(message_body.smtp_server, message_body.port, context=message_context) as server:
            server.login(message_body.sender_email, message_body.password)
            server.sendmail(message_body.sender_email, message_body.receiver_email, message_context)

def main(service):
    config = configparser.ConfigParser()
    config.read(WPE_CNF)
    
    message_body = Message(config)
    message_to_send = SendGmailForServiceDown.create_mesage(service)
    
    try:
        SendGmailForServiceDown.send_email(message_to_send, message_body)
    except:
        print('error sending the email')