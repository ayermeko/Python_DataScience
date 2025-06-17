# Python_DataScience

The command ""python setup.py sdist bdist_wheel"" builds a binary distribution of a Python package in the Wheel (.whl) format, which is a built package ready for installation.

or if you do not have setup.py file

but first make sure if you have the build dependencies...

• python3 -m build

After everything is created run

pip install ./dist/ft_package-0.0.1.tar.gz
pip install ./dist/ft_package-0.0.1-py3-none-any.whl