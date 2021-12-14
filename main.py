import json
import os


def max_depth(startpath):
    max_d = 0
    for path, dirs, files in os.walk(startpath):
        current_d = path.count(os.sep) - startpath.count(os.sep)
        # print(path, '-->', startpath)
        if current_d > max_d:
            max_d = current_d
    return max_d


def number_of_files_and_directories(startpath):
    nb_files = 0
    nb_dir = 0
    for path, dirs, files in os.walk(startpath):
        nb_files += len(files)
        nb_dir += len(dirs)
    return nb_files, nb_dir


def dir_size(startpath):
    list_size_dir = {}
    for path, dirs, files in os.walk(startpath):
        for d in dirs:
            dp = os.path.join(path, d)
            list_size_dir.update({d: get_size(dp)})
    return list_size_dir


def stats_file_extension(startpath, ext):
    nb_files = 0

    list_nb_files = {}  # numarul fisierelor pentru fiecare extensie
    list_size_files = {}  # marimea fisierelor pentru fiecare extensie
    for i in ext:
        list_size_files.update({i: 0})
        list_nb_files.update({i: 0})

    for path, dirs, files in os.walk(startpath):
        for f in files:
            filename, file_extension = os.path.splitext(f)
            if file_extension in ext:
                # numarul fisierelor pentru fiecare extensie
                tmp_nb = list_nb_files.get(file_extension)
                tmp_nb += 1
                list_nb_files.update({file_extension: tmp_nb})

                # numarul total de fisiere
                nb_files += 1

                # marimea fisierelor pentru fiecare extensie
                fp = os.path.join(path, f)
                tmp_size = list_size_files.get(file_extension)
                tmp_size += os.path.getsize(fp)
                list_size_files.update({file_extension: tmp_size})

    return nb_files, list_nb_files, list_size_files


def get_level_size(startpath):
    level_size = [0] * (max_depth(startpath) + 1)
    level_size[0] = get_size(startpath)
    for path, dirs, files in os.walk(startpath):
        level = path.replace(startpath, '').count(os.sep)
        for d in dirs:
            dp = os.path.join(path, d)
            # print(level, get_size(dp))
            level_size[level + 1] += get_size(dp)
    return level_size


def get_size(path):
    directory_size = 0

    # get size
    for path, dirs, files in os.walk(path):
        for f in files:
            fp = os.path.join(path, f)
            directory_size += os.path.getsize(fp)
    return directory_size


# MAIN

data = {}
folder_input_path = 'C:\\PartitieD\\FACULTATE\\3sem1\\Test'
json_output_path = 'C:\\PartitieD\\FACULTATE\\3sem1'

# path input
# while True:
#     folder_input_path = str(input("Folder input path: "))
#     # list_files(folder_input_path)
#     # print(folder_input_path)
#     if os.path.isdir(folder_input_path):
#         break
#     else:
#         print("Path gresit, reintroduceti path")

# path output
# while True:
#     json_output_path = str(input("JSON output path: "))
#     # list_files(json_path_output)
#     # print(json_path_output)
#     if os.path.isdir(json_output_path):
#         break
#     else:
#         print("Path gresit, reintroduceti path")

# File extensions input
ext_list = ['.exe', '.jpg']

print("Input file extensions with dot before and finish with \'0\' ")

# while True:
#     x = str(input("\tFile extension:"))
#     if x != "0":
#         ext_list.append(x)
#     else:
#         break

x1, x2 = number_of_files_and_directories(folder_input_path)
x3, x4, x5 = stats_file_extension(folder_input_path, ext_list)

# print(ext_list)
data.update({'max_depth': max_depth(folder_input_path)})
data.update({'number_of_all_files': x1})
data.update({'number_of_all_directories': x2})
data.update({'level_sizes': get_level_size(folder_input_path)})
data.update({'number_of_all_files_by_ext': x3})
data.update({'number_of_files_by_ext': x4})
data.update({'size_of_files_by_ext': x5})
data.update({'directory_name_and_size': dir_size(folder_input_path)})
# data.max_depth = max_depth(folder_input_path)
# data.number_of_all_files, data.number_of_all_directories = number_of_files_and_directories(folder_input_path)
# data.level_sizes = get_level_size(folder_input_path)
# data.number_of_all_files_by_ext, data.number_of_files_by_ext, data.size_of_files_by_ext = stats_file_extension(
#     folder_input_path, ext_list)

if str(input("Doresti sa exportezi JSON?\n\t")) == "Da":
    json_data = json.dumps(data)
    with open(json_output_path + '\\data.json', 'w') as f:
        json.dump(data, f)
else:
    print("Ok, have a nice day!\n\n")

items = data.items()
for i in items:
    print(i)
