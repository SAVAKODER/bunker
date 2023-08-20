import pathlib
from game.services.game_logic.parse_any_formats_characteristic.parser_characteristic import ParserCharacteristics
from game.services.functional_game_parts.path_characteristic_makers.json.json_characteristics import PathJsonCharacteristicsMaker



class ParserJsonCharacteristic:

    def __init__(self, start_path:pathlib.Path) -> None:
        self.parser = ParserCharacteristics(
            PathJsonCharacteristicsMaker(start_path)
        )

    def make_characteristic_dict_object(self,need_characteristic:str) -> dict:
        characteristic_object = self.parser.make_characteristic_dict_object(
            need_characteristic
        )
        return characteristic_object
        
    
