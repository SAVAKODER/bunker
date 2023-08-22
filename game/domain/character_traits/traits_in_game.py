import pathlib
from typing import List
from pydantic import BaseModel, field_validator
from game.services.game_setup_parts.setup_utilities.folder_names_collector import get_names_folders
from game.settings.game_settings import JSON_CHARACTERISTICS_DIRECTORY







class TraitsInGame(BaseModel):
    tratis_name: pathlib.Path = JSON_CHARACTERISTICS_DIRECTORY

    @field_validator('tratis_name')
    @classmethod
    def get_traits(cls, path : pathlib.Path) ->List[str]:
        return get_names_folders(path)


