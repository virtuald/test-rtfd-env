# this is a dirty hack to convince readthedocs to install a specific
# version of our software. We assume that this will always be triggered
# on a specific version

from setuptools import setup

package = "wpilib"
version = "2021.2.1.0"

setup(
    name="dummy-package",
    version="1.0",
    install_requires=["%s==%s" % (package, version)],
)
