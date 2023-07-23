from dataclasses import dataclass


@dataclass
class DataClassCommands:
    command_select_device: str
    command_deeplink_execute: str
    command_screen_capture: str
    command_log_clear: str
    command_log_detect_crash: str
    command_kill_app: str
