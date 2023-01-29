import setuptools

setuptools.setup(
    name="demo_reader",
    verson="1.0.0",
    description="Tools for reading various file imports",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"}
)
