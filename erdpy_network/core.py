from typing import Any, Dict

import requests
from erdpy import errors
from erdpy.proxy.messages import GenericProxyResponse


class ProxyNetworkProvider():
    def __init__(self, url: str):
        self.url = url

    def do_get(self, url: str) -> GenericProxyResponse:
        try:
            response = requests.get(url)
            response.raise_for_status()
            parsed = response.json()
            return _get_data(parsed, url)
        except requests.HTTPError as err:
            error_data = _extract_error_from_response(err.response)
            raise errors.ProxyRequestError(url, error_data)
        except requests.ConnectionError as err:
            raise errors.ProxyRequestError(url, err)
        except Exception as err:
            raise errors.ProxyRequestError(url, err)

    def do_post(self, url: str, payload: Any) -> GenericProxyResponse:
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            parsed = response.json()
            return _get_data(parsed, url)
        except requests.HTTPError as err:
            error_data = _extract_error_from_response(err.response)
            raise errors.ProxyRequestError(url, error_data)
        except requests.ConnectionError as err:
            raise errors.ProxyRequestError(url, err)
        except Exception as err:
            raise errors.ProxyRequestError(url, err)


def _get_data(parsed: Dict[str, Any], url: str) -> GenericProxyResponse:
    err = parsed.get("error")
    code = parsed.get("code")

    if not err and code == "successful":
        data: Dict[str, Any] = parsed.get("data", dict())
        return GenericProxyResponse(data)

    raise errors.ProxyRequestError(url, f"code:{code}, error: {err}")


def _extract_error_from_response(response: Any):
    try:
        return response.json()
    except Exception:
        return response.text
