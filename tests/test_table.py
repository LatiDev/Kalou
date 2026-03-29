import os
import app.table as table

def test_agents():
    with open(os.path.join("tests", "agents.html"), encoding="UTF-16") as file:
        agents_html = file.read()

    tables = table.find_all(agents_html)
    assert len(tables) == 2, len(tables)

    agents, *_ = tables

    rows = table.get_rows(agents)
    assert len(rows) == 47, len(rows)

    header, row, *_ = rows

    columns = table.get_columns(row)
    assert len(columns) == 8, len(columns)

def test_characters():
    with open(os.path.join("tests", "characters.html"), encoding="UTF-16") as file:
        characters_html = file.read()

    tables = table.find_all(characters_html)
    assert len(tables) == 11, len(tables)

    characters, *_ = tables

    rows = table.get_rows(characters)
    assert len(rows) == 110, len(rows)

    header, row, *_ = rows

    columns = table.get_columns(row)
    assert len(columns) == 9, len(columns)