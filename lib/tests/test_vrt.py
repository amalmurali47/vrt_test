from utils import utils
import unittest
import subprocess
import jsonschema
import glob
import os

class TestVrt(unittest.TestCase):
    def setUp(self):
        self.mappings = [
            { 'filename': f, 'name': os.path.splitext(os.path.basename(f))[0] }
            for f in glob.glob(utils.MAPPING_DIR + '/**/*.json', recursive=True) if 'schema' not in f
        ]

    @unittest.skip('need to decide the best way to handle this')
    def test_changelog_updated(self):
        """
        Checks if CHANGELOG.md is being updated with the current commit
        and prompts the user if it isn't
        """
        p = subprocess.Popen('git diff HEAD --stat --staged CHANGELOG.md | wc -l', shell=True, stdout=subprocess.PIPE)
        out, _err = p.communicate()
        self.assertGreater(int(out), 0, 'CHANGELOG.md not updated')

    def validate_schema(self, schema_file, data_file):
        schema = utils.get_json(schema_file)
        data = utils.get_json(data_file)
        jsonschema.Draft4Validator.check_schema(schema)
        error = jsonschema.exceptions.best_match(jsonschema.Draft4Validator(schema).iter_errors(data))
        if error:
            raise error

    def test_vrt_schema(self):
        self.validate_schema(utils.VRT_SCHEMA_FILENAME, utils.VRT_FILENAME)

    def test_mapping_schemas(self):
        for mapping in self.mappings:
            schema_file = glob.glob(
                f'{utils.MAPPING_DIR}/**/{mapping["name"]}.schema.json',
                recursive=True
            )[0]
            self.assertTrue(os.path.isfile(schema_file), 'Missing schema file for %s mapping' % mapping['name'])
            self.validate_schema(schema_file, mapping['filename'])

    def all_vrt_ids_have_mapping(self, mappping_filename, key):
        vrt = utils.get_json(utils.VRT_FILENAME)
        mapping = utils.get_json(mappping_filename)
        keyed_mapping = utils.key_by_id(mapping['content'])
        for vrt_id_list in utils.all_id_lists(vrt, include_internal=False):
            self.assertTrue(utils.has_mapping(keyed_mapping, vrt_id_list, key),
                                'no ' + key + ' mapping for ' + '.'.join(vrt_id_list))

    def test_all_vrt_ids_have_all_mappings(self):
        for mapping in self.mappings:
            self.all_vrt_ids_have_mapping(mapping['filename'], mapping['name'])

    def only_map_valid_ids(self, mapping_filename):
        vrt_ids = utils.all_id_lists(utils.get_json(utils.VRT_FILENAME))
        mapping_ids = utils.all_id_lists(utils.get_json(mapping_filename))
        for id_list in mapping_ids:
            self.assertIn(id_list, vrt_ids, 'invalid id in ' + mapping_filename + ' - ' + '.'.join(id_list))

    def test_only_map_valid_ids(self):
        for mapping in self.mappings:
            self.only_map_valid_ids(mapping['filename'])


if __name__ == '__main__':
    unittest.main()
