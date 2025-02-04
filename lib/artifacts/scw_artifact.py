import json
import requests
import utils.utils

BASE_SCW_URL = 'https://integration-api.securecodewarrior.com/api/v1/trial?id=bugcrowd&mappingList=vrt&mappingKey='
OUTPUT_FILENAME = 'scw_links.json'


def scw_url(vrt_id):
    return f'{BASE_SCW_URL}{vrt_id.replace(".", ":")}'


def scw_mapping(vrt_id):
    path = scw_url(vrt_id)
    print('Fetching...')
    response = requests.get(path)
    if response.status_code == 200:
        print(f'Exists: {path}')
        return path + '&redirect=true'
    else:
        print(f'Not Found: {path}')
        return None


def join_vrt_id(parent_id, child_id):
    return '.'.join([parent_id, child_id]) if parent_id is not None else child_id


def generate_urls(vrt, content, parent_id=None):
    for node in vrt:
        vrt_id = join_vrt_id(parent_id, node['id'])
        content[vrt_id] = scw_mapping(vrt_id)
        if 'children' in node:
            content.update(
                generate_urls(
                    node['children'],
                    {},
                    vrt_id
                )
            )

    return content


def write_artifact_file(mapping):
    with open(OUTPUT_FILENAME, 'w') as outfile:
        json.dump(mapping, outfile, indent=2, sort_keys=False)
