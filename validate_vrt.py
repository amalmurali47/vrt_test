#!/usr/bin/env python
import json
import jsonschema
import sys
import validate_deprecated_mapping
import subprocess
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

def is_changelog_updated():
    '''
    Checks if CHANGELOG.md is being updated with the current commit
    and prompts the user if it isn't
    '''
    p = subprocess.Popen("git diff HEAD --stat --staged CHANGELOG.md | wc -l", shell=True, stdout=subprocess.PIPE)
    out, err = p.communicate()
    if not int(out):
        print('\n########## Make sure to update CHANGELOG.md! ##########\n')

def validate_schema(schema_file, data_file):
    schema = get_json(schema_file)
    data = get_json(data_file)
    if schema and data:
        Draft4Validator.check_schema(schema)
         # Get the most relevant validation error to produce sensical output
        error = best_match(Draft4Validator(schema).iter_errors(data))
        if error:
            print(error)
            sys.exit(1)
        else:
            print('JSON validation success!')

def has_mapping(mapping, id_list, key):
    if key in mapping:
        return True
    elif 'children' in mapping:
        return has_mapping(mapping['children'], id_list, key)
    elif len(id_list) > 0 and id_list[0] in mapping:
        return has_mapping(mapping[id_list[0]], id_list[1:], key)
    else:
        return False

def key_by_id(mapping):
    if isinstance(mapping, list):
        return {x['id']: key_by_id(x) for x in mapping}
    elif isinstance(mapping, dict):
        return {k: key_by_id(v) for k, v in mapping.iteritems()}
    else:
        return mapping

# gets a list of ids in dotted notation, including internal nodes
#
# contains a leading . on every id but it doesn't matter in this instance
def flatten_ids(vrt, prefix):
    if isinstance(vrt, list):
        return [vrt_id for entry in vrt for vrt_id in flatten_ids(entry, prefix)]
    elif isinstance(vrt, dict):
        if 'children' in vrt:
            return [prefix + '.' + vrt['id']] + flatten_ids(vrt['children'], prefix + '.' + vrt['id'])
        else:
            return [prefix + '.' + vrt['id']]
    else:
        print(vrt)
        raise Exception('unexpected entry found')

def validate_mappings(vrt_file, mapping_file, key):
    vrt = get_json(vrt_file)
    mapping = get_json(mapping_file)
    keyed_mapping = key_by_id(mapping['content'])

    def validate_vrt_has_mapping(vrt_list, parent_ids):
        for entry in vrt_list:
            ids = parent_ids + [entry['id']]
            if 'children' in entry:
                validate_vrt_has_mapping(entry['children'], ids)
            else:
                if not has_mapping(keyed_mapping, ids, key):
                    print('missing %s mapping for %s' % (key, '.'.join(ids)))
                    sys.exit(1)

    validate_vrt_has_mapping(vrt['content'], [])
    print("All VRT nodes have %s mappings" % key)

    unexpected_ids = set(flatten_ids(mapping['content'], '')).difference(flatten_ids(vrt['content'], ''))
    if len(unexpected_ids) > 0:
        print("Unknown ids found in mapping:\n    %s" % "\n    ".join(unexpected_ids))
        sys.exit(1)

def main():
    validate_schema("vrt.schema.json", "vulnerability-rating-taxonomy.json")
    validate_schema("mappings/cvss_v3.schema.json", "mappings/cvss_v3.json")
    validate_mappings("vulnerability-rating-taxonomy.json", "mappings/cvss_v3.json", "cvss_v3")
    is_changelog_updated()

    errors = validate_deprecated_mapping.main()
    if errors:
        print '\nErrors:'
        sys.exit(errors)
    else:
        print 'All Good!'
        return True

if __name__ == '__main__':
    main()
