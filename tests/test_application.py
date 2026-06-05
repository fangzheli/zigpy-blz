import zigpy.config

from zigpy_blz.zigbee.application import ControllerApplication


def test_controller_exposes_zigpy_probe_configs_for_blz_baudrate():
    assert ControllerApplication._probe_configs == [
        {zigpy.config.CONF_DEVICE_BAUDRATE: 2000000}
    ]


def test_legacy_probe_config_variants_aliases_probe_configs():
    assert ControllerApplication._probe_config_variants is ControllerApplication._probe_configs
