import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="WonderPyWindows",
    version="0.0.1",
    author="James Truxon",
    author_email="james@modeic.com",
    description="Windows port of Python API for working with Wonder Workshop robots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jtruxon/WonderPy",
    packages=setuptools.find_packages(),
    package_data={'WonderPy': ['lib/WonderWorkshop/osx/*.dylib']},
    classifiers=(
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Environment :: Windows",
        "Framework :: Robot Framework",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
        "Programming Language :: Python :: 3.5",
    ),
    keywords=['robots', 'dash', 'dot', 'cue', 'wonder workshop', 'robotics', 'sketchkit',],
    test_suite='test',
    install_requires=['mock', 'svgpathtools','bleak'],
    # this also requires pip install git+git://github.com/playi/Adafruit_Python_BluefruitLE@928669a#egg=Adafruit_BluefruitLE
)
