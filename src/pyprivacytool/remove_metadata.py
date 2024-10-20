import os
from PIL import Image
from PyPDF2 import PdfReader, PdfWriter
import mutagen

# Supported formats
formats = {
    "images": [".jpg", ".jpeg", ".png"],
    "pdfs": [".pdf"],
    "audio": [".mp3", ".flac", ".wav"],
}

# Flatten the list of all supported formats
supported_formats = [ext for exts in formats.values() for ext in exts]


# Function to remove metadata from an image
def remove_image_metadata(image_path, output_path):
    """
    Remove metadata from an image file.

    Parameters:
    image_path (str): The path to the input image file.
    output_path (str): The path to save the output image file without metadata.
    """
    try:
        image = Image.open(image_path)

        # Remove EXIF data
        data = list(image.getdata())
        image_without_exif = Image.new(image.mode, image.size)
        image_without_exif.putdata(data)

        # Save the image without EXIF data
        image_without_exif.save(output_path, quality=95)
        print(f"Image metadata removed: {output_path}")
    except Exception as e:
        print(f"Error removing image metadata: {e}")
        # Optionally re-raise the exception for debugging
        # raise


# Function to remove metadata from a PDF
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

        # Copy over pages without the metadata
        for page in reader.pages:
            writer.add_page(page)

        # Remove metadata
        writer.add_metadata({})

        with open(pdf_output_path, "wb") as f:
            writer.write(f)
        print(f"PDF metadata removed: {pdf_output_path}")
    except Exception as e:
        print(f"Error removing PDF metadata: {e}")
        # Optionally re-raise the exception for debugging
        # raise


# Function to remove metadata from audio (e.g., MP3) files
def remove_audio_metadata(audio_path, output_path=None):
    """
    Remove metadata from an audio file.

    Parameters:
    audio_path (str): The path to the input audio file.
    output_path (str, optional): The path to save the cleaned audio file.
                                 Defaults to input path.
    """
    try:
        audio = mutagen.File(audio_path)
        if audio is not None:
            audio.delete()  # Remove all metadata
            if output_path is None:
                output_path = audio_path
            audio.save(output_path)
            print(f"Audio metadata removed: {output_path}")
        else:
            print(f"Unsupported audio format: {audio_path}")
    except Exception as e:
        print(f"Error removing audio metadata: {e}")
        # Optionally re-raise the exception for debugging
        # raise


def remove_metadata(file_path, output_path=None):
    """
    Remove metadata from the specified file and save the output to the given path.

    Args:
        file_path (str): The path to the file from which to remove metadata.
        output_path (str, optional): The path to save the file without metadata.
                                     Defaults to None.
    """
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()

    if file_extension in formats["images"]:
        if output_path is None:
            output_path = file_path
        remove_image_metadata(file_path, output_path)
    elif file_extension in formats["pdfs"]:
        if output_path is None:
            output_path = file_path
        remove_pdf_metadata(file_path, output_path)
    elif file_extension in formats["audio"]:
        if output_path is None:
            output_path = file_path
        remove_audio_metadata(file_path, output_path)
    else:
        print(f"Unsupported file type: {file_extension}")
        print(f"Supported formats are: {', '.join(supported_formats)}")


def main(args):
    """
    Main function to remove metadata from files based on provided arguments.

    Args:
        args: Parsed command-line arguments.
    """
    if args.list_formats:
        print("Supported file formats:")
        for category, extensions in formats.items():
            print(f"{category.capitalize()}: {', '.join(extensions)}")
        return

    if not args.file_path:
        print("Please provide a file path using --file or -f.")
        return

    # Validate file extension
    _, file_extension = os.path.splitext(args.file_path)
    file_extension = file_extension.lower()
    if file_extension not in supported_formats:
        print(f"Unsupported file type: {file_extension}")
        print(f"Supported formats are: {', '.join(supported_formats)}")
        return

    remove_metadata(args.file_path, args.output_path)
