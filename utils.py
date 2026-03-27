import os
import logging

logger = logging.getLogger(__name__)

def validate_output_path(path: str) -> str:
    """
    Ensure output path is safe and within current working directory.
    This prevents overwriting arbitrary files on the system.
    """
    try:
        abs_path = os.path.abspath(path)
        cwd = os.getcwd()
        if not os.path.commonpath([abs_path, cwd]) == cwd:
            msg = f"Security Error: Output path '{path}' is outside the current working directory."
            logger.error(msg)
            raise ValueError(msg)
        return abs_path
    except Exception as e:
        # Re-raise if it's our ValueError, otherwise wrap/log
        if isinstance(e, ValueError):
            raise
        logger.error(f"Invalid path {path}: {e}")
        raise ValueError(f"Invalid path {path}: {e}")
