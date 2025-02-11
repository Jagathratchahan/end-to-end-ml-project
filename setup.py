'''
This setup.py file is used to package and distribute your projects'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function return list of requirements """

    reuqirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines = file.readLines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement!= '-e .':
                    reuqirement_list.apppend(requirement)
    except FileNotFoundError:
        print("requirement.txt file not found.")

    return reuqirement_list

setup(
    name="SampleProject",
    version='0.0.1',
    author="Jagathratchahan V",
    author_email="jagathratchahan.2@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
