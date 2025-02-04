from utils import utils
import os
import unittest

class TestArtifactFormat(unittest.TestCase):
  def setUp(self):
    self.scw_artifact_path = os.path.join(
      utils.THIRD_PARTY_MAPPING_DIR,
      utils.SCW_DIR,
      utils.SCW_FILENAME
    )

  def test_artifact_loads_valid_json(self):
    self.assertTrue(
      utils.get_json(self.scw_artifact_path),
      self.scw_artifact_path + ' is not valid JSON.'
    )

if __name__ == "__main__":
    unittest.main()