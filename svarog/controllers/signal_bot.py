import asyncio

from svarog.logger import log


def send_message(
    message: str,
):
    from signalbot import SignalBot
    from config import config

    CFG = config()

    recipient = CFG.SIGNAL_TO
    signal_bot = SignalBot({"signal_service": f"{CFG.SIGNAL_HOST}:{CFG.SIGNAL_PORT}", "phone_number": CFG.SIGNAL_FROM})
    log(log.INFO, f"Sending message to [{recipient}]")
    message_id = asyncio.run(signal_bot.send(recipient, message))
    log(log.INFO, f"Message [{message_id}] sent to {recipient}")
