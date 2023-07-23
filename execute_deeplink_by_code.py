"""
Deeplink executor manager
"""

import deeplink
from deeplink import DeeplinkData
from handler.arrange_commands_handler import arrange_commands
from handler.execute_deeplink_handler import execute_deeplink


def execute_adb_command_mode_code(device_name: str, deeplinks, sleep_time: int, kill_app: bool):
    """
    execute deep-links by hardcodes data
    :param device_name: emulator name
    :param deeplinks: load from deeplink.py
    :param sleep_time: the wait time before execute another deeplink or exit from runner
    :param kill_app: kill the app after executing a deeplink
    :return: screenshots will be saved in the images folder
    """
    deeplink_data, deeplink_data_size = deeplinks, len(deeplinks)
    print(f'Count of data: {deeplink_data_size}')
    adb = arrange_commands(deeplink_data, device_name)
    counter = 1
    for datum in deeplink_data:
        deeplink_data = datum
        deeplink_name = device_name
        execute_deeplink(adb,
                         counter,
                         deeplink_data,
                         deeplink_data_size,
                         deeplink_name,
                         device_name,
                         sleep_time,
                         kill_app)


if __name__ == '__main__':
    DEVICE: str = 'emulator-5558'
    TIME: int = 20
    dl: DeeplinkData = deeplink.DeeplinkData()
    execute_adb_command_mode_code(DEVICE, dl.test_deeplink(), TIME, False)
