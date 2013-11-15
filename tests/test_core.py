from flexmock import flexmock
import pytest
import requests


@pytest.fixture
def auth():
    return flexmock()


@pytest.fixture
def netvisor(auth):
    from netvisor import core
    kwargs = dict(
        sender='Test client',
        partner_id='xxx_yyy',
        partner_key='E2CEBB1966C7016730C70CA92CBB93DD',
        customer_id='xx_yyyy_zz',
        customer_key='7767899D6F5FB333784A2520771E5871',
        organization_id='1967543-8',
        language='EN'
    )
    (
        flexmock(core)
        .should_receive('NetvisorAuth')
        .with_args(**kwargs)
        .and_return(auth)
    )
    return core.Netvisor(host='http://koulutus.netvisor.fi/', **kwargs)


class TestNetvisor(object):
    def test_constructor_sets_host(self, netvisor):
        assert netvisor.host == 'http://koulutus.netvisor.fi/'

    def test_constructor_creates_session(self, netvisor):
        assert isinstance(netvisor._session, requests.Session)

    def test_constructor_sets_session_auth(self, auth, netvisor):
        assert netvisor._session.auth is auth
