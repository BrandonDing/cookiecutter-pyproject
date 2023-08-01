{% if cookiecutter.configuration == 'y' and cookiecutter.logging == 'y' -%}
from {{cookiecutter.project_slug}} import settings, logger


def foo() -> str:
    """Summary line.

    Extended description of function.

    Args:
        foo (str): Description of arg1

    Returns:
        str: Description of return value
    """
    logger.info("I am not a foo.")
    return "foo"


{% endif -%}
{% if cookiecutter.configuration == 'y' and cookiecutter.logging != 'y' -%}
from {{cookiecutter.project_slug}} import settings


def foo() -> str:
    """Summary line.

    Extended description of function.

    Args:
        foo (str): Description of arg1

    Returns:
        str: Description of return value
    """
    return "foo"


{% endif -%}
{% if cookiecutter.configuration != 'y' and cookiecutter.logging == 'y' -%}
from {{cookiecutter.project_slug}} import logger


def foo() -> str:
    """Summary line.

    Extended description of function.

    Args:
        foo (str): Description of arg1

    Returns:
        str: Description of return value
    """
    logger.info("I am not a foo.")
    return "foo"


{% endif -%}
{% if cookiecutter.configuration != 'y' and cookiecutter.logging != 'y' -%}
def foo() -> str:
    """Summary line.

    Extended description of function.

    Args:
        foo (str): Description of arg1

    Returns:
        str: Description of return value
    """
    return "foo"


{% endif -%}


if __name__ == "__main__":  # pragma: no cover
    print(f"I am not a {foo()}")
