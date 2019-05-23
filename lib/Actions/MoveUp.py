from .Action import Action;

class MoveUp(Action):
	def Run(self, window):
		window.write('MoveUpAction');
