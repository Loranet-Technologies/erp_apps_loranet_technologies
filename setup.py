from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in loranet_technologies/__init__.py
from loranet_technologies import __version__ as version

setup(
	name="loranet_technologies",
	version=version,
	description="Loranet Technologies PLT IOT Services",
	author="Loranet",
	author_email="admin@loranet.my",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
