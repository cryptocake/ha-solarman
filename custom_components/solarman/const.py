from datetime import timedelta as td

DOMAIN = "solarman"
PLATFORMS: list[str] = ["sensor", "switch", "number", "select", "time"]

IP_BROADCAST = "<broadcast>"
IP_ANY = "0.0.0.0"

PORT_ANY = 0

DISCOVERY_PORT = 48899
DISCOVERY_TIMEOUT = 1.0
DISCOVERY_MESSAGE = "WIFIKIT-214028-READ"
DISCOVERY_RECV_MESSAGE_SIZE = 1024

COMPONENTS_DIRECTORY = "custom_components"

LOOKUP_DIRECTORY = "inverter_definitions"
LOOKUP_DIRECTORY_PATH = f"{COMPONENTS_DIRECTORY}/{DOMAIN}/{LOOKUP_DIRECTORY}/"
LOOKUP_CUSTOM_DIRECTORY_PATH = f"{COMPONENTS_DIRECTORY}/{DOMAIN}/{LOOKUP_DIRECTORY}/custom/"

CONF_DISCOVERY = "inverter_discovery"
CONF_INVERTER_HOST = "inverter_host"
CONF_INVERTER_SERIAL = "inverter_serial"
CONF_INVERTER_PORT = "inverter_port"
CONF_INVERTER_MB_SLAVE_ID = "inverter_mb_slave_id"
CONF_LOOKUP_FILE = "lookup_file"
CONF_BATTERY_NOMINAL_VOLTAGE = "battery_nominal_voltage"
CONF_BATTERY_LIFE_CYCLE_RATING = "battery_life_cycle_rating"

DEFAULT_NAME = "Inverter"
DEFAULT_DISCOVERY = True
DEFAULT_PORT_INVERTER = 8899
DEFAULT_INVERTER_MB_SLAVE_ID = 1
DEFAULT_LOOKUP_FILE = "deye_hybrid.yaml"
DEFAULT_BATTERY_NOMINAL_VOLTAGE = 48
DEFAULT_BATTERY_LIFE_CYCLE_RATING = 6000

DEFAULT_REGISTERS_UPDATE_INTERVAL = 60
DEFAULT_REGISTERS_CODE = 0x03
DEFAULT_REGISTERS_MIN_SPAN = 25
DEFAULT_DIGITS = 6

AUTO_RECONNECT = True
ACTION_ATTEMPTS = 5
ACTION_ATTEMPTS_MAX = ACTION_ATTEMPTS * 6

TIMINGS_INTERVAL = 5
TIMINGS_UPDATE_INTERVAL = td(seconds = TIMINGS_INTERVAL)
TIMINGS_UPDATE_TIMEOUT = TIMINGS_INTERVAL * 6
TIMINGS_SOCKET_TIMEOUT = TIMINGS_INTERVAL * 4 - 1
TIMINGS_WAIT_SLEEP = 0.2

ATTR_FRIENDLY_NAME = "friendly_name"

REQUEST_UPDATE_INTERVAL = "update_interval"
REQUEST_MIN_SPAN = "min_span"
REQUEST_CODE = "code"
REQUEST_CODE_ALT = "mb_functioncode"
REQUEST_START = "start"
REQUEST_END = "end"

SERVICES_PARAM_DEVICE = "device"
SERVICES_PARAM_REGISTER = "register"
SERVICES_PARAM_QUANTITY = "quantity"
SERVICES_PARAM_VALUE = "value"
SERVICES_PARAM_VALUES = "values"
SERVICES_PARAM_WAIT_FOR_ATTEMPTS = "wait_for_attempts"

SERVICE_READ_HOLDING_REGISTERS = "read_holding_registers"
SERVICE_WRITE_HOLDING_REGISTER = "write_holding_register"
SERVICE_WRITE_MULTIPLE_HOLDING_REGISTERS = "write_multiple_holding_registers"
