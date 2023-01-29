import importlib
import os
import pkgutil
import demo_reader.compressed

def iter_namespace(ns_pkg):
    return pkgutil.iter_modules(
        ns_pkg.__path__,
        ns_pkg.__name__ + ".")

compression_plugins = {
    importlib.import_module(module_name)
    for _, module_name, _
    in iter_namespace(
        demo_reader.compressed)
}

extension_map = {
    module.extension: module.opener
    for module in compression_plugins
}


class MultiReader:
    def __init__(self, filename):
        """following 2 lines for debug only"""
        myModules = [m for _,m,_ in pkgutil.iter_modules(demo_reader.compressed.__path__)]
        print(myModules)
        extension = os.path.splitext(filename)[1]
        opener = extension_map.get(extension, open)
        self.f = opener(filename, 'rt')

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()
