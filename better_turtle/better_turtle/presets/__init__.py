from .default_presets import AVAILABLE_FILE_PRESETS as default_presets
from .user_presets import AVAILABLE_FILE_PRESETS as user_presets
AVAILABLE_FILE_PRESETS = default_presets | user_presets
__all__ = ["AVAILABLE_FILE_PRESETS"]
