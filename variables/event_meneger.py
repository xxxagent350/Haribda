from core.Event import Event

from core.text_reactions.start import command_start

text_event = Event()
call_event = Event()

text_event.add_handler(command_start)