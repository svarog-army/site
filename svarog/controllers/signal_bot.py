import asyncio

from datetime import date


from config import CFG
from svarog.logger import log
from svarog import models as m


def create_new_application_message(application: m.Application) -> str:
    return f"""
    Отримано новий запит на вступ до військової служби: \n
    ПІБ: {application.full_name} \n
    Вік: {date.today().year - application.birth_date.year} \n
    Телефон: {application.phone} \n
    Посилання на анкету: скоро буде
    """


def send_signal_message(
    message: str,
):
    from signalbot import SignalBot

    recipient = CFG.SIGNAL_TO
    signal_bot = SignalBot({"signal_service": f"{CFG.SIGNAL_HOST}:{CFG.SIGNAL_PORT}", "phone_number": CFG.SIGNAL_FROM})
    log(log.INFO, f"Sending message to [{recipient}]")
    message_id = asyncio.run(signal_bot.send(recipient, message))
    log(log.INFO, f"Message [{message_id}] sent to {recipient}")
