#!/usr/bin/env python
import json
import jsonschema
import sys
from jsonschema import Draft4Validator
from jsonschema.exceptions import best_match

def get_json(filename):
    '''
    Returns deserialized JSON if the input file is a valid JSON
    or exits with an error otherwise
    '''
    try:
        return json.loads(open(filename).read())
    except ValueError as e:
        print('Error: Not a valid JSON file:', filename)
        sys.exit(e)

def main():
    vrt_schema = get_json("vrt.schema.json")
    vrt_json = get_json("vulnerability-rating-taxonomy.json")

    # Validate the VRT against the schema
    if vrt_schema and vrt_json:
        # Get the most relevant validation error to produce sensical output
        error = best_match(Draft4Validator(vrt_schema).iter_errors(vrt_json))
        if error:
            print(error)
            sys.exit(1)
        else:
            print('JSON validation success!')

if __name__ == '__main__':
    main()
