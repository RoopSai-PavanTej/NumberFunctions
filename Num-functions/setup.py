from setuptools import setup

def readme():
	with open('README.md') as f:
		README = f.read()
	return README

setup(
	name="Num-functions",
	version="1.0.0",
	description="A Python Package of various Number Functions for computing them",
	long_description=readme(),
	long_description_content_type="text/markdown",
	url="https://https://github.com/RoopSai-PavanTej/NumberFunctions",
	author="Roop Sai Pavan Tej Pendyala",
	author_email="roopsai84@gmail.com",
	license="MIT",
	classifiers=[
		"License :: OSI Approved :: MIT License ",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.7",
	],
	packages=["Num_functions"],
	include_package_data=True,
	entry_points={
		"console_scripts":[
			"Num-functions=Num_functions.Numfunctions"
		]
	},

)