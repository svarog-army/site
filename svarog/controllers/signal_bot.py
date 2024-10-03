import asyncio

from datetime import date


from config import CFG
from svarog.logger import log
from svarog import models as m


def create_new_application_message(application: m.Application) -> str:
    return f"""
    Отримано новий запит на вступ до військової служби:
    ПІБ: {application.full_name}
    Вік: {date.today().year - application.birth_date.year}
    Телефон: {application.phone}
    Посилання на анкету: скоро буде
    """


def send_signal_message(
    message: str,
):
    from signalbot import SignalBot
    # from signalbot import SignalBot, SendMessageError

    # try:
    ensure_event_loop()

    recipient = CFG.SIGNAL_TO
    signal_bot = SignalBot({"signal_service": f"{CFG.SIGNAL_HOST}:{CFG.SIGNAL_PORT}", "phone_number": CFG.SIGNAL_FROM})
    log(log.INFO, f"Sending message to [{recipient}]")
    message_id = asyncio.run(signal_bot.send(recipient, message))
    log(log.INFO, f"Message [{message_id}] sent to {recipient}")
    # except SendMessageError as e:
    # log(log.ERROR, f"Error while sending message: {e}")


def ensure_event_loop():
    try:
        asyncio.get_event_loop()
    except RuntimeError:
        asyncio.set_event_loop(asyncio.new_event_loop())
    return asyncio.get_event_loop()
