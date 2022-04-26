"""
messenger.py

Created by Stephen Andrews, April 26th, 2022.
"""
from twilio.rest import Client

from app.constants import APP_NAME


class Messenger:

    def __init__(self) -> None:
        self.account_sid = 'AC1334c10bd35a7dd766e769a2e46f9289'
        self.auth_token = '8815b89803406c7c8746e73f39a78444'

        self.client: Client = None

    def __enter__(self) -> 'Messenger':
        self.client = Client(self.account_sid, self.auth_token)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        pass

    def send(self, to: str, msg: str) -> None:
        """
        Send an SMS via Twilio API.

        :param to: The number to send the message to including a country code prefix.
        :param msg: The message content to send.
        """
        separator = '-' * len(APP_NAME)
        body = f"""{APP_NAME}
        {separator}

        {msg}
        """.strip()

        self.client.messages.create(
            body=body,
            from_='+18608913251',
            to=to
        )


# Example usage
if __name__ == '__main__':
    messanger: Messenger

    with Messenger() as messenger:
        messenger.send('+16034258689', 'hi baby girl <3')
