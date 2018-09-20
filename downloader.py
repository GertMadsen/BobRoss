""" 
If no given parameters will download files from 'list_of_files.txt'

Usage:
    python downloader.py [<url>] [<file_name>]
"""

import os
import sys
from urllib import request as req

# windows_tmp = 'C:\\Users\\Gert Lehmann Madsen\\AppData\\Local\\Temp'
# unix_tmp = '/tmp/'

def download(from_url, to_file): 
    if not os.path.isfile(to_file):
        req.urlretrieve(from_url, to_file)


if __name__ == '__main__':
    try:
        _, url, file_name = sys.argv
    except:
        try:
            _, url = sys.argv
            file_name = os.path.basename(url)
        except:
            try:
                # open file
                cfg_file = 'list_of_files.txt'
                with open(cfg_file) as fp:
                    for line in fp:
                        file_name = os.path.basename(line.rstrip())
                        url = line
                        download(url, file_name)
                sys.exit(0)    
            except Exception as e:
                print(__doc__)
                sys.exit(1)    
    download(url, file_name)

