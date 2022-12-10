"""Endpoint functions."""

from pyapi.server import Request, Response


def retrieve_schemas(request: Request) -> Response | dict:
    """Retrieve the latest versions of all published schemas."""
    return {}


def retrieve_schema(request: Request) -> Response | dict:
    """Retrieve the latest version of a schema."""
    return {}


def update_schema(request: Request) -> Response | dict:
    """
    Update the latest non-published version of the schema.

    If the name does not exist, a new draft schema (with `version=0.0`) is inserted.
    Otherwise, if there are no non-published versions, `409 CONFLICT` is returned.
    """
    return {}


def retrieve_schema_version(request: Request) -> Response | dict:
    """Retrieve a specific version of a schema."""
    return {}


def update_schema_version(request: Request) -> Response | dict:
    """
    Retrieve a specific version of a schema.

    If either the name or the version do not exist, a new draft schema, with the
    given version, is inserted. If the version is already published or deprecated,
    `409 CONFLICT` is returned.
    """
    return {}
