import click
import pathlib
import sys
import json
from jrnl2web.exporter import export_html

BASE_DIR = pathlib.Path(__file__).resolve().parent
THEME_DIR = BASE_DIR / 'themes'

def get_themes():
    """Retrieve available themes from the themes directory."""
    return tuple(theme.name for theme in THEME_DIR.iterdir() if theme.is_dir())

@click.command(
    help="""
    Convert jrnl entries to a collection of HTML pages for deployment as a static website.
    """
)
@click.option(
    "-i", "--input",
    type=click.Path(exists=True),
    help="Path to the input jrnl file (e.g. ~/.local/share/jrnl/journal.txt)."
)
@click.option(
    "-o", "--output",
    default='public',
    help="Path to the output directory for generated HTML files. Defaults to 'public'."
)
@click.option(
    "-t", "--theme",
    default="mini",
    type=click.Choice(get_themes()),
    help="Specify a theme to use (default: 'mini')."
)
def main(input, output, theme):
    """Main function to process the jrnl file and generate HTML."""
    # Handle input
    if input:
        try:
            with open(input, 'r') as f:
                json_data = json.load(f)
        except json.JSONDecodeError as e:
            click.echo(f"Invalid JSON input: {e}", err=True)
            sys.exit(1)
    else:
        if sys.stdin.isatty():
            click.echo("No input provided. Use --input or pipe JSON data.", err=True)
            sys.exit(1)
        try:
            json_data = json.load(sys.stdin)
        except json.JSONDecodeError as e:
            click.echo(f"Invalid JSON input: {e}", err=True)
            sys.exit(1)

    # Resolve output path
    outpath = pathlib.Path(output).resolve()

    # Resolve theme templates path
    templates = THEME_DIR / theme

    # Convert and export entries
    click.echo("Converting entries to HTML...")
    entries = json_data.get("entries", [])

    click.echo(f"Exporting HTML files to '{outpath}'...")
    export_html(entries, outpath, templates)

    click.echo("Conversion complete! Your journal entries are now available as a website.")

if __name__ == "__main__":
    main()
