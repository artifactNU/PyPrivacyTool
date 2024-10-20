# main.py
import argparse
import sys
import os
from pyprivacytool import remove_metadata as metadata_remover
from pyprivacytool import secure_delete

# Add the parent directory to sys.path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)


def main():
    """
    Entry point for the PyPrivacyTool command-line interface.
    """
    parser = argparse.ArgumentParser(
        description="PyPrivacyTool: A suite of privacy-enhancing tools."
    )
    subparsers = parser.add_subparsers(
        title="Tools",
        dest="tool",
        help="Available privacy tools",
    )

    # Metadata Remover Subcommand
    parser_metadata = subparsers.add_parser(
        "remove-metadata", help="Remove metadata from files."
    )
    parser_metadata.add_argument(
        "--file", "-f", dest="file_path", required=True, help="File to process."
    )
    parser_metadata.add_argument(
        "--output", "-o", dest="output_path", help="Output file path."
    )
    parser_metadata.add_argument(
        "--list-formats",
        action="store_true",
        help="List supported file formats and exit.",
    )
    parser_metadata.set_defaults(func=metadata_remover.main)

    # Secure Delete Subcommand
    parser_delete = subparsers.add_parser(
        "secure-delete", help="Securely delete files or directories."
    )
    group = parser_delete.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", "-f", dest="file_path", help="File to delete.")
    group.add_argument("--dir", "-d", dest="dir_path", help="Directory to delete.")
    parser_delete.add_argument(
        "--passes", "-p", type=int, default=3, help="Number of overwrite passes."
    )
    parser_delete.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose output."
    )
    parser_delete.set_defaults(func=secure_delete.main)

    # Add subparsers for other tools similarly...

    args = parser.parse_args()

    if not args.tool:
        parser.print_help()
        return

    # Call the function associated with the chosen subcommand
    args.func(args)


if __name__ == "__main__":
    main()
