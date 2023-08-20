import pathlib
from typing import Callable


class PathCharacteristicsMaker:
    def __init__(self,
                 start_path:pathlib.Path,
                 filename_with_format_maker: Callable[[str,str],str]
                 ) -> None:
        self.filename_with_format_maker = filename_with_format_maker
        self.start_path = start_path

    def _make_name_of_file(self,need_characteristic:str) -> str:
        file_name_with_format = self.filename_with_format_maker(need_characteristic)
        return file_name_with_format

    def make_path(self,need_characteristic:str) ->pathlib.Path:
        file_with_characteristic = self._make_name_of_file(need_characteristic)
        path_for_out = self.start_path.joinpath(need_characteristic,file_with_characteristic)

        return path_for_out