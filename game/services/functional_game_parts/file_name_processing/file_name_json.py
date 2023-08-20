from game.services.game_logic.file_utilities.file_name_utils import make_file_name_with_format


def make_file_name_with_json(file_name:str) -> str:

    file_name_with_json_format = make_file_name_with_format(file_name,'JSON')
    return file_name_with_json_format
