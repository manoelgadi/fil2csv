from setuptools import setup

setup(name='fil2csv',
      version='0.1',  # Development release
      description='Library to convert .FIL (List of database objects stored in a database; created by early versions of dBASE, as well as ACL for Windows) to csv for later use with pandas DataFrame.',
      url='https://github.com/manoelgadi/fil2csv',
      author='Prof. Manoel Gadi',
      author_email='mfalonso@faculty.ie.edu',
      license='MIT',
          packages=['fil2csv'],
      zip_safe=False)
