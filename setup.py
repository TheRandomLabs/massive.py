import pathlib

from setuptools import find_namespace_packages, setup

CURRENT_DIRECTORY = pathlib.Path(__file__).parent
README = (CURRENT_DIRECTORY / "README.md").read_text()

setup(
	name="massive.py",
	version="0.2.3",
	description="Utilities for converting text to massive text, especially on Discord.",
	long_description=README,
	long_description_content_type="text/markdown",
	keywords="massive text discord",
	url="https://github.com/TheRandomLabs/massive.py",
	project_urls={
		"Bug Tracker": "https://github.com/TheRandomLabs/massive.py/issues",
		"Source Code": "https://github.com/TheRandomLabs/massive.py"
	},
	author="TheRandomLabs",
	author_email="therandomlabsinc@gmail.com",
	license="MIT",
	classifiers=[
		"Development Status :: 4 - Beta",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 3.7",
	],
	packages=find_namespace_packages()
)
