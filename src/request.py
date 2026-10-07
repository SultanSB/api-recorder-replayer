# https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY
import re

# scheme://host[:port]/path  — stops at "?" (query) or "#" (fragment)
URL_PATTERN = re.compile(r"https?://([^/?#]+)([^?#]*)", re.IGNORECASE)

class Request:
    # def __init__(self, baseUrl, endpoint, queryParam, httpMethod):
    #     self.baseUrl = baseUrl
    #     self.endpoint = endpoint
    #     self.queryParam = queryParam
    #     self.httpMethod = httpMethod

    def __init__(self, url, httpMethod, headers=None, body=None):
        self.url = url
        match = URL_PATTERN.match(url)
        if match is None:
            raise ValueError(f"Invalid URL, expected http:// or https://: {url!r}")
        self.base_url = match.group(1)
        self.endpoint = match.group(2) or "/"
        self.query_params = self._handle_query_params(url)
        self.http_method = httpMethod
        self.headers = headers
        self.body = body

    def _handle_query_params(self, url):
        if "?" in url:
            query_part = url.split("?")[1]
            if query_part:
                if "&" in query_part:
                    return query_part.split("&")
                else:
                    return [query_part]
        return []
    def display_info(self):
        print(f"This is the whole URL: {self.url}, \nthis is the host: {self.base_url}, \nthis is the endpoint: {self.endpoint}, \nthis is the query parameters {self.query_params}, \nthis is the http method {self.http_method}")