from distutils.core import setup

setup(
    name='py_bandcamp',
    version='0.7.0',
    packages=['py_bandcamp'],
    install_requires=["beautifulsoup4", "requests", "requests_cache"],
    url='https://github.com/OpenJarbas/py_bandcamp',
    license='Apache2',
    author='jarbasAI',
    author_email='jarbasai@mailfence.com',
    description='bandcamp data scrapper'
)
