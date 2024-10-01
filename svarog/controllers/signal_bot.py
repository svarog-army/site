import asyncio

from config import CFG
from svarog.logger import log


def send_signal_message(
    message: str,
):
    from signalbot import SignalBot

    recipient = CFG.SIGNAL_TO
    signal_bot = SignalBot({"signal_service": f"{CFG.SIGNAL_HOST}:{CFG.SIGNAL_PORT}", "phone_number": CFG.SIGNAL_FROM})
    log(log.INFO, f"Sending message to [{recipient}]")
    message_id = asyncio.run(signal_bot.send(recipient, message))
    log(log.INFO, f"Message [{message_id}] sent to {recipient}")
