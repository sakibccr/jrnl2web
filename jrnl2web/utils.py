import os
import math


import shutil

def copy_static_files(static_dir, output_dir):
    """
    Copy static files (e.g., CSS, JS) to the output directory.

    Args:
        static_dir (str): Path to the static files directory.
        output_dir (str): Path to the output directory.

    Returns:
        None
    """
    destination = os.path.join(output_dir, "static")
    if os.path.exists(static_dir):
        shutil.copytree(static_dir, destination, dirs_exist_ok=True)
    else:
        print(f"Warning: Static directory '{static_dir}' does not exist.")

def ensure_directory_exists(directory):
    """
    Ensure that a directory exists. If it doesn't, create it.

    Args:
        directory (str): Path to the directory.

    Returns:
        None
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def sanitize_filename(filename):
    """
    Sanitize a string to make it safe for use as a filename.

    Args:
        filename (str): The original string.

    Returns:
        str: Sanitized filename.
    """
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, "_")
    return filename.strip()

def truncate_text(text, max_length=100):
    """
    Truncate text to a specified length, adding ellipses if needed.

    Args:
        text (str): Original text.
        max_length (int): Maximum allowed length.

    Returns:
        str: Truncated text.
    """
    if len(text) > max_length:
        return text[:max_length].strip() + "..."
    return text

def human_readable_size(size_bytes):
    """
    Convert a size in bytes to a human-readable format (e.g., KB, MB).

    Args:
        size_bytes (int): Size in bytes.

    Returns:
        str: Human-readable size.
    """
    if size_bytes == 0:
        return "0B"
    size_names = ("B", "KB", "MB", "GB", "TB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_names[i]}"
