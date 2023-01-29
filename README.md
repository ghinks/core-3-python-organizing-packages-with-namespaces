# Plural Sight 

## Core Python 3: Organizing Larger Programs

[link to course](https://app.pluralsight.com/library/courses/core-python-organizing-larger-programs/table-of-contents)

Note the namespace method works based on a search

```python
myModules = [m for _,m,_ in pkgutil.iter_modules(demo_reader.compressed.__path__)]
```

The namespace "demo_reader.compressed" has a path and that path is used to produce a map of extension modules

The following sets up the extension map when demo_reader.compressed namespace is iterated over.

```python
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
```