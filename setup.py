import pathlib

from setuptools import find_namespace_packages, setup

CURRENT_DIRECTORY = pathlib.Path(__file__).parent
README = (CURRENT_DIRECTORY / "README.md").read_text()

setup(
	name="massive.py",
	version="1.0.0",
	description="Utillities for converting text to MASSIVE text, especially on Discord.",
	long_description=README,
	long_description_content_type="text/markdown",
	keywords="massive text discord",
	url="https://github.com/TheRandomLabs/massive.py",
	project_urls={
		"Bug Tracker": "https://github.com/TheRandomLabs/massive.py/issues",
		"Documentation": "https://github.com/TheRandomLabs/massive.py/wiki",
		"Source Code": "https://github.com/TheRandomLabs/massive.py"
	},
	download_url="https://github.com/TheRandomLabs/massive.py/v1.0.0.tar.gz",
	author="TheRandomLabs",
	author_email="therandomlabsinc@gmail.com",
	license="MIT",
	classifiers=[
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.7",
	],
	packages=find_namespace_packages()
)
