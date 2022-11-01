import httpx
import pytest

from kiota_http import middleware
from kiota_http.kiota_client_factory import KiotaClientFactory
from kiota_http.middleware import (
    AsyncKiotaTransport,
    MiddlewarePipeline,
    ParametersNameDecodingHandler,
    RedirectHandler,
    RetryHandler,
)


def test_create_with_default_middleware():
    """Test creation of HTTP Client using default middleware"""
    client = KiotaClientFactory.create_with_default_middleware()

    assert isinstance(client, httpx.AsyncClient)
    assert isinstance(client._transport, AsyncKiotaTransport)


def test_get_default_middleware():
    middleware = KiotaClientFactory._get_default_middleware()

    assert len(middleware) == 3
    assert isinstance(middleware[0], RedirectHandler)
    assert isinstance(middleware[1], RetryHandler)
    assert isinstance(middleware[2], ParametersNameDecodingHandler)


def test_create_middleware_pipeline():

    middleware = KiotaClientFactory._get_default_middleware()
    pipeline = KiotaClientFactory._create_middleware_pipeline(
        middleware,
        httpx.AsyncClient()._transport
    )

    assert isinstance(pipeline, MiddlewarePipeline)
