import setuptools

with open("README.md", "r") as fh:
	description = fh.read()

setuptools.setup(
	name="test-package",
	version="0.0.1",
	author="sunny kumar",
	author_email="sunnykumar1516@gmail.com",
	packages=["test_package"],
	description="A sample test package",
	long_description=description,
	long_description_content_type="text/markdown",
	url="https://github.com/sunnykumar1516/testenvforpackage",
	license='MIT',
	python_requires='>=3.8',
	install_requires=[]
)
