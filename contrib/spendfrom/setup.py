from distutils.core import setup
setup(name='btcspendfrom',
      version='1.0',
      description='Command-line utility for barnacoin "coin control"',
      author='Gavin Andresen',
      author_email='gavin@barnacoinfoundation.org',
      requires=['jsonrpc'],
      scripts=['spendfrom.py'],
      )
