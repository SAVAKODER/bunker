import json
from game.services.game_logic.make_path_to_characteristic.path_maker import PathCharacteristicsMaker

class ParserCharacteristicsWindows(PathCharacteristicsMaker):

    def make_characteristic_dict_object(self,need_characteristic:str) -> dict:
        path_to_needed_characteristic = self.path_maker.make_path(need_characteristic)

        with open(path_to_needed_characteristic, "r",encoding="utf-8") as json_file:
            character_data = json.load(json_file)

        return character_data