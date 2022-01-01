#! /usr/bin/python 
from setuptools  import setup
import os
import sys
import platform
import configparser

from io import open
# to install type:
# python setup.py install --root=/
LONG_DESCRIPTION=open('README.md','r',encoding='utf8').read()        
        
if sys.version_info[0] < 3:
    raise Exception(
        'You are tying to install hlpl_transcriber on Python version {}.\n'
        'Please install hlpl_transcriber in Python 3 instead.'.format(
            platform.python_version()
        )
    )
    
config = configparser.ConfigParser()
current_directory = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_directory, 'hlpl_transcriber/setup.cfg')
config.read(config_file_path)

VERSION = config['hlpl_transcriber']['version']
AUTHOR = config['hlpl_transcriber']['author']
AUTHOR_EMAIL = config['hlpl_transcriber']['email']
URL = config['hlpl_transcriber']['url']


projects_urls={}
for i in range(4,len(list(config['hlpl_transcriber'].keys()))):
    x=list(config['hlpl_transcriber'].keys())[i]
    y=x
    if i>3:
       y=y[0:len(y)-4]
    projects_urls[y]=config['hlpl_transcriber'][x]
    

setup (name='hlpl_transcriber', version=VERSION,
      description='Text Transcriber',
      long_description_content_type='text/markdown',  
      long_description = LONG_DESCRIPTION,       
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      download_url=URL+'/download/',
      project_urls=projects_urls,      
      python_requires='>=3, <=3.9',
      license='MIT',
      platform="OS independent",
      keywords=['hlpl_transcriber', 'hlpl transcriber', 'hlpl-transcriber', 'text transcriber', 'hlpl'],
      package_dir={'hlpl_transcriber': 'hlpl_transcriber',},
      packages=['hlpl_transcriber',],
      install_requires=[],         
      include_package_data=True,
      entry_points ={
        'console_scripts': [
                'hlpl_transcriber = hlpl_transcriber.__main__:main',
            ]},   
      classifiers=[
          'Framework :: Robot Framework',
          'Framework :: Robot Framework :: Library',
          'Framework :: Robot Framework :: Tool',
          'Natural Language :: Arabic',
          'Natural Language :: English',
          ],
                  
    );
