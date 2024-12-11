import click
import pathlib
import sys
import json
from jrnl2web.exporter import export_html
from rich import print

BASE_DIR = pathlib.Path(__file__).absolute().parent
THEME_DIR = BASE_DIR / 'themes'

def get_themes():
    themes = [item.name for item in pathlib.Path(THEME_DIR).iterdir() if item.is_dir()]
    return tuple(themes)

@click.command(help="This is a tool to convert jrnl entries to a collection of HTML pages which can be deployed as a static website.")
@click.option("-i", "--input",
              type=click.File('r', ),
              default=sys.stdin,
              help="Path to the input jrnl file (e.g. ~/.local/share/jrnl/journal.txt)."
    )
@click.option("-o", "--output",
              help="Path to the output directory where HTML files will be generated."
    )
@click.option("-t", "--theme",
              default="mini",
              type=click.Choice(get_themes()),
              help="Specify a theme to use (default: 'mini')."
    )
# @click.option("-", "--input", help="") Convert jrnl entries to HTML for deployment as a website.
def main(input, output, theme):

    output = pathlib.Path(BASE_DIR / output)
    templates = pathlib.Path(THEME_DIR / theme)

    # Convert jrnl entries to HTML content
    click.echo(f"Converting '{input}' to HTML...")
    data = json.load(input)
    entries = data.get("entries", [])

    # Export the converted entries to the output directory
    click.echo(f"Exporting HTML files to '{output}'...")
    export_html(entries, output, theme)

    click.echo("Conversion complete! Your journal entries are now available as a website.")

if __name__ == "__main__":
    main()
