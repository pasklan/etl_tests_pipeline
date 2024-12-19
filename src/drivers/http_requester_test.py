from .http_requester import HttpRequester


def test_request_from_page():
    # url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'
    http_requester = HttpRequester()
    request_response = http_requester.request_from_page()
    print()
    print(request_response)
