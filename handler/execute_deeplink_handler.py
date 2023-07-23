import subprocess
import time as t
from datetime import datetime

from model.command_model import DataClassCommands


def execute_deeplink(adb: DataClassCommands,
                     counter: int,
                     deeplink_data,
                     deeplink_data_size,
                     deeplink_name,
                     device_name: str,
                     sleep_time: int,
                     kill_app: bool):
    cmd_execute_deeplink = f'{adb.command_select_device} {device_name} {adb.command_deeplink_execute} "{deeplink_data}"'
    cmd_log_clear = f'{adb.command_select_device} {device_name} {adb.command_log_clear}'
    cmd_log_detect_crash = f'{adb.command_select_device} {device_name} {adb.command_log_detect_crash}'
    print('Executed commend is (execute deeplink):', cmd_execute_deeplink)
    subprocess.call(rf'{cmd_log_clear}', shell=True)
    subprocess.call(rf'{cmd_execute_deeplink}', shell=True)
    time = str(datetime.now()).replace(' ', '-').replace(':', '-').replace('.', '-')
    cmd_capture_screenshot = f'{adb.command_select_device} {device_name} ' \
                             f'{adb.command_screen_capture}{time}-{deeplink_name}.png '
    if counter != deeplink_data_size:
        for i in range(sleep_time, 0, -1):
            print(i, flush=True, end="...")
            t.sleep(1)
        counter += 1
    else:
        print('Stopping the runner...')
    crash_log = subprocess.check_output(rf'{cmd_log_detect_crash}', shell=True)
    if len(crash_log) > 0:
        print(
            f'We have a crash with this deeplink: {deeplink_data} ,and the crash logs is:'
            f'\n{crash_log.decode("utf-8")}')
    print(f'execute deeplink: {deeplink_data} on the device: {device_name} is done!', flush=True)
    subprocess.call(f'{cmd_capture_screenshot}', shell=True)
    if kill_app:
        cmd_kill_app = f'{adb.command_select_device} {device_name} {adb.command_kill_app}'
        subprocess.call(f'{cmd_kill_app}', shell=True)
        print('The app killed!', flush=True)
    print('Execute deeplink process done!', flush=True, end='\n\n')
