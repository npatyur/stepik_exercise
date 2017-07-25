from distutils.core import setup
from setuptools import find_packages

setup(
    name='stepik_exercise',
    packages=find_packages(exclude=['test', '*.test', '*.test.*']),
    version='1.0',
    description='Stepik PyPI exercise',
    author='{{your_username}}',
    author_email='{{your@mail.ru}}',
    url='https://github.com/{{your_username}}/stepik_exercise',
    download_url='https://github.com/{{your_username}}/stepik_exercise/archive/1.0.tar.gz',
    keywords=['pypi', 'python'],
    scripts=['bin/stepik_exercise'],
    install_requires=['scipy']
)
