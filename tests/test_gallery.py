import os
import app.gallery as gallery
import bs4

def test_attribute():
    with open(os.path.join("tests", "gallery_attribute.html"), encoding="UTF-16") as file:
        attribute_html = file.read()

    attributes: list[bs4.Tag] = gallery.find_all(attribute_html)
    assert(len(attributes) == 1), len(attributes)

    attribute_gallery, *other = attributes
    is_valid = gallery.is_valid(attribute_gallery, gallery.DEFAULT_GALLERY)
    assert(is_valid), len(is_valid)

    elements = gallery.scrap(attribute_gallery)
    assert(len(elements) == 5), len(elements)

def test_speciality():
    with open(os.path.join("tests", "gallery_speciality.html"), encoding="UTF-16") as file:
        speciality_html = file.read()

    specialities: list[bs4.Tag] = gallery.find_all(speciality_html)
    assert(len(specialities) == 1), len(specialities)

    speciality_gallery, *other = specialities
    is_valid = gallery.is_valid(speciality_gallery, gallery.DEFAULT_GALLERY)
    assert(is_valid), len(is_valid)

    elements = gallery.scrap(speciality_gallery)
    assert(len(elements) == 6), len(elements)