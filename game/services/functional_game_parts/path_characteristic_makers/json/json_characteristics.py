import pathlib
from game.services.functional_game_parts.file_name_processing.file_name_json import make_file_name_with_json
from game.services.game_logic.make_path_to_characteristic.path_maker import PathCharacteristicsMaker


class PathJsonCharacteristicsMaker:
    def __init__(self, start_path:str) -> None:
        self.path_characteristic_maker = PathCharacteristicsMaker(start_path,make_file_name_with_json)

    def make_path(self, need_characteristic:str) ->pathlib.Path:
        return self.path_characteristic_maker.make_path(need_characteristic)