import os

from model.command_model import DataClassCommands


def arrange_commands(deeplink_data, device_name):
    default_package_name = 'com.farsitel.bazaar'
    select_device = 'adb -s'
    deeplink_execute = 'shell am start -W -a android.intent.action.VIEW -d'
    screen_capture = f'exec-out screencap -p > {os.getcwd()}/images/'
    log_clear = 'logcat -c'
    log_detect_crash = f'logcat -d --buffer=crash -v color {default_package_name}:E'
    kill_app = f'shell am force-stop {default_package_name}'
    print(f'device_name: {device_name}', f'deeplink_data: {deeplink_data}\n', flush=True)
    adb_commands = DataClassCommands(select_device,
                                     deeplink_execute,
                                     screen_capture,
                                     log_clear,
                                     log_detect_crash,
                                     kill_app)
    return adb_commands
