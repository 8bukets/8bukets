"""
Shared pytest setup for the tests/ suite.

Compatibility shim: aioresponses==0.7.8 (the latest release on PyPI at the
time of writing) builds its mocked aiohttp.ClientResponse objects without
passing the ``stream_writer`` keyword argument. Newer aiohttp releases made
``stream_writer`` a required keyword-only parameter of
``ClientResponse.__init__``, so aioresponses-mocked requests fail with:

    TypeError: ClientResponse.__init__() missing 1 required keyword-only
    argument: 'stream_writer'

This patches the missing argument in, only when the installed aiohttp
actually requires it, so the shim is a no-op again once aioresponses ships
a fix upstream (or if run against an older aiohttp).
"""
import inspect
from unittest import mock

try:
    from aioresponses import core as _aioresponses_core
    from aiohttp import ClientResponse as _ClientResponse

    _needs_stream_writer = (
        "stream_writer" in inspect.signature(_ClientResponse.__init__).parameters
    )

    if _needs_stream_writer:
        # aiohttp's ClientResponse.__init__ reads `stream_writer.output_size`
        # whenever `writer` (aioresponses always passes None) is None, so the
        # stand-in needs an `output_size` attribute rather than being None.
        class _DummyStreamWriter:
            output_size = 0

        _original_build_response = _aioresponses_core.RequestMatch._build_response

        def _patched_build_response(self, *args, **kwargs):
            _original_init = _ClientResponse.__init__

            def _init_with_stream_writer(resp_self, *a, **kw):
                kw.setdefault("stream_writer", _DummyStreamWriter())
                return _original_init(resp_self, *a, **kw)

            with mock.patch.object(_ClientResponse, "__init__", _init_with_stream_writer):
                return _original_build_response(self, *args, **kwargs)

        _aioresponses_core.RequestMatch._build_response = _patched_build_response
except ImportError:
    # aioresponses/aiohttp not installed; nothing to patch (e.g. environments
    # that only run the non-aioresponses tests).
    pass
