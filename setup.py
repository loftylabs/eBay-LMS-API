from distutils.core import setup

setup(
    name='lmslib',
    version='0.1',
    description='Python Bindings for eBay LMS API. ',
    author='Wesley Hansen',
    author_email='casey@hirelofty.com',
    url='https://github.com/loftylabs/',
    packages=['lmslib'],
    install_requires=[
        'lxml',
        'simplejson',
        'request',
    ],
)
