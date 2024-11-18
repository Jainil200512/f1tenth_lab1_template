import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ubuntu22/sim_ws/src/safety_node/install/safety_node'
