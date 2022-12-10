"""Main application object."""

from pathlib import Path

from pyapi.server import Application

from . import endpoints

SOURCE_ROOT = Path(__file__).parent
API_SPEC_PATH = SOURCE_ROOT.parent / "reference/openapi.json"

app = Application.from_file(API_SPEC_PATH, module=endpoints)
