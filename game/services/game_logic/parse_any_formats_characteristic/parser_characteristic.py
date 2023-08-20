import json
from typing import Type
from game.services.game_logic.make_path_to_characteristic.path_maker import PathCharacteristicsMaker

class ParserCharacteristics:

    def __init__(self, path_maker:Type[PathCharacteristicsMaker]) -> None:
        self.path_maker = path_maker

    def make_characteristic_dict_object(self,need_characteristic:str) -> dict:
        path_to_needed_characteristic = self.path_maker.make_path(need_characteristic)

        with open(path_to_needed_characteristic, "r") as json_file:
            character_data = json.load(json_file)

        return character_data