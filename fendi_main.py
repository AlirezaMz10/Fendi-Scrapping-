from bs4 import BeautifulSoup
import requests, json, re

# request to page
def request_to_page(url) :
    response = requests.get(url)
    if response.status_code != 200:
        request_to_page(url)
    return response

# create soup object
def create_soup(response) :
    soup = BeautifulSoup(response.content, "html.parser")
    return soup


# get categories url


# save all categories url in a file


# get and save all categories urls


# open product json file if exists
def open_file() :
    with open("product_urls.json", "r") as f:
        product_urls = json.load(f)
        f.close()
    return product_urls


# create product json file if it does not exist
def create_file(product_urls):
    try :
        with open("product_urls.json", "w") as f:
            product_urls = json.dumps(product_urls)
            f.write(product_urls)
            f.close
    except Exception as e :
        print("error in create_file is" + e)


# save product urls in a file
def save_main(product_urls) :
    try:
        products_file = open_file()
    except FileNotFoundError

