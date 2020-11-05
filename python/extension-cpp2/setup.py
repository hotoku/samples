from distutils.core import setup, Extension

module1 = Extension('hoge',
                    sources=['hoge.cpp'])

setup(name='hoge',
      version='1.0',
      description='This is a demo package',
      ext_modules=[module1])
