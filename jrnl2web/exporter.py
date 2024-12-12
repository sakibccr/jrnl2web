import pathlib
from jinja2 import Environment, FileSystemLoader
from jrnl2web.utils import ensure_directory_exists, copy_static_files
from slugify import slugify

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
    Export HTML files based on journal entries.

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
    output_dir = pathlib.Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    entry_list = []

    # Generate individual entry pages
    for entry in entries:
        filename = slugify(entry["title"])
        entry_dir = output_dir / filename
        entry_dir.mkdir(parents=True, exist_ok=True)

        entry["url"] = entry_dir.relative_to(output_dir)
        html_content = render_template(env, "entry.html", {"entry": entry, "title": "My Journal"})

        filepath = entry_dir / "index.html"
        filepath.write_text(html_content)
        entry_list.append(entry)
        print(f"Generated: {filepath}")

    # Generate the index page
    index_filepath = output_dir / "index.html"
    context = {
        "entries": entry_list,
        "title": "My Journal"
    }
    index_content = render_template(env, "index.html", context)
    index_filepath.write_text(index_content)
    print(f"Generated: {index_filepath}")
