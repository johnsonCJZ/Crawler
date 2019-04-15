import os


def create_project_dir(directory: str):
    if not os.path.exists(directory):
        print("Creating project" + directory)
        os.makedirs(directory)


# Create queue and crawled files(if not created)

def create_data_files(project_name: str, base_url: str) -> None:
    queue = project_name + "/queue.txt"
    crawled = project_name + "/crawled.txt"
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, "")


# Create a new file
def write_file(path: str, data):
    f = open(path, "w")
    f.write(data)
    f.close()


# Add data onto an existing file
def append_to_file(path: str, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Delete the contents of a file
def delete_file_contents(path: str):
    with open(path, 'w'):
        pass