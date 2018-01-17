try:
    from setuptools import setup
except ImportError:
    try:
        import ez_setup
        ez_setup.use_setuptools()
    except ImportError:
        raise ImportError("CairoDrawBot could not be installed, probably because"
            " neither setuptools nor ez_setup are installed on this computer."
            "\nInstall ez_setup ([sudo] pip install ez_setup) and try again.")

from setuptools import setup, find_packages

exec(open('cairodrawbot/version.py').read()) # loads __version__

setup(name='cairodrawbot',
    version=__version__,
    author='EliH',
    description='DrawBot for GNU+Linux',
    long_description=open('README.md').read(),
    license='see LICENSE',
    keywords="Cairo vector graphics",
    install_requires=['cairocffi', 'numpy'],
    packages= find_packages(exclude='docs'))
