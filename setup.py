import setuptools

options = dict(
    name = "boisgera-pioupiou",
    version = "0.0a11",
    license = "MIT License",
    description = "A nano probabilistic programming language for Python",
    author = "Sébastien Boisgérault",
    author_email = "Sebastien.Boisgerault@mines-paristech.fr",
    url = "https://github.com/boisgera/pioupiou",
    classifiers = [
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    python_requires=">=3.8",
)

with open("README.md", "r", encoding="utf-8") as README:
    options["long_description"] = README.read()
options["long_description_content_type"] = "text/markdown"

options["packages"] = setuptools.find_packages()

options["install_requires"] = ["numpy", "wrapt"],

setuptools.setup(**options)