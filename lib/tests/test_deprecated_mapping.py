from utils import utils
import unittest
from semantic_version import Version


class TestDeprecatedMapping(unittest.TestCase):
    def setUp(self):
        self.vrt_versions = utils.all_versions(utils.VRT_FILENAME)
        self.last_tagged_version = max([Version.coerce(x) for x in self.vrt_versions.keys() if x != 'current'])
        self.deprecated_json = utils.get_json(utils.DEPRECATED_MAPPING_FILENAME)

    def test_old_vrt_ids_have_current_node(self):
        for version, vrt in self.vrt_versions.items():
            if version == 'current':
                continue
            for id_list in utils.all_id_lists(vrt):
                vrt_id = '.'.join(id_list)
                if vrt_id in self.deprecated_json:
                    max_ver = sorted(self.deprecated_json[vrt_id].keys(), key=lambda s: map(int, s.split('.')))[-1]
                    vrt_id = self.deprecated_json[vrt_id][max_ver]
                    id_list = vrt_id.split('.')
                self.assertTrue(vrt_id == 'other' or self.check_mapping(id_list),
                                '%s from v%s has no mapping' % (vrt_id, version))

    def test_deprecated_nodes_map_valid_node(self):
        for old_id, mapping in self.deprecated_json.items():
            for new_version, new_id in mapping.items():
                self.assertTrue(new_id == 'other' or utils.id_valid(self.vrt_version(new_version), new_id.split('.')),
                                new_id + ' is not valid')

    def check_mapping(self, id_list):
        if utils.id_valid(self.vrt_versions['current'], id_list):
            return True
        elif len(id_list) == 1:
            return False
        else:
            return self.check_mapping(id_list[0:-1])

    def vrt_version(self, version):
        if version in self.vrt_versions:
            return self.vrt_versions[version]
        elif Version.coerce(version) > self.last_tagged_version:
            return self.vrt_versions['current']
        else:
            self.fail('Unknown version: %s' % version)

if __name__ == "__main__":
    unittest.main()
