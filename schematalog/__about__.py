import json
from pathlib import Path

SOURCE_PATH = Path(__file__).parent
API_SPEC_PATH = SOURCE_PATH.parent / "reference/openapi.json"

with open(API_SPEC_PATH) as spec_file:
    API_SPEC_RAW = json.load(spec_file)

with open(SOURCE_PATH / "VERSION") as version_file:
    VERSION = version_file.read()
