from setuptools import setup


setup(
    name='simulator',
    version='1.0',
    py_modules=['simulator'],
    install_requires=[
        'Click',
    ],
    entry_points='''
    [console_scripts]
    simulator=simulator:cli
    '''
)
