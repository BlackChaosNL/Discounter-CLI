class Window:
	window = '';
	running = True;
	
	def __init__(self, window):
		self.window = window;
		self.window.nodelay(True);

	def Draw(self):
		pass;	

	def write(self, str):
		self.window.addstr(str);

	def getWindow(self):
		return self.window;

	def isRunning(self):
		return self.running;

	def setRunning(self, running):
		self.running = running;
