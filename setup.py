from setuptools import setup

setup(name = 'hex',
      version = '1',
      description = 'Hexapod Robot Code',
      url = 'http://github.com/cbvpt/hex',
      author = 'cbvpt',
      author_email = 'cbvpt1@gmail.com',
      license = 'Mine',
      packages = ['hex', 'hex.robot', 'hex.demo', 'hex.comm'],
      zip_safe = False)
