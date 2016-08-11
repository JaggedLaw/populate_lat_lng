#!/usr/bin/python
import os

def main():

    path_to_data = '/home/density/gathered-data/'
    print path_to_data
    locations = [name for name in os.listdir(path_to_data) if os.path.isdir(os.path.join(path_to_data, name))]

    try:
        THREE_WORDS_KEY = os.environ['WHAT3WORDS_API_KEY']
    except KeyError:
        print 'Please set the environment variable WHAT3WORDS_API_KEY'
        return 1

    for directory in locations:
        print directory
        # get path to each manifest
        # make api request for locations latitude and longitude
        # push these values to the manifest

if __name__ == '__main__':
    main()
