"""main."""

from pathlib import Path


def prepare_stack(d: dict) -> dict:
    dn = {}
    for k, v in d.items():
        dn.setdefault(v["category"], []).append(k)
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
        "python": {
            "name": "Python",
            "logo": "python",
            "type": "programming language",
            "category": "Development & Engineering",
        },
        "pandas": {
            "name": "Pandas",
            "logo": "pandas",
            "type": "data analysis",
            "category": "Data & Analytics",
        },
        "fastapi": {
            "name": "FastAPI",
            "logo": "fastapi",
            "type": "web framework",
            "category": "Development & Engineering",
        },
        "docker": {
            "name": "Docker",
            "logo": "docker",
            "type": "containerization",
            "category": "Development & Engineering",
        },
        "postgresql": {
            "name": "PostgreSQL",
            "logo": "postgresql",
            "type": "database",
            "category": "Data & Analytics",
        },
        "numpy": {
            "name": "NumPy",
            "logo": "numpy",
            "type": "scientific computing",
            "category": "Data & Analytics",
        },
        "clickhouse": {
            "name": "ClickHouse",
            "logo": "clickhouse",
            "type": "database",
            "category": "Data & Analytics",
        },
        "sqlalchemy": {
            "name": "SQLAlchemy",
            "logo": "sqlalchemy",
            "type": "ORM",
            "category": "Supporting Tools",
        },
        "pytest": {
            "name": "Pytest",
            "logo": "pytest",
            "type": "testing",
            "category": "Testing & Quality",
        },
        "pydantic": {
            "name": "Pydantic",
            "logo": "pydantic",
            "type": "data validation",
            "category": "Supporting Tools",
        },
        "Apache-Airflow": {
            "name": "Apache Airflow",
            "logo": "apache-airflow",
            "type": "workflow orchestration",
            "category": "Data & Analytics",
        },
        "Apache-Superset": {
            "name": "Apache Superset",
            "logo": "apache-superset",
            "type": "data visualization",
            "category": "Data & Analytics",
        },
        "django": {
            "name": "Django",
            "logo": "django",
            "type": "web framework",
            "category": "Development & Engineering",
        },
        "Nuxt": {
            "name": "NuxtJS",
            "logo": "nuxt",
            "type": "frontend framework",
            "category": "Development & Engineering",
        },
        "Git": {
            "name": "Git",
            "logo": "git",
            "type": "version control",
            "category": "Development & Engineering",
        },
        "Celery": {
            "name": "Celery",
            "logo": "celery",
            "type": "task queue",
            "category": "Supporting Tools",
        },
        "jupyter": {
            "name": "Jupyter",
            "logo": "jupyter",
            "type": "interactive computing",
            "category": "Supporting Tools",
        },
    }

    with stack_md.open("r", encoding="utf-8") as input_file:
        content = input_file.read()

    stack1 = prepare_stack(stack)

    for skill_type, items in stack1.items():
        content += f"\n## {skill_type}"
        for item in items:
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
        "stack": Path(__file__).parent / "md/STACK.md",
    }
    output_md = Path(__file__).parent / "README.md"

    create_empty_md(output_md)

    for key, file_path in resources.items():
        if key == "stack":
            create_stack_links(file_path, output_md)
        else:
            append_md(file_path, output_md)
