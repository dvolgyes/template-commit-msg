from setuptools import find_packages
from setuptools import setup


setup(
    name='template_commit_msg',
    description='Commit message template',
    url='https://github.com/dvolgyes/template_commit_sync',
    version='0.1.1',

    author='David Volgyes',
    author_email='david.volgyes@ieee.org',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    packages=find_packages(exclude=('tests*', 'testing*')),
    install_requires=[
        'gitpython',
    ],
    entry_points={
        'console_scripts': [
            'template-commit-msg = template_commit_msg.template_commit_msg:main',
        ],
    },
)
