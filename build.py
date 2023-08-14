# 3rd party imports
from config import settings

# pan-os-python imports
from panos.device import Vsys
from panos.ha import HA1, HA2, HighAvailability
from panos.panorama import (
    DeviceGroup,
    Panorama,
    Template,
    TemplateStack,
    TemplateVariable,
)
from panos.network import EthernetInterface, Zone
from panos.errors import PanDeviceError


# create a panorama object
pan = Panorama(
    hostname=settings.panorama.base_url,
    api_key=settings.api_key,
)

# attempt to refresh the system info with credientials
try:
    pan.refresh_system_info()
    print("Successfully connected to Panorama with credientials")
except PanDeviceError as e:
    print("Failed to connect to Panorama: ", str(e))

