from setuptools import setup

setup(
    name='mypkg.egg-info',
    version='3.8',
    Author='Masande Gontyeleni',
    author_email='masandegontyeleni@gmail.com',
    packages='["mypkg.egg-info", "mypkg.egg-info.test]',
    scripts='["bin/script1","bin/script2]',
    url='http://pypi.python.org/pypi/End_Of_Module/mypkg',
    license='LICENSE.txt',
    description='A programme that generates lotto numbers ',
    long_description=open('README').read(),
    install_requires=["Django>=1.1.1", "pytest"]
)
