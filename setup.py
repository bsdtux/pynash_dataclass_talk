from setuptools import setup


setup(
    name='battle',
    version='1.0',
    py_modules=['battle'],
    install_requires=[
        'Click',
    ],
    entry_points='''
    [console_scripts]
    battle=battle:cli
    '''
)
