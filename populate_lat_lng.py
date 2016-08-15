#!/usr/bin/python
import os
import what3words
import json

def main():

    try:
        path_to_data = os.environ['PATH_TO_CAPTURES']
    except KeyError:
        print 'Please set the environment variable WHAT3WORDS_API_KEY'
        return 1
    locations = [name for name in os.listdir(path_to_data) if os.path.isdir(os.path.join(path_to_data, name))]

    try:
        w3w_api_key = os.environ['WHAT3WORDS_API_KEY']
    except KeyError:
        print 'Please set the environment variable WHAT3WORDS_API_KEY'
        return 1

    # w3w client
    w3w = what3words.Geocoder(w3w_api_key)

    for directory in locations:
        w3w_location = directory.replace("-", ".")

        # get latitude and longitude from w3w
        res = w3w.forward(addr=w3w_location)
        lat = res['geometry']['lat']
        lng = res['geometry']['lng']

        # get path to each manifest
        manifest_path = os.path.join(path_to_data, directory, 'manifest.json')
        json_file = open(manifest_path, 'r')
        json_original = json.load(json_file)
        json_original['latitude'] = lat
        json_original['longitude'] = lng

        # push these values to the manifest
        with open(manifest_path, 'w') as json_file:
            json.dump(json_original, json_file)

if __name__ == '__main__':
    main()
