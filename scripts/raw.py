# Python bytecode 3.6 (3379)
# Embedded file name: run.py
# Compiled at: 2019-03-16 07:21:36
# Size of source mod 2**32: 2060 bytes
from notebook.auth import passwd
import os
os.system('clear')
os.system('echo')
print('This script is written by Yi Ru.')
print('If you got troubles running this script, please go upstairs and ask him ;-)\n')
input('Press Enter to continue, or Ctrl + Z to quit.\n')
print('Start setting up your Jupyter Notebook for ssh access...\n')

os.system('cd ~')
os.system('jupyter-notebook --generate-config')
print('\n')

print('Setting your Notebook IP...')
os.system('\nsed -i "/NotebookApp.ip/s/#c.NotebookApp.ip = \'localhost\'/c.NotebookApp.ip = \'140.232.230.73\'/g" ~/.jupyter/*.py\n')

print("IP address is now link to 'ghostrider'.\n")
print('Now please select your port number.')

print('The default port is 8888. However, it might cause conflicts between users when')
print('more than two users trying to log in. 8844, 12345, 2323 are good choice for a')
print('port number. Port number should between 1 and 65535. Please avoid common port')
print('such as 80, 8080, 21, 443, etc.\n')
print('Make your choice now.')
port = input('Input your port: ')
os.system('\nsed -i "/NotebookApp.port/s/#c.NotebookApp.port = 8888/c.NotebookApp.port = %s/g" ~/.jupyter/*.py\n' % port)
print('Your port is set to %s\n' % port)
print('Setting your Notebook connection encryption...')

print('Now generating a sha1 key for notebook authentication. ')
print('If it prompts you for a password, DO NOT input your password, just hit Enter here.')
print('(It just for SHA1 key generation)')

sha1 = passwd()
os.system('\nsed -i "/NotebookApp.password/s/#c.NotebookApp.password = \'\'/c.NotebookApp.password = \'%s\'/g" ~/.jupyter/*.py\n' % sha1)

print('Your Notebook connection now is encrypted.\n')

print('If you want to change these settings, please open ~/.jupyter/jupyter_notebook_config.py to edit.')
print('Bye-bye.')