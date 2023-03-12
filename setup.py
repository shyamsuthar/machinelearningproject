from setuptools import find_packages,setup
from typing import List
def get_requirement(file_path:str)-> List[str]:
    '''
    this function will return the list of requirements
    '''
    HYPEN_EDOT ='-e .'
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements =[req.replace('/n','') for req in requirements]

        if HYPEN_EDOT  in requirements:
            requirements.remove(HYPEN_EDOT)

    return requirements


setup(
    name = 'machinelearningproject',
    version = '0.0.1',
    author ='shyam suthar',
    author_email = 'shyamsuthar06@gmail.com',
    packages = find_packages(),
    install_requires =get_requirement('requirements.txt')



)