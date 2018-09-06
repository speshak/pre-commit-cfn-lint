from setuptools import find_packages
from setuptools import setup


setup(
    name='cfn_lint_pre_commit',
    version='0.2.0',
    install_requires=['cfn-lint'],
    packages=find_packages(exclude=('tests*', 'testing*')),
    entry_points={
        'console_scripts': [
            'cfn-lint-wrapper = cfn_lint_pre_commit.cfn_lint_wrapper:main'
        ]
    },
)
