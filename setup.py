#!python3
import ast
from pathlib import Path

from setuptools import setup


source = Path(__file__).with_name("irsdk.py").read_text(encoding="utf-8")
module = ast.parse(source)

for node in module.body:
    if isinstance(node, ast.Assign) and any(
        isinstance(target, ast.Name) and target.id == "VERSION"
        for target in node.targets
    ):
        VERSION = ast.literal_eval(node.value)
        break
else:
    raise RuntimeError("VERSION is not defined in irsdk.py")

setup(
    name='pyirsdk',
    version=VERSION,
    description='Python 3 implementation of iRacing SDK',
    author='Mihail Latyshov',
    author_email='kutu182@gmail.com',
    url='https://github.com/kutu/pyirsdk',
    py_modules=['irsdk'],
    license='MIT',
    platforms=['win64'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
    ],
    entry_points={
        'console_scripts': ['irsdk = irsdk:main'],
    },
    install_requires=[
        'PyYAML >= 5.3',
    ],
)
