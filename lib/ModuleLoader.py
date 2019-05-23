from os import walk;
import toml;

class ModuleLoader:
    path = "";
    modules = [];
    parsed = [];

    # Load the available module TOML files in to prepare for parse.
    def __init__(self, path='./lib/Modules'):
        self.path = path;
        for (dirpath, dirnames, filenames) in walk(self.path):
            self.modules.extend(filenames);
            break;

    # Parse the found TOML modules to dictionaries for easy loading.
    def parse(self):
        for module in self.modules:
            self.parsed.extend(toml.loads(open(self.path + "/" + module, 'r').read()));
        return self.parsed;