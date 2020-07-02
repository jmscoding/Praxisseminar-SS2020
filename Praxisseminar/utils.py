"""


	Praxisseminar utils.py

	sqlite and enip use name (string) and pid (int) has key and the state stores
	values as strings.
	
	sqlite uses float keyword and cpppo use REAL keyword.
	if ACTUATORX is 1 then is ON otherwise is OFF.
"""

from minicps.utils import *

#Eigenen Logger basteln der mir die Daten persistent speichert, sodass ich sie danach auslesen kann

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
MOTOR_VEL = { #Geschwindigkeitseinstellungen + Quelle Andi
    'LV': 0.9,
    'HV': 6.0,
    'MIN': 0.0,
    'MAX': 9.0
}

# topo {{{1
IP = {
    'plc1': '10.0.0.10',
    'plc2': '10.0.0.20',
    'plc3': '10.0.0.30',
    'plc4': '10.0.0.40',
    'plc5': '10.0.0.50',
    'host1': '10.0.0.60',
    'attacker': '10.0.0.77',
}

NETMASK = '/24'

MAC = {
    'plc1': '00:00:00:00:00:01',
    'plc2': '00:00:00:00:00:06',
    'plc3': '00:00:00:00:00:02',
    'plc4': '00:00:00:00:00:0C',
    'plc5': '00:00:00:00:00:0F',
    'host1': '00:00:00:00:00:0D',
    'attacker': 'AA:AA:AA:AA:AA:AA',
}

# others
PLC1_DATA = {
    'SENSOR1': '0',
    'ACTUATOR1': '1',  # 0 means OFF and 1 means ON
}

# protocol
PLC1_MAC = MAC['plc1']
PLC1_TAGS = (
    ('SENSOR', 1, 'INT'),
    ('MOTOR', 1, 'INT'),  # 0 means OFF and 1 means ON
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

# state
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

# Sensor + Actuator initialisierende Daten

SCHEMA_INIT = """
    INSERT INTO cb_table VALUES ('SENSOR1',   'int', '0', 1);
    INSERT INTO cb_table VALUES ('ACTUATOR1', 'int', '1', 1);
"""   
