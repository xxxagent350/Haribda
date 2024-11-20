from os import path


def get_project_path() -> str:
    return path.dirname(path.abspath(__file__))

def get_global_path(local_path):
    return path.join(get_project_path(), local_path)
