"""
    Praxisseminar utils.py
"""


from minicps.utils import *

# Eigener Logger

Praxisseminar_test_logger = logging.getLogger(__name__)
Praxisseminar_test_logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('logs/file.log')
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

Praxisseminar_test_logger.addHandler(fh)

# Ende des eigenen Loggers

Praxisseminar_logger = build_debug_logger(
    name=__name__,
    bytes_per_file=10000,
    rotating_files=2,
    lformat='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    ldir='logs/',
    suffix='.log')

# Control logic threshold
MOTOR_VEL = {# Geschwindigkeitseinstellungen
    'STD': 3.0,
    'MIN': 0.0,
    'MAX': 9.0
}


# topo {{{1
IP = {
    'plc1': '10.0.0.10',
    'host1': '10.0.0.60',
    'attacker': '10.0.0.77',
}

NETMASK = '/24'

MAC = {
    'plc1': '00:00:00:00:00:01',
    'host1': '00:00:00:00:00:0D',
    'attacker': 'AA:AA:AA:AA:AA:AA',
}

# Anfangsdaten
PLC1_DATA = {
    'SENSOR': '0.0',
    'MOTOR': '0',   # 0 means OFF and 1 means ON
}

# Protokoll
PLC1_MAC = MAC['plc1']
PLC1_TAGS = (
    ('SENSOR', 1, 'REAL'),
    ('MOTOR', 1, 'INT'),
)

PLC1_ADDR = IP['plc1']
PLC1_SERVER = {
    'address': PLC1_ADDR,
    'tags': PLC1_TAGS
}
PLC1_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC1_SERVER
}


HMI_ADDR = IP['host1']

HMI_MAC = MAC['host1']

# Anfangsdaten
HMI_DATA = {
    'SENSOR': '0.0',
    'MOTOR': '0',   # 0 means OFF and 1 means ON
}

# Protokoll
HMI_TAGS = (
    ('SENSOR', 1, 'REAL'),
    ('MOTOR', 1, 'INT'),
)

HMI_SERVER = {
    'address': HMI_ADDR,
    'tags': HMI_TAGS
}
HMI_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': HMI_SERVER
}


# Datenbank
PATH = 'cb_db.sqlite'
NAME = 'cb_table'

STATE = {
    'name': NAME,
    'path': PATH
}

SCHEMA = """
	CREATE TABLE cb_table (
		name              TEXT NOT NULL,
		datatype          TEXT NOT NULL,
		value             TEXT,
		pid               INTEGER NOT NULL,
		PRIMARY KEY (name, pid)
);"""


SCHEMA_INIT = """
    INSERT INTO cb_table VALUES ('SENSOR', 'float', '0.0', 1);
    INSERT INTO cb_table VALUES ('MOTOR', 'int', '0', 1);
"""   
