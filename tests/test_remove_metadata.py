import unittest
from pyprivacytool import remove_metadata
from PIL import Image
from PyPDF2 import PdfReader
import mutagen
import os


class TestRemoveMetadata(unittest.TestCase):
    """Unit tests for the remove_metadata functions in the pyprivacytool module."""

    def setUp(self):
        # Create a test image with metadata
        self.test_image = "test_image_with_metadata.jpg"
        image = Image.new("RGB", (100, 100), color="red")
        exif_data = image.getexif()
        exif_data[0x010E] = "Test Image Description"  # Add ImageDescription tag
        image.save(self.test_image, exif=exif_data)

        # Create a test PDF with metadata
        self.test_pdf = "test_pdf_with_metadata.pdf"
        with open(self.test_pdf, "wb") as f:
            f.write(b"%PDF-1.4\n%Test PDF with metadata\n")
            f.write(b"1 0 obj\n<< /Title (Test PDF) /Author (Test Author) >>\nendobj\n")

        # Create a test audio file with metadata
        self.test_audio = "test_audio_with_metadata.mp3"
        with open(self.test_audio, "wb") as f:
            f.write(b"Test audio data")

        # Use mutagen to add metadata
        audio_file = mutagen.File(self.test_audio, easy=True)
        if audio_file is None:
            audio_file = mutagen.File(self.test_audio, easy=True, force_id3=True)
        if audio_file is not None:
            audio_file["artist"] = "Test Artist"
            audio_file.save()

    def tearDown(self):
        # Remove test files
        files_to_remove = [
            self.test_image,
            "clean_" + self.test_image,
            self.test_pdf,
            "clean_" + self.test_pdf,
            self.test_audio,
        ]
        for file in files_to_remove:
            if os.path.exists(file):
                os.remove(file)

    def test_remove_image_metadata(self):
        """Test the removal of metadata from an image file."""
        output_image = "clean_" + self.test_image
        remove_metadata.remove_image_metadata(self.test_image, output_image)
        # Verify that the output image exists
        self.assertTrue(os.path.exists(output_image))

        # Check that metadata has been removed
        image = Image.open(output_image)
        exif_data = image.getexif()
        self.assertEqual(len(exif_data.items()), 0, "Image metadata was not removed")

    def test_remove_pdf_metadata(self):
        """Test the removal of metadata from a PDF file."""
        output_pdf = "clean_" + self.test_pdf
        remove_metadata.remove_pdf_metadata(self.test_pdf, output_pdf)
        # Verify that the output PDF exists
        self.assertTrue(os.path.exists(output_pdf))

        # Check that metadata has been removed
        reader = PdfReader(output_pdf)
        self.assertEqual(reader.metadata, {}, "PDF metadata was not removed")

    def test_remove_audio_metadata(self):
        """Test the removal of metadata from an audio file."""
        remove_metadata.remove_audio_metadata(self.test_audio)
        # Check that metadata has been removed
        audio_file = mutagen.File(self.test_audio, easy=True)
        self.assertEqual(len(audio_file.keys()), 0, "Audio metadata was not removed")

    def test_remove_metadata(self):
        """Test the general remove_metadata function with various file types."""
        # Test with image
        output_image = "clean_" + self.test_image
        remove_metadata.remove_metadata(self.test_image, output_image)
        self.assertTrue(os.path.exists(output_image))
        image = Image.open(output_image)
        exif_data = image.getexif()
        self.assertEqual(len(exif_data.items()), 0, "Image metadata was not removed")

        # Test with PDF
        output_pdf = "clean_" + self.test_pdf
        remove_metadata.remove_metadata(self.test_pdf, output_pdf)
        self.assertTrue(os.path.exists(output_pdf))
        reader = PdfReader(output_pdf)
        self.assertEqual(reader.metadata, {}, "PDF metadata was not removed")

        # Test with audio
        remove_metadata.remove_metadata(self.test_audio)
        audio_file = mutagen.File(self.test_audio, easy=True)
        self.assertEqual(len(audio_file.keys()), 0, "Audio metadata was not removed")


if __name__ == "__main__":
    unittest.main()
