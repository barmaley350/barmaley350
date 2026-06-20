"""main."""

from pathlib import Path


def create_steck_links(steck_md: Path, output_md: Path) -> None:
    """Create links.

    :param steck_md: _description_
    :type steck_md: Path
    :param output_md: _description_
    :type output_md: Path

    For icons
    https://simpleicons.org/

    For badges
    https://shields.io/badges/static-badge
    """
    stack = {
        "python": {
            "name": "Python",
            "logo": "python",
        },
        "pandas": {
            "name": "Pandas",
            "logo": "pandas",
        },
        "fastapi": {
            "name": "FastAPI",
            "logo": "fastapi",
        },
        "docker": {
            "name": "Docker",
            "logo": "docker",
        },
        "postgresql": {
            "name": "PostgreSQL",
            "logo": "postgresql",
        },
        "numpy": {
            "name": "NumPy",
            "logo": "numpy",
        },
        "clickhouse": {
            "name": "ClickHouse",
            "logo": "clickhouse",
        },
        "sqlalchemy": {
            "name": "SQLAlchemy",
            "logo": "sqlalchemy",
        },
        "pytest": {
            "name": "Pytest",
            "logo": "pytest",
        },
        "pydantic": {"name": "Pydantic", "logo": "pydantic"},
        "Apache-Airflow": {"name": "Apache_Airflow", "logo": "apache-airflow"},
        "Apache-Superset": {"name": "Apache_Superset", "logo": "apache-superset"},
        "django": {"name": "Django", "logo": "django"},
        "Nuxt": {"name": "NuxtJS", "logo": "nuxt"},
        "Git": {"name": "Git", "logo": "git"},
        "Celery": {"name": "Celery", "logo": "celery"},
        "jupyter": {"name": "Jupyter", "logo": "jupyter"},
    }
    with steck_md.open("r", encoding="utf-8") as input_file:
        content = input_file.read()

    for item in stack:
        name = stack[item]["name"]
        logo = stack[item]["logo"]
        url = f"![Static Badge](https://img.shields.io/badge/{name}-abcdef?style=for-the-badge&logo={logo})"
        content += f"\n{url}"

    with output_md.open("a", encoding="utf-8") as output_file:
        output_file.write(f"{content} \n\n")


def create_empty_md(output_md: Path):
    output_md.write_text("", encoding="utf-8")


def append_md(file_path: Path, output_md: Path):
    with file_path.open("r", encoding="utf-8") as input_file:
        content = input_file.read()

    with output_md.open("a", encoding="utf-8") as output_file:
        output_file.write(f"{content} \n\n")


if __name__ == "__main__":
    resources = {
        # "contact": Path(__file__).parent / "md/CONTACTS.md",
        "about": Path(__file__).parent / "md/ABOUT.md",
        "steck": Path(__file__).parent / "md/STECK.md",
    }
    output_md = Path(__file__).parent / "README.md"

    create_empty_md(output_md)

    for key, file_path in resources.items():
        if key == "steck":
            create_steck_links(file_path, output_md)
        else:
            append_md(file_path, output_md)
