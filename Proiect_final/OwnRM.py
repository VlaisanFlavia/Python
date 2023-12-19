import os
import sys
import argparse
import shutil

def verb_file(file_path, log_file=None):
    message = f"removed file '{file_path}'"
    if log_file:
        with open(log_file, 'a') as log:
            log.write(f"{message}\n")
    else:
        print(message)
def verb_dir(file_path, log_file=None):
    message = f"removed directory '{file_path}'"
    if log_file:
        with open(log_file, 'a') as log:
            log.write(f"{message}\n")
    else:
        print(message)


def remove_files(file_paths, force=False, interactive=False, one_file_system=False, preserve_root=None, verbose=False,log_file=None):
    for file_path in file_paths:
        try:
            if not os.path.exists(file_path):
                if force:
                    continue
                else:
                    print(f"rm: cannot remove '{file_path}': No such file or directory")
                    sys.exit(1)

            if preserve_root == 'all' and os.path.abspath(file_path) == os.path.abspath('/'):
                print("rm: it is dangerous to operate recursively on '/'")
                sys.exit(1)

            if one_file_system and os.path.islink(file_path):
                continue
            if interactive:
                user_input = input(f"rm: remove '{file_path}'? ")
                if user_input.lower() in ('y', 'yes'):
                    os.remove(file_path)
                else:
                    print(f"cannot remove '{file_path}'")

            else:
                user_input = input(f"rm: remove '{file_path}'? ")
                if user_input.lower() in ('y', 'yes'):
                    os.remove(file_path)
                else:
                    print(f"cannot remove '{file_path}'")

            if os.path.isdir(file_path):
                print(f"rm: cannot remove '{file_path}': Is a directory")
                sys.exit(1)
            if verbose or log_file:
                verb_file(file_path, log_file=args.log)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
            sys.exit(1)

def remove_directory_recursive(directory, force=False, interactive=False, verbose=False, log_file=None):
    try:
        if interactive:
            user_input = input(f"rm: remove '{directory}'? ")
            if user_input.lower() not in ('y', 'yes'):
                print(f"{directory} was not deleted")
            else:
                shutil.rmtree(directory)
                if verbose or log_file:
                    verb_dir(directory, log_file=log_file)

        elif force:
            shutil.rmtree(directory)
            if verbose or log_file:
                verb_dir(directory, log_file=log_file)

        else:
            if not os.access(directory, os.W_OK):
                user_input = input(f"rm: remove write-protected directory '{directory}'? ")
                if user_input.lower() not in ('y', 'yes'):
                    print(f"{directory} was not deleted")
                else:
                    shutil.rmtree(directory)
                    if verbose or log_file:
                        verb_dir(directory, log_file=log_file)

    except Exception as e:
        print(f"Error deleting directory {directory}: {e}")
        sys.exit(1)

def remove_empty_directory(directory, force=False, interactive=False, verbose=False, log_file=None):
    try:
        if interactive:
            user_input = input(f"rm: remove '{directory}'? ")
            if user_input.lower() not in ('y', 'yes'):
                print(f"{directory} was not deleted")
            else:
                os.rmdir(directory)
                if verbose or log_file:
                    verb_dir(directory, log_file=log_file)

        elif force:
            os.rmdir(directory)
            if verbose or log_file:
                verb_dir(directory, log_file=log_file)

        else:
            if not os.access(directory, os.W_OK):
                user_input = input(f"rm: remove write-protected directory '{directory}'? ")
                if user_input.lower() not in ('y', 'yes'):
                    print(f"{directory} was not deleted")
                else:
                    os.rmdir(directory)
                    if verbose or log_file:
                        verb_dir(directory, log_file=log_file)

            else:
                os.rmdir(directory)
                if verbose or log_file:
                    verb_dir(directory, log_file=log_file)

    except Exception as e:
        print(f"Error deleting directory {directory}: {e}")
        sys.exit(1)


def remove_files_extension(directory, force=False, interactive=False, verbose=False, file_extension=None, log_file=None):
    for file in os.listdir(directory):
        if file.endswith(f".{file_extension}"):
            file_path = os.path.join(directory, file)
            try:
                if interactive:
                    user_input = input(f"rm: remove '{file_path}'? ")
                    if user_input.lower() not in ('y', 'yes'):
                        print(f"{file_path} was not deleted")
                    else:
                        os.remove(file_path)
                        if verbose or log_file:
                            verb_file(directory, log_file=log_file)
                elif force:
                    os.remove(file_path)
                    if verbose or log_file:
                        verb_file(file_path, log_file=log_file)

                else:
                    os.remove(file_path)
                    if verbose or log_file:
                        verb_file(file_path, log_file=log_file)
            except Exception as e:
                print(f"Error deleting file {file_path}: {e}")
            sys.exit(1)
        else:
            file_path = os.path.join(directory, file)
            if file_extension is None or os.path.isfile(file_path):
                try:
                    if interactive:
                        user_input = input(f"rm: remove '{file_path}'? ")
                        if user_input.lower() not in ('y', 'yes'):
                            print(f"{file_path} was not deleted")
                        else:
                            os.remove(file_path)
                            if verbose or log_file:
                                verb_file(file_path, log_file=log_file)
                    elif force:
                        os.remove(file_path)
                        if verbose or log_file:
                            verb_file(file_path, log_file=log_file)


                    else:
                        os.remove(file_path)
                        if verbose or log_file:
                            verb_file(file_path, log_file=log_file)
                except Exception as e:
                    print(f"Error deleting file {file_path}: {e}")
                    sys.exit(1)
                else:
                    print("f rm: there are no files with the extension")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove files or directories.")
    parser.add_argument('files', metavar='file', nargs='+', help='Files or directories to remove.')
    parser.add_argument('-f', '--force', action='store_true', help='Ignore nonexistent files and arguments, never prompt.')
    parser.add_argument('-i', '--interactive', action='store_true', help='Prompt before every removal.')
    parser.add_argument('-I', '--prompt-once', action='store_true', help='Prompt once before removing more than three files or when removing recursively.')
    parser.add_argument('--one-file-system', action='store_true', help='Skip directories on a different file system.')
    parser.add_argument('--no-preserve-root', action='store_true', help="Do not treat '/' specially.")
    parser.add_argument('--preserve-root', nargs='?', const='all', help="Do not remove '/'. With 'all', reject any command line argument on a separate device from its parent.")
    parser.add_argument('-r', '-R', '--recursive', action='store_true', help='Remove directories and their contents recursively.')
    parser.add_argument('-d', '--dir', action='store_true', help='Remove empty directories.')
    parser.add_argument('--ext', help='Remove files with a specific extension.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Explain what is being done.')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('--log', help='Log file to record removal operations.')

    args = parser.parse_args()

    if args.prompt_once and args.interactive:
        print("rm: conflicting options: -I and -i")
        sys.exit(1)

    if args.ext:
        for directory in args.files:
            remove_files_extension(directory, force=args.force, interactive=args.interactive, verbose=args.verbose, file_extension=args.ext)
    elif args.recursive:
        for directory in args.files:
            remove_directory_recursive(directory, force=args.force, interactive=args.interactive, verbose=args.verbose, log_file=args.log)
    elif args.dir:
            for directory in args.files:
                if not os.listdir(directory):
                    remove_empty_directory(directory, force=args.force, interactive=args.interactive, verbose=args.verbose, log_file=args.log)

                else:
                    print(f"{directory} is not empty")
    else:
        remove_files(args.files, force=args.force, interactive=args.interactive, one_file_system=args.one_file_system,
                     preserve_root=args.preserve_root, verbose=args.verbose,log_file=args.log)
