import urllib

import google.auth.transport.requests
import google.oauth2.id_token


def make_authorized_get_request(endpoint, audience):
    """
    make_authorized_get_request makes a GET request to the specified HTTP endpoint
    by authenticating with the ID token obtained from the google-auth client library
    using the specified audience value.
    """
    req = urllib.request.Request(endpoint)
    auth_req = google.auth.transport.requests.Request()
    id_token = google.oauth2.id_token.fetch_id_token(auth_req, audience)
    req.add_header("Authorization", f"Bearer {id_token}")
    response = urllib.request.urlopen(req)
    return response.read()


if __name__ == "__main__":
    url_ = "https://gpw-scraper-app-hlfk7e2nga-lm.a.run.app/load_stocks_close_prices/"
    res = make_authorized_get_request(endpoint=url_, audience=url_)
    print(res)
