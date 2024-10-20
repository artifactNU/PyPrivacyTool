import os
import argparse


def secure_delete_file(file_path, passes=3, verbose=False):
    """
    Securely delete a file by overwriting it with random data.

    Args:
        file_path (str): The path to the file to be securely deleted.
        passes (int): Number of times to overwrite the file.
        verbose (bool): Enable verbose output.
    """
    if not os.path.isfile(file_path):
        if verbose:
            print(f"[!] File not found: {file_path}")
        return

    file_size = os.path.getsize(file_path)
    if verbose:
        print(f"[*] Securely deleting file: {file_path}")
        print(f"[*] File size: {file_size} bytes")
        print(f"[*] Overwriting {passes} time(s)")

    try:
        with open(file_path, "ba+", buffering=0) as f:
            length = f.tell()
            for pass_num in range(1, passes + 1):
                if verbose:
                    print(f"    - Pass {pass_num}/{passes}")
                f.seek(0)
                f.write(os.urandom(length))
                f.flush()
                os.fsync(f.fileno())
        os.remove(file_path)
        if verbose:
            print(f"[+] File securely deleted: {file_path}")
    except Exception as e:
        print(f"[!] Error deleting file {file_path}: {e}")


def secure_delete_directory(directory_path, passes=3, verbose=False):
    """
    Securely delete all files in a directory and its subdirectories.

    Args:
        directory_path (str): The path to the directory to be securely deleted.
        passes (int): Number of times to overwrite each file.
        verbose (bool): Enable verbose output.
    """
    if not os.path.isdir(directory_path):
        if verbose:
            print(f"[!] Directory not found: {directory_path}")
        return

    if verbose:
        print(f"[*] Securely deleting directory: {directory_path}")

    for root, dirs, files in os.walk(directory_path, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            secure_delete_file(file_path, passes, verbose)
        for name in dirs:
            dir_path = os.path.join(root, name)
            try:
                os.rmdir(dir_path)
                if verbose:
                    print(f"[+] Directory removed: {dir_path}")
            except Exception as e:
                print(f"[!] Error removing directory {dir_path}: {e}")
    try:
        os.rmdir(directory_path)
        if verbose:
            print(f"[+] Directory removed: {directory_path}")
    except Exception as e:
        print(f"[!] Error removing directory {directory_path}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Securely delete files or directories by overwriting them with random data.",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--file",
        "-f",
        dest="file_path",
        help="The path to the file to be securely deleted.",
    )
    group.add_argument(
        "--dir",
        "-d",
        dest="dir_path",
        help="The path to the directory to be securely deleted.",
    )

    parser.add_argument(
        "--passes",
        "-p",
        type=int,
        default=3,
        help="Number of overwrite passes (default: 3).",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose output.",
    )

    args = parser.parse_args()

    if args.file_path:
        secure_delete_file(args.file_path, args.passes, args.verbose)
    elif args.dir_path:
        secure_delete_directory(args.dir_path, args.passes, args.verbose)


if __name__ == "__main__":
    main()
