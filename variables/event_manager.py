from models.event import Event

from core.text_reactions.start import command_start
from core.text_reactions.map import command_map
from core.call_reactions.arrow import arrow

text_event = Event()
call_event = Event()

text_event.add_handler(command_start)
text_event.add_handler(command_map)

call_event.add_handler(arrow)