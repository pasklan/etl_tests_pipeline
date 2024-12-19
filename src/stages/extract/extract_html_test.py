from src.drivers.http_requester import HttpRequester
from src.drivers.html_collector import HtmlCollector
from src.stages.contracts.extract_contract import ExtractContract

from .extract_html import ExtractHtml

def test_extract():
    http_requester = HttpRequester()    
    html_collector = HtmlCollector()
    
    extract_html = ExtractHtml(http_requester, html_collector)
    
    response = extract_html.extract()
    
    print(response)
    
    assert isinstance(response, ExtractContract)