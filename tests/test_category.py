import os
import app.category as category
from returns.result import Result, Success, Failure


def test_agents():
    with open(os.path.join("tests", "category_agents.html"), encoding="UTF-16") as file:
        agents_html = file.read()
    
    categories = category.find_all(agents_html)
    assert len(categories) == 23
    
    tables = category.get_all(agents_html)
    assert len(tables) == 71, print(tables)

def test_elements():
    with open(os.path.join("tests", "category_elements.html"), encoding="UTF-16") as file:
        elements_html = file.read()

    tables = category.find_all(elements_html)
    assert len(tables) == 8

    
    element, anemo, cryo, dendro, electro, *_ = tables

    section = category.get_from(cryo)
    assert len(section) == 1

    section = category.get_from(dendro)
    assert len(section) == 1

    section = category.get_from(electro)
    assert len(section) == 1