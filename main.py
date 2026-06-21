"""main."""

from pathlib import Path


def prepare_stack(d: dict) -> dict:
    dn = {}
    for k, v in d.items():
        dn.setdefault(v["type"], []).append(k)
    return dn


def create_stack_links(stack_md: Path, output_md: Path) -> None:
    """Create links.

    :param stack_md: _description_
    :type stack_md: Path
    :param output_md: _description_
    :type output_md: Path

    For icons
    https://simpleicons.org/

    For badges
    https://shields.io/badges/static-badge
    """
    stack = {
        "Python": {
            "name": "Python",
            "logo": "python",
            "category": "Development & Engineering",
            "type": "Backend",
        },
        "Pandas": {
            "name": "Pandas",
            "logo": "pandas",
            "category": "Data & Analytics",
            "type": "Data Analysis",
        },
        "Fastapi": {
            "name": "FastAPI",
            "logo": "fastapi",
            "category": "Development & Engineering",
            "type": "Backend",
        },
        "Docker": {
            "name": "Docker",
            "logo": "docker",
            "category": "Development & Engineering",
            "type": "Supporting Tools",
        },
        "Postgresql": {
            "name": "PostgreSQL",
            "logo": "postgresql",
            "category": "Data & Analytics",
            "type": "Database",
        },
        "Numpy": {
            "name": "NumPy",
            "logo": "numpy",
            "category": "Data & Analytics",
            "type": "Data Analysis",
        },
        "Clickhouse": {
            "name": "ClickHouse",
            "logo": "clickhouse",
            "category": "Data & Analytics",
            "type": "Database",
        },
        "Sqlalchemy": {
            "name": "SQLAlchemy",
            "logo": "sqlalchemy",
            "category": "Supporting Tools",
            "type": "Supporting Tools",
        },
        "Pytest": {
            "name": "Pytest",
            "logo": "pytest",
            "category": "Testing & Quality",
            "type": "Testing & Quality",
        },
        "Pydantic": {
            "name": "Pydantic",
            "logo": "pydantic",
            "category": "Supporting Tools",
            "type": "Supporting Tools",
        },
        "Apache-Airflow": {
            "name": "Apache_Airflow",
            "logo": "apache-airflow",
            "category": "Data & Analytics",
            "type": "Data Analysis",
        },
        "Apache-Superset": {
            "name": "Apache_Superset",
            "logo": "apache-superset",
            "category": "Data & Analytics",
            "type": "Data Analysis",
        },
        "Matplotlib": {
            "name": "Matplotlib",
            "logo": "matplotlib",
            "category": "Data & Analytics",
            "type": "Data Analysis",
        },
        "Seaborn": {
            "name": "Seaborn",
            "logo": "seaborn",
            "category": "Data & Analytics",
            "type": "Data Analysis",
        },
        "Django": {
            "name": "Django",
            "logo": "django",
            "category": "Development & Engineering",
            "type": "Backend",
        },
        "Django REST Framework (DRF)": {
            "name": "Django_REST_Framework_(DRF)",
            "logo": "Django_REST_Framework_(DRF)",
            "category": "Development & Engineering",
            "type": "Backend",
        },
        "Nuxt": {
            "name": "NuxtJS",
            "logo": "nuxt",
            "category": "Development & Engineering",
            "type": "Frontend",
        },
        "Git": {
            "name": "Git",
            "logo": "git",
            "category": "Development & Engineering",
            "type": "Supporting Tools",
        },
        "Celery": {
            "name": "Celery",
            "logo": "celery",
            "category": "Supporting Tools",
            "type": "Supporting Tools",
        },
        "Jupyter": {
            "name": "Jupyter",
            "logo": "jupyter",
            "category": "Supporting Tools",
            "type": "Supporting Tools",
        },
    }

    with stack_md.open("r", encoding="utf-8") as input_file:
        content = input_file.read()

    stack1 = prepare_stack(stack)

    for skill_type, items in stack1.items():
        content += f"\n### {skill_type}"
        for item in items:
            name = stack[item]["name"]
            logo = stack[item]["logo"]
            url = f"![{item}](https://img.shields.io/badge/{name}-white?logo={logo})"
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
        "stack": Path(__file__).parent / "md/STACK.md",
    }
    output_md = Path(__file__).parent / "README.md"

    create_empty_md(output_md)

    for key, file_path in resources.items():
        if key == "stack":
            create_stack_links(file_path, output_md)
        else:
            append_md(file_path, output_md)
