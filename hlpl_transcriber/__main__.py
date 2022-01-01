
import configparser
import sys
import os

def get_hlpl_templater__version(case):
    config = configparser.ConfigParser()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(current_directory, 'setup.cfg')
    config.read(config_file_path)
    if case=='version':
       return config['hlpl_transcriber']['version']
    if case=='else':
       return config['hlpl_transcriber']['version']+'\n'+config['hlpl_transcriber']['author']+'\n'+config['hlpl_transcriber']['email']+'\n'+config['hlpl_transcriber']['url']+'\n'
       
 
    
def main():
    if 'version' in sys.argv:
        print('\n'+get_hlpl_templater__version('version'))
    else:
        print('\n'+get_hlpl_templater__version('else')+'\n'+'hlpl_transcriber under developement, it will be released next versions of HLPL')