Simple tool to convert your [jrnl](https://jrnl.sh/en/stable/) entries into a _ready to publish_ website.

### How to use
To use this tool, follow these steps:

1. Export your `jrnl` entries in a JSON format using this command: `jrnl --export json`. See the [jrnl documentations](https://jrnl.sh/en/v2.4.4/export/) for more information.
2. Run the following command to convert the entries into HTML website: `python main.py --input <path/to/jrnl.json> --output /output/dir/path`

Now you should have a working website in the output directory.

### How to modify the styles
This tool uses [jinja2](https://jinja.palletsprojects.com/en/stable/) templates (located in the `templates` directory). You can modify these templates however you want. For styles, you can modify the `styles.css` file in the `static/css` directory to suit your needs.
