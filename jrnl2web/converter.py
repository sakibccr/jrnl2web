import os
import json
from datetime import datetime

def parse_jrnl_file(filepath):
    """
    Parse the jrnl file and extract entries.
    
    Args:
        filepath (str): Path to the jrnl file.

    Returns:
        list: A list of journal entries, each as a dictionary.
    """

    with open(filepath, "r") as file:
        data = json.load(file)
    return data.get("entries", [])

def convert_jrnl_to_html(filepath, template="default"):
    """
    Convert jrnl entries to HTML content.

    Args:
        filepath (str): Path to the jrnl file.
        template (str): The name of the template to use (not yet implemented in this step).

    Returns:
        list: A list of dictionaries containing HTML-ready content.
    """
    entries = parse_jrnl_file(filepath)
    html_entries = []

    for entry in entries:
        html_entries.append({
            "date": format_date(entry["date"]),
            "title": entry["title"],
            "content": format_content(entry["body"]),
            "tags": entry["tags"]
        })

    return html_entries

def format_date(date_str):
    """
    Format the date string for display.

    Args:
        date_str (str): The original date string from the jrnl entry.

    Returns:
        str: Formatted date string.
    """
    try:
        # Assuming ISO 8601 date format (e.g., "2024-12-11T10:00:00")
        dt = datetime.fromisoformat(date_str)
        return dt.strftime("%B %d, %Y")  # e.g., "December 11, 2024"
    except ValueError:
        return date_str  # Return the original string if formatting fails

def format_content(content):
    """
    Format the journal content for HTML display.

    Args:
        content (str): The raw content of the journal entry.

    Returns:
        str: Content formatted as HTML.
    """
    # Replace newlines with <br> tags for HTML rendering
    return content.replace("\n", "<br>")
