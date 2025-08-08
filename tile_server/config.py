import os
from pathlib import Path
from pydantic import BaseModel


# Environment variables config

class _EnvConfig(BaseModel):
    class Config:
        alias_generator = str.upper
        populate_by_name = True

    cache_dir: Path = Path.home() / ".tile_server_cache"
    mapbox_token = ""
    overpass_api = "https://overpass-api.de/api"


env_config = _EnvConfig.model_validate(os.environ)
