from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='Deep Learning for NLP Task',
version='0.0.0',
author='Himanshu',
author_email='986himanshusharma@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),
python_requires='>=3.11'

)