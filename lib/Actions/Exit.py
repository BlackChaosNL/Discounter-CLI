from .Action import Action;

class Exit(Action):
	def Run(self, window):
		window.setRunning(False);
