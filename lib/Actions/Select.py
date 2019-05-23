from .Action import Action;

class Select(Action):
	def Run(self, window):
		window.write('SelectAction');
