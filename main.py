import argparse
import os
from jrnl2web.converter import convert_jrnl_to_html
from jrnl2web.exporter import export_html

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description="Convert jrnl entries to HTML for deployment as a website."
    )
    parser.add_argument(
        "--input",
        "-i",
        required=True,
        help="Path to the input jrnl file (e.g., 'sample.jrnl')."
    )
    parser.add_argument(
        "--output",
        "-o",
        required=True,
        help="Path to the output directory where HTML files will be generated."
    )
    parser.add_argument(
        "--template",
        "-t",
        default="default",
        help="Specify a template to use (default: 'default')."
    )
    args = parser.parse_args()

    # Validate input file
    if not os.path.exists(args.input):
        print(f"Error: Input file '{args.input}' not found.")
        exit(1)

    # Validate or create output directory
    if not os.path.exists(args.output):
        os.makedirs(args.output)

    # Convert jrnl entries to HTML content
    print(f"Converting '{args.input}' to HTML...")
    entries = convert_jrnl_to_html(args.input, template=args.template)

    # Export the converted entries to the output directory
    print(f"Exporting HTML files to '{args.output}'...")
    export_html(entries, args.output)

    print("Conversion complete! Your journal entries are now available as a website.")

if __name__ == "__main__":
    main()
