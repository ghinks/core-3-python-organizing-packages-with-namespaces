import setuptools

setuptools.setup(
    name="demo_reader_gz_plugin",
    version="0.0.0",
    description="demo_reader_bz2 plugin for reading gz files",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    entry_points={
        'demo_reader.compression_plugins':
            [
                'gz = demo_reader_gz.gzipped'
            ]
    }
)
