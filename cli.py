import os;
import curses;
import urllib.request;
from lib.Window import Window;
from lib.CacheHelper import CacheHelper;
from lib.ModuleLoader import ModuleLoader;
from lib.KeyActionFactory import KeyActionFactory;

def __init__():
	curses.start_color();
	curses.use_default_colors();
	# Check cache, otherwise cache important items
	file = os.path.isfile("./cache/.cached");
	if file:
		Cache.LoadCache();
	else:
		Cache.GenerateCache();

def __main__(win):
	__init__();
	window = Window(win);
	kaf = KeyActionFactory(window);
	
	while window.isRunning():
		kaf.Run();

curses.wrapper(__main__);
