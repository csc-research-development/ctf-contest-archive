import os
import stat
from lib.storage import instances

chall_start_path = os.path.join(os.getcwd(), 'chall/start.sh')
chall_stop_path = os.path.join(os.getcwd(), 'chall/stop.sh')

def start_instance(port):
    instance_id = f'coin-hunt-{port}'

    # ensure the start script is executable
    os.chmod(chall_start_path, stat.S_IRWXU)

    result = os.system(f'"{chall_start_path}" {port} {instance_id}')

    if result != 0:
        return None, 'Failed to start new instance'

    return instance_id, None

def stop_instance(port, instance_id, user_id):
    # ensure the start script is executable
    os.chmod(chall_stop_path, stat.S_IRWXU)

    result = os.system(f'"{chall_stop_path}" {port} {instance_id}')

    if result != 0:
        return None, 'Failed to stop instance'
        
    del instances[user_id]

    return instance_id, None