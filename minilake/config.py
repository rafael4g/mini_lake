import os

from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="MINILAKE",
    root_path=os.path.dirname(__file__),
    settings_files=["settings.toml"],
)
