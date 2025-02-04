import os
import sys
import json
from utils import utils
from artifacts import scw_artifact

artifact_json = utils.get_json(scw_artifact.OUTPUT_FILENAME)
repo_path = os.path.join(utils.THIRD_PARTY_MAPPING_DIR, utils.SCW_DIR, utils.SCW_FILENAME)
print(os.path.abspath(repo_path))
repo_json = utils.get_json(repo_path)

sorted_artifact_json = json.dumps(artifact_json, sort_keys=True)
sorted_repo_json = json.dumps(repo_json, sort_keys=True)

if sorted_artifact_json == sorted_repo_json:
    print('SCW Document is valid!')
    sys.exit(0)
else:
    print('SCW Document is invalid, copy the artifact to the remediation training')
    sys.exit(1)
