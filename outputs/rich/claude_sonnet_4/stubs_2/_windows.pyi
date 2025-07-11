from dataclasses import dataclass

@dataclass
class WindowsConsoleFeatures:
    vt: bool = False
    truecolor: bool = False

def get_windows_console_features() -> WindowsConsoleFeatures: ...