"""Tests for getters."""

from napalm.base.test.getters import BaseTestGetters

import pytest


@pytest.mark.usefixtures("set_device_parameters")
class TestGetter(BaseTestGetters):
    """Test get_* methods."""

    @pytest.mark.skip
    def test_get_interfaces(self, test_case):
        """Need to implement."""
        raise NotImplementedError

    @pytest.mark.skip
    def test_get_ntp_servers(self, test_case):
        """Need to implement."""
        raise NotImplementedError

    @pytest.mark.skip
    def test_get_interfaces_counters(self, test_case):
        """Need to implement."""
        raise NotImplementedError

    @pytest.mark.skip
    def test_get_lldp_neighbors_detail(self, test_case):
        """Need to implement."""
        raise NotImplementedError

    @pytest.mark.skip
    def test_get_lldp_neighbors(self, test_case):
        """Need to implement."""
        raise NotImplementedError

    @pytest.mark.skip
    def test_get_facts(self, test_case):
        """Need to implement."""
        raise NotImplementedError

    @pytest.mark.skip
    def test_is_alive(self, test_case):
        """Need to implement."""
        raise NotImplementedError

    @pytest.mark.skip
    def test_get_config(self, test_case):
        """Need to implement."""
        raise NotImplementedError

    @pytest.mark.skip
    def test_get_arp_table(self, test_case):
        """Need to implement."""
        raise NotImplementedError

    @pytest.mark.skip
    def test_get_interfaces_ip(self, test_case):
        """Need to implement."""
        raise NotImplementedError

    @pytest.mark.skip
    def test_get_arp_table_with_vrf(self, test_case):
        """Need to implement."""
        raise NotImplementedError

    @pytest.mark.skip
    def test_get_config_filtered(self, test_case):
        """Need to implement."""
        raise NotImplementedError

    @pytest.mark.skip
    def test_method_signatures(self, test_case):
        """Need to implement."""
        raise NotImplementedError
