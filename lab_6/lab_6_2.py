import os


def list_directories_and_files(path):
    try:
        directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        print("Directories:")
        for d in directories:
            print(d)
        print("Files:")
        for f in files:
            print(f)
    except OSError as e:
        print("Error:", e)


def check_path_access(path):
    print("Checking access for path:", path)
    if os.path.exists(path):
        print("Path exists")
        print("Readable?", os.access(path, os.R_OK))
        print("Writable?", os.access(path, os.W_OK))
        print("Executable?", os.access(path, os.X_OK))
    else:
        print("Path does not exist")


def find_filename_and_directory(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print("Filename:", filename)
        print("Directory:", directory)
    else:
        print("Path does not exist")


def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            print("Number of lines in", filename, ":", len(lines))
    except FileNotFoundError:
        print("File not found.")


def write_list_to_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')


def generate_text_files():
    for char in range(ord('A'), ord('Z') + 1):
        filename = chr(char) + ".txt"
        with open(filename, 'w') as file:
            file.write("This is file: " + filename)


def copy_file(source, destination):
    try:
        with open(source, 'r') as src, open(destination, 'w') as dest:
            dest.write(src.read())
        print("File copied successfully.")
    except FileNotFoundError:
        print("File not found.")


def delete_file(path):
    if os.path.exists(path):
        try:
            os.remove(path)
            print("File deleted successfully.")
        except OSError as e:
            print("Error:", e)
    else:
        print("File does not exist.")


if __name__ == "__main__":
    path = "example_directory"  # Specify your desired path here
    list_directories_and_files(path)
    check_path_access(path)

    specific_path = "example_directory/example_file.txt"  # Specify your desired file path here
    find_filename_and_directory(specific_path)
    count_lines_in_file(specific_path)

    data_to_write = ["Line 1", "Line 2", "Line 3"]  # Data to write to file
    write_list_to_file("example_output.txt", data_to_write)

    generate_text_files()

    source_file = "example_file.txt"  # Source file to copy
    destination_file = "example_copy.txt"  # Destination file
    copy_file(source_file, destination_file)

    file_to_delete = "file_to_delete.txt"  # File to delete
    delete_file(file_to_delete)