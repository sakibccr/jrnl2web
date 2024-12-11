import os
import pathlib
from jinja2 import Environment, FileSystemLoader
from jrnl2web.utils import ensure_directory_exists, copy_static_files

THEME_DIR = pathlib.Path('themes/')

def setup_jinja_env(template_dir):
    """
    Set up the Jinja2 environment for rendering templates.

    Args:
        template_dir (str): Path to the directory containing HTML templates.

    Returns:
        Environment: Configured Jinja2 environment.
    """
    return Environment(loader=FileSystemLoader(template_dir))

def render_template(env, template_name, context):
    """
    Render an HTML template with the given context.

    Args:
        env (Environment): Jinja2 environment.
        template_name (str): Name of the template file.
        context (dict): Context data for rendering.

    Returns:
        str: Rendered HTML content.
    """
    template = env.get_template(template_name)
    return template.render(context)

def export_html(entries, output_dir, theme):
    """
    Export the HTML files based on journal entries.

    Args:
        entries (list): List of dictionaries containing HTML-ready journal entries.
        output_dir (str): Directory where the HTML files will be generated.
        theme (str): Directory containing HTML templates.

    Returns:
        None
    """

    # Set up the Jinja2 environment
    env = setup_jinja_env(THEME_DIR / theme)

    # Ensure output directory exists
    ensure_directory_exists(output_dir)

    # Copy static files to output
    copy_static_files('static/', output_dir)

    # Ensure output directory exists
    if not output_dir.exists():
        output_dir.mkdir()

    # Generate individual entry pages
    for index, entry in enumerate(entries):
        filename = f"entry_{index + 1}.html"
        filepath = os.path.join(output_dir, filename)
        context = {
            "entry": entry,
            "title": entry["title"]
        }
        html_content = render_template(env, "entry.html", context)

        with open(filepath, "w", encoding="utf-8") as file:
            file.write(html_content)
        print(f"Generated: {filepath}")

    # Generate the index page
    index_filepath = os.path.join(output_dir, "index.html")
    context = {
        "entries": [
            {"title": entry["title"], "date": entry["date"], "filename": f"entry_{i + 1}.html"}
            for i, entry in enumerate(entries)
        ],
        "title": "Journal Index"
    }
    index_content = render_template(env, "index.html", context)

    with open(index_filepath, "w", encoding="utf-8") as file:
        file.write(index_content)
    print(f"Generated: {index_filepath}")
