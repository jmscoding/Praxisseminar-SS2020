"""


	Praxisseminar utils.py

	sqlite and enip use name (string) and pid (int) has key and the state stores
	values as strings.
	
	sqlite uses float keyword and cpppo use REAL keyword.
	if ACTUATORX is 1 then is ON otherwise is OFF.
"""

from minicps.utils import build_debug_logger

Praxisseminar_logger = build_debug_logger(
    name=__name__,
    bytes_per_file=10000,
    rotating_files=2,
    lformat='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    ldir='logs/',
    suffix='')


# others
PLC1_DATA = {
    'SENSOR1': '0',
    'ACTUATOR1': '1',  # 0 means OFF and 1 means ON
}

# protocol
PLC1_MAC = '00:00:00:00:00:01'
PLC1_TAGS = (
    ('SENSOR1', 1, 'INT'),
    ('ACTUATOR1', 1, 'INT'),  # 0 means OFF and 1 means ON
)

PLC1_ADDR = '10.0.0.1'
PLC1_SERVER = {
    'address': PLC1_ADDR,
    'tags': PLC1_TAGS
}
PLC1_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC1_SERVER
}

# topo {{{1
IP = {
    'plc1': '192.168.1.10',
    'plc2': '192.168.1.20',
    'plc3': '192.168.1.30',
    'plc4': '192.168.1.40',
    'plc5': '192.168.1.50',
    'host1': '192.168.1.60',
    'attacker': '192.168.1.77',
}

NETMASK = '/24'

MAC = {
    'plc1': '00:1D:9C:C7:B0:70',
    'plc2': '00:1D:9C:C8:BC:46',
    'plc3': '00:1D:9C:C8:BD:F2',
    'plc4': '00:1D:9C:C7:FA:2C',
    'plc5': '00:1D:9C:C8:BC:2F',
    'host1': '00:1D:9C:C7:FA:2D',
    'attacker': 'AA:AA:AA:AA:AA:AA',
}

# state
PATH = 'cb_db.sqlite'
NAME = 'cb_table'

STATE = {
    'name': NAME,
    'path': PATH
}

SCHEMA = 
CREATE TABLE cb_table (
    name              TEXT NOT NULL,
    datatype          TEXT NOT NULL,
    value             TEXT,
    pid               INTEGER NOT NULL,
    PRIMARY KEY (name, pid)
);

# Sensor + Actuator initialisierende Daten

SCHEMA_INIT = 
    INSERT INTO cb_table VALUES ('SENSOR1',   'int', '0', 1);
    INSERT INTO cb_table VALUES ('ACTUATOR1', 'int', '1', 1);
   
