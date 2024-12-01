from models.event import Event

from UI.text_reactions.start_reaction import command_start
from UI.text_reactions.map_reaction import map_button_reaction
from UI.call_reactions.arrows_reaction import arrow

text_event = Event()
call_event = Event()

text_event.add_handler(command_start)
text_event.add_handler(map_button_reaction)

call_event.add_handler(arrow)