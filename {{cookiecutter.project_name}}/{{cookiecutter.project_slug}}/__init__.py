{% if cookiecutter.configuration == 'y' and cookiecutter.logging == 'y' -%}
import os
from pathlib import Path
from dynaconf import Dynaconf
from loguru import logger


PROJECT_PATH = Path(__file__).parent.parent
settings = Dynaconf(
    root_path=str(PROJECT_PATH),
    envvar_prefix="DYNACONF",
    settings_files=['settings.yaml', '.secrets.yaml'],
)
logger.add(os.path.join(PROJECT_PATH, settings.log_path), rotation="1 month")
{% endif -%}
{% if cookiecutter.configuration == 'y' and cookiecutter.logging != 'y' -%}
import os
from pathlib import Path
from dynaconf import Dynaconf


PROJECT_PATH = Path(__file__).parent.parent
settings = Dynaconf(
    root_path=str(PROJECT_PATH),
    envvar_prefix="DYNACONF",
    settings_files=['settings.yaml', '.secrets.yaml'],
)
{% endif -%}
{% if cookiecutter.configuration != 'y' and cookiecutter.logging == 'y' -%}
import os
from pathlib import Path
from loguru import logger


PROJECT_PATH = Path(__file__).parent.parent
logger.add(os.path.join(PROJECT_PATH, 'logs/{{cookiecutter.project_slug}}.log'), rotation="1 month")
{% endif -%}
{% if cookiecutter.configuration != 'y' and cookiecutter.logging != 'y' -%}
{% endif -%}
