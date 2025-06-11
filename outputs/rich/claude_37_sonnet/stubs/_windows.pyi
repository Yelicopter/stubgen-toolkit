from dataclasses import dataclass

@dataclass
class WindowsConsoleFeatures:
    vt: bool
    truecolor: bool

def get_windows_console_features() -> WindowsConsoleFeatures:
    ...