from utils import utils
from artifacts import scw_artifact

url_mapping = {}
current_vrt = utils.get_json(utils.VRT_FILENAME)
scw_artifact.write_artifact_file(
  scw_artifact.generate_urls(current_vrt['content'], url_mapping)
)
