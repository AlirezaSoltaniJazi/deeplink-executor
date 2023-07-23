"""
Deeplink executor manager
"""

from handler.arrange_commands_handler import arrange_commands
from handler.execute_deeplink_handler import execute_deeplink
from util.file_handler import read_from_file


def execute_adb_command_mode_file(device_name: str, file_name: str, sheet_name: str, sleep_time: int, kill_app: bool):
    """
    execute deep-links by a file
    :param device_name: emulator or device name
    :param file_name: file name
    :param sheet_name: sheet name in the Excel file
    :param sleep_time: the wait time before execute another deeplink or exit from runner
    :param kill_app: kill the app after executing a deeplink
    :return: screenshots will be saved in the images folder
    """
    deeplink_data, deeplink_data_size_all = read_from_file(f'./{file_name}', sheet_name)
    deeplink_data_size = deeplink_data_size_all.get(1)
    print(f'Count of data: {deeplink_data_size}')
    adb = arrange_commands(deeplink_data, device_name)
    counter = 1
    for datum in deeplink_data:
        deeplink_data = datum.deeplink
        deeplink_name = datum.name
        execute_deeplink(adb,
                         counter,
                         deeplink_data,
                         deeplink_data_size,
                         deeplink_name,
                         device_name,
                         sleep_time,
                         kill_app)


if __name__ == '__main__':
    DEVICE: str = '393d63d8'
    TIME: int = 5
    execute_adb_command_mode_file(device_name=DEVICE, file_name='deeplink-file-1.xlsx', sheet_name='Sheet1',
                                  sleep_time=TIME,
                                  kill_app=False)
