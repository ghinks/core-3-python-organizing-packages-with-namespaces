# Plural Sight 

## Core Python 3: Organizing Larger Programs

[link to course](https://app.pluralsight.com/library/courses/core-python-organizing-larger-programs/table-of-contents)

Note the namespace method works based on a search

```python
myModules = [m for _,m,_ in pkgutil.iter_modules(demo_reader.compressed.__path__)]
```

The namespace "demo_reader.compressed" has a path and that path is used to produce a map of extension modules