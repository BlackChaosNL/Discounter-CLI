from .Action import Action;

class MoveDown(Action):
	def Run(self, window):
		window.write('MoveDownAction');
