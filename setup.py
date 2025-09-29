from setuptools import find_packages,setup
from typing import List

HyphenE = "-e ."
def get_requirements(find_path:str)->List[str]:
    requirements = []
    with open(find_path) as f:
        requirements= f.readlines()
        requirements = [r.replace("\n", "") for r in requirements]
        
        if HyphenE in requirements:
            # Remove editable install flag from install_requires list
            requirements.remove(HyphenE)
    return requirements
        

setup(
name='endtoend-mlproject',
version='0.0.1',
author='Swetha Srinivasan',
author_email='srinivasswetha85@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)