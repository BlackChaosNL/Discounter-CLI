from .Actions.Exit import Exit;
from .Actions.MoveUp import MoveUp;
from .Actions.MoveDown import MoveDown;
from .Actions.Select import Select;
from .Actions.Search import Search;

class KeyActionFactory:
	actions = {
		'q': Exit(),
		'j': MoveUp(),
		'k': MoveDown(),
		's': Select(),
		':': Search()
	};
	window = '';

	def __init__(self, window):
		self.window = window;

	def Run(self):
		try:
			# Get an action based on a key pressed on the keyboard. 
			# Wanted this VIM style, to ease up use.
			# How it works: 
			# * Request a key from Window and map this to a string for eval.
			# * See if this key is registered in the map 
			# * Execute that command.
			# NOTE: If a key is pressed that is not found, an exception will be thrown. This is not mission critical and can be disgarded. 
			self.actions[
				str(
					self.window.getWindow().getkey()
				)
			].Run(self.window);
		except Exception as e:
			pass;

