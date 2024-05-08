from bs4 import BeautifulSoup
import requests, json


# generate soup
def generate_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup


# single_product_url = "https://www.fendi.com/de-en/woman/new-in/fendi-filo-white-leather-court-shoes-8i8498na7f1ny8"
# soup = generate_soup(single_product_url)


# get products url
def get_products_urls(soup):
    product_url = soup.find(
        "div", {"class": "container-expanded container-fluid p-0"}
    ).find_all("a", {"class": "link"})
    return product_url


# get name
def find_name(soup):

    product_name = (
        soup.find_all("div", {"class": "product-name-hero"})[0]
        .find("h1", {"class": "product-name"})
        .text
    )
    return product_name


# get price
def find_price(soup):

    product_price = (
        soup.find("div", {"class": "d-flex align-items-center w-100"})
        .find("span", {"class": "value"})
        .text
    )
    return product_price


# get color
def find_color(soup):

    product_color = (
        soup.find_all("div", {"class", "attribute"})[0]
        .find("span", {"class", "product-detail-selected-color-value"})
        .text
    )
    return product_color


# get description
def find_product_descriptions(soup):

    product_detail = (
        soup.find(
            "div",
            {
                "class",
                "product-detail-attributes-container-inner product-detail-long-description",
            },
        )
        .find("div", {"class", "card-body px-0"})
        .find("p")
        .text
    )
    return product_detail


# get details
def find_product_details(soup):

    product_id = (
        soup.find(
            "div",
            {
                "class",
                "product-detail-attributes-container-inner product-detail-long-description",
            },
        )
        .find("div", {"class", "card-body px-0"})
        .find("div", {"class", "definition-list"})
        .text
    )
    return product_id


def get_product_data(url):
    soup = generate_soup(url)
    name = find_name(soup)
    color = find_color(soup)
    price = find_price(soup)
    descriptions = find_product_descriptions(soup)
    product_detail = find_product_details(soup)

    data = {
        "name": name,
        "color": color,
        "price": price,
        "descriptions": descriptions,
        "detail": product_detail,
    }

    return data


# url = "https://www.fendi.com/de-en/woman/new-in"
# url = "https://www.fendi.com/de-en/woman/bags"


# ***********************************************************************************************************

url = "https://www.fendi.com/de-en/woman/shoes"
soup = generate_soup(url)
products_urls = get_products_urls(soup)
for a_tag in products_urls:
    url = a_tag.get("href")
    print(json.dumps(get_product_data(url), indent=4))
    print("\n\n")


# ***********************************************************************************************************


# url = "https://www.fendi.com/de-en/woman/bags"


if __name__ == "__main__":
    # print(json.dumps(get_product_data(soup), indent=3))
    pass
