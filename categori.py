from bs4 import BeautifulSoup
import requests, json

url = "https://www.fendi.com/de-en/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")


def get_category_url(soup):
    category_url = soup.find_all(
        "div", {"class": "c-header__inner-navbar--element"}
    ).find_all("div", {"class": "c-navbar__nav menu-group"}
    ).find_all(
        "li", {"class": "c-navbar__dropdown-list--item nav-item c-navbar__list-item dropdown"}
    ).find_all(
        "div", {"class": "c-navbar__dropdown-menu--level2"}
    ).find_all(
        "ul", {"class": "c-navbar__dropdown-sublist main-nav__primary__level3 nav align-content-start main-nav__primary__level3--tile-group"}
    ).find_all(
        "li", {"class": "c-navbar__dropdown-list--item nav-item c-navbar__dropdown-list--viewall"}
    ).find_all(
        "a", {"class": "c-dropdown-menu__link d-inline-block w-100 "}
    )
    return category_url

print(get_category_url(soup))
