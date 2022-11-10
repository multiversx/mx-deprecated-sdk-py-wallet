from typing import Any, Dict

import requests


class ProxyNetworkProvider():
    def __init__(self, url: str):
        self.url = url

    def do_get(self, url: str) -> 'GenericResponse':
        url = f"{self.url}/{url}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            parsed = response.json()
            return _get_data(parsed, url)
        except requests.HTTPError as err:
            error_data = _extract_error_from_response(err.response)
            raise GenericError(url, error_data)
        except requests.ConnectionError as err:
            raise GenericError(url, err)
        except Exception as err:
            raise GenericError(url, err)

    def do_post(self, url: str, payload: Any) -> 'GenericResponse':
        url = f"{self.url}/{url}"

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            parsed = response.json()
            return _get_data(parsed, url)
        except requests.HTTPError as err:
            error_data = _extract_error_from_response(err.response)
            raise GenericError(url, error_data)
        except requests.ConnectionError as err:
            raise GenericError(url, err)
        except Exception as err:
            raise GenericError(url, err)


def _get_data(parsed: Dict[str, Any], url: str) -> 'GenericResponse':
    err = parsed.get("error")
    code = parsed.get("code")

    if not err and code == "successful":
        data: Dict[str, Any] = parsed.get("data", dict())
        return GenericResponse(data)

    raise GenericError(url, f"code:{code}, error: {err}")


def _extract_error_from_response(response: Any):
    try:
        return response.json()
    except Exception:
        return response.text


class GenericResponse():
    def __init__(self, data: Any) -> None:
        self.__dict__.update(data)

    def get(self, key: str, default: Any = None) -> Any:
        return self.__dict__.get(key, default)

    def to_dictionary(self) -> Dict[str, Any]:
        return self.__dict__


class GenericError(Exception):
    def __init__(self, url: str, data: Any):
        super().__init__(f"Url = [{url}], error = {data}")
