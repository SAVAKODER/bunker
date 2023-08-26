import json
from game.services.game_logic.parse_any_formats_characteristic.parser_characteristic import ParserCharacteristics

class ParserCharacteristicsWindows(ParserCharacteristics):

    def make_characteristic_dict_object(self,need_characteristic:str) -> dict:
        path_to_needed_characteristic = self.path_maker.make_path(need_characteristic)

        with open(path_to_needed_characteristic, "r",encoding="utf-8") as json_file:
            character_data = json.load(json_file)

        return character_data