import pathlib



def get_names_folders(path_for_folder:pathlib.Path):
    names_of_folders = []

    for folder in path_for_folder.iterdir():
        if folder.is_dir():
            folder_name = folder.name
            names_of_folders.append(folder_name)

    return names_of_folders
           