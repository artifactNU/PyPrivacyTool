import os
from PIL import Image
from PyPDF2 import PdfFileReader as PdfReader, PdfFileWriter as PdfWriter
import mutagen
import argparse


# supported formats
formats = {
    "images": [".jpg", ".jpeg", ".png"],
    "pdfs": [".pdf"],
    "audio": [".mp3", ".flac", ".wav"],
}


# function to remove metadata from an image
def remove_image_metadata(image_path, output_path):
    """
    Remove metadata from an image file.

    Parameters:
    image_path (str): The path to the input image file.
    output_path (str): The path to save the output image file without metadata.
    """
    try:
        image = Image.open(image_path)
        # create a new image without metadata
        image.save(output_path, quality=95)
        print(f"Image metadata removed: {output_path}")
    except Exception as e:
        print(f"Error removing image metadata: {e}")


def remove_pdf_metadata(pdf_path, pdf_output_path):
    """
    Remove metadata from a PDF file.

    Parameters:
    pdf_path (str): The path to the input PDF file.
    pdf_output_path (str): The path to save the output PDF file without metadata.
    """
    try:
        reader = PdfReader(pdf_path)
        writer = PdfWriter()

        # copy over pages without the metadata
        for page in reader.pages:
            writer.add_page(page)

        # remove metadata
        writer.add_metadata({})

        with open(pdf_output_path, "wb") as f:
            writer.write(f)
        print(f"PDF metadata removed: {pdf_output_path}")
    except Exception as e:
        print(f"Error removing PDF metadata: {e}")


def remove_audio_metadata(audio_path):
    """
    Remove metadata from an audio file.

    Parameters:
    audio_path (str): The path to the input audio file.
    """
    try:
        audio = mutagen.File(audio_path, easy=True)
        if audio is not None:
            for tag in list(audio.keys()):
                del audio[tag]  # remove each metadata tag
            audio.save()
            print(f"Audio metadata removed: {audio_path}")
        else:
            print(f"Unsupported audio format: {audio_path}")
    except Exception as e:
        print(f"Error removing audio metadata: {e}")


def remove_metadata(file_path, output_path=None):
    """
    Remove metadata from the specified file and save the output to the given path.

    Args:
        file_path (str): The path to the file from which to remove metadata.
        output_path (str, optional): The path to save the file without metadata.
                                     Defaults to None.
    """
    _, file_extension = os.path.splitext(file_path)

    if file_extension.lower() in [".jpg", ".jpeg", ".png"]:
        if output_path is None:
            output_path = file_path
        remove_image_metadata(file_path, output_path)
    elif file_extension.lower() == ".pdf":
        if output_path is None:
            output_path = file_path
        remove_pdf_metadata(file_path, output_path)
    elif file_extension.lower() in [".mp3", ".flac", ".wav"]:
        if output_path is None:
            output_path = file_path
        remove_audio_metadata(file_path)
    else:
        print(f"Unsupported file type: {file_extension}")


def main():
    """
    Main function to parse arguments and remove metadata from files.
    """
    parser = argparse.ArgumentParser(
        description="Remove metadata from files.",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "--file",
        "-f",
        dest="file_path",
        help="The path to the file from which to remove metadata.",
    )
    parser.add_argument(
        "--output",
        "-o",
        dest="output_path",
        help="The path to save the file without metadata. Defaults to overwriting the input file.",
        default=None,
    )
    parser.add_argument(
        "--list-formats",
        action="store_true",
        help="List all supported file formats and exit.",
    )

    args = parser.parse_args()

    if args.list_formats:
        print("Supported file formats:")
        for category, extensions in formats.items():
            print(f"{category.capitalize()}: {', '.join(extensions)}")
        parser.print_help()
        exit(1)

    if not args.file_path:
        parser.print_help()
        return

    # validate file extension
    _, file_extension = os.path.splitext(args.file_path)
    file_extension = file_extension.lower()
    if file_extension not in [ext for exts in formats.values() for ext in exts]:
        print(f"Unsupported file type: {file_extension}")
        print(
            f"Supported formats are: {', '.join([ext for exts in formats.values() for ext in exts])}"
        )
        return

    remove_metadata(args.file_path, args.output_path)


if __name__ == "__main__":
    main()
