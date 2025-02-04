import json
import git

VRT_FILENAME = 'vulnerability-rating-taxonomy.json'
DEPRECATED_MAPPING_FILENAME = 'deprecated-node-mapping.json'
VRT_SCHEMA_FILENAME = 'vrt.schema.json'
MAPPING_DIR = 'mappings'

SCW_FILENAME = 'secure-code-warrior-links.json'
SCW_DIR = 'remediation_training'
THIRD_PARTY_MAPPING_DIR = 'third-party-mappings'

def get_json(filename):
    with open(filename) as f:
        return json.loads(f.read())

def all_versions(filename):
    """
    Find, open and parse all tagged versions of a json file, including the current version

    :param filename: The filename to find
    :return: a dictionary of all the versions, in the form
        {
            'current': {...},
            '1.0': {...},
            '1.1': {...}
        }
    """
    repo = git.Repo()
    versions = {
        'current': get_json(filename)
    }
    for tag in repo.tags:
        version_dict = repo.git.show('%s:%s' % (tag.name, filename))
        versions[tag.name.strip('v')] = json.loads(version_dict)
    return versions


def id_valid(vrt, id_list):
    """
    Check if a vrt id is valid

    :param vrt: The vrt object
    :param id_list: The vrt id, split into components, eg ['category', 'subcategory', 'variant']
    :return: True/False
    """
    # this is not particularly efficient, but it's more readable than other options so until we need to care...
    return id_list in all_id_lists(vrt)


def has_mapping(mapping, id_list, key):
    """
    Check if a vrt id has a mapping

    :param mapping: The mapping object, keyed by id
    :param id_list: The vrt id, split into components, eg ['category', 'subcategory', 'variant']
    :param key: The mapping key to look for, eg 'cvss_v3'
    :return: True/False
    """
    if key in mapping:
        return True
    elif 'children' in mapping:
        return has_mapping(mapping['children'], id_list, key)
    elif len(id_list) > 0 and id_list[0] in mapping:
        return has_mapping(mapping[id_list[0]], id_list[1:], key)
    else:
        return False


def key_by_id(mapping):
    """
    Converts arrays to hashes keyed by the id attribute for easier lookup. So
        [{'id': 'one', 'foo': 'bar'}, {'id': 'two', 'foo': 'baz'}]
    becomes
        {'one': {'id': 'one', 'foo': 'bar'}, 'two': {'id': 'two', 'foo': 'baz'}}
    """
    if isinstance(mapping, list) and isinstance(mapping[0], dict) and 'id' in mapping[0]:
        return {x['id']: key_by_id(x) for x in mapping}
    elif isinstance(mapping, dict):
        return {k: key_by_id(v) for k, v in mapping.items()}
    else:
        return mapping


def all_id_lists(vrt, include_internal=True):
    """
    Get all valid vrt ids for a given vrt object, including internal nodes by default

    :param vrt: The vrt object
    :param include_internal: Whether to include internal nodes or only leaf nodes
    :return: ids in the form
        [
            ['category'],
            ['category', 'subcategory'],
            ['category', 'subcategory', 'variant1'],
            ['category', 'subcategory', 'variant2']
        ]
    """
    def _all_id_lists(sub_vrt, prefix):
        if isinstance(sub_vrt, list):
            return [vrt_id for entry in sub_vrt for vrt_id in _all_id_lists(entry, prefix)]
        elif isinstance(sub_vrt, dict):
            if 'children' in sub_vrt:
                new_prefix = prefix + [sub_vrt['id']]
                sub_ids = _all_id_lists(sub_vrt['children'], new_prefix)
                if include_internal:
                    sub_ids += [new_prefix]
                return sub_ids
            else:
                return [prefix + [sub_vrt['id']]]
        else:
            print(sub_vrt)
            raise Exception('unexpected entry found')
    return _all_id_lists(vrt['content'], [])
