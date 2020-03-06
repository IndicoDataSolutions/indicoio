import pytest

from pathlib import Path
from indicoio.api.prebuilt import IndicoApi


@pytest.fixture
def indicoapi(request):
    return IndicoApi(config_options={"host": request.config.getoption("--host")})

def test_document_extraction_file(indicoapi):
    path = Path(__file__).parent / "data" / "mock.pdf"
    results = indicoapi.document_extraction(data=[path])
    import ipdb; ipdb.set_trace()
    assert isinstance(results, list)
    assert isinstance(results[0], dict)
    for field in ("metadata", "pages"):
        assert field in results[0]
