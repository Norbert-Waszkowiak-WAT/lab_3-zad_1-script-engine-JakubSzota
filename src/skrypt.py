import requests
from faker import Faker
import random

BASE_URL = 'http://127.0.0.1:8080/api'

fake = Faker()

def create_affiliation(parent=None):
    url = BASE_URL + '/affiliation'
    data = {
        "name": fake.company(),
        "parent": create_affiliation() if random.random() < 0.25 else None
    }
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print("Affiliation ok")
        print("Response JSON:", response.json())
        return response.json().get('id')
    else:
        print("Affiliation status code:", response.status_code)
        print("Affiliation response text:", response.text)
        return None

def create_author(parent=None):
    url = BASE_URL + '/author'   
    data = {
        "surname": fake.last_name(),
        "name": fake.first_name(),
        "affiliation": create_affiliation()
    }
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print("Author ok")
        print("Response JSON:", response.json())
        return response.json().get('id')
    else:
        print("Author status code:", response.status_code)
        print("Author response text:", response.text)
        return None

def create_article():
    url = BASE_URL + '/article'
    data = {
        "title": fake.text(),
        "collection": fake.word(),
        "score": random.randint(1, 200),
        "vol": random.randint(1, 200),
        "year": random.randint(1900, 2023),
        "no": random.randint(1, 150),
        "articleNo": random.randint(1, 50),
        "journal": create_journal(),
        "authors": [create_author(), create_author(), create_author()]
    }
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print("Article ok")
        return response.json()
    else:
        print("Article status code:", response.status_code)
        print("Article response text:", response.text)
        return None

def create_journal():
    url = BASE_URL + '/journal'
    publisher = create_publisher()
    if not publisher:
        return None
    data = {
        "issn": fake.isbn13(),
        "baseScore": random.randint(1, 30),
        "title": fake.text(max_nb_chars=20),
        "publisher": publisher.get('id')
    }
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print("Journal ok")
        return response.json()
    else:
        print("Journal status:", response.status_code)
        print("Journal response:", response.text)
        return None

def create_publisher():
    url = BASE_URL + '/publisher'
    data = {
        "name": fake.company(),
        "location": fake.city()
    }
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print("Publisher ok")
        return response.json()
    else:
        print("Publisher status:", response.status_code)
        print("Publisher response:", response.text)
        return None

def create_book():
    url = BASE_URL + '/book'
    data = {
        "isbn": fake.word(),
        "year": fake.year(),
        "baseScore": random.randint(1,30),
        "title": fake.text(),
        "editor": create_author(),
        "publisher": create_publisher(),
        "name": fake.company(),
        "location": fake.city()
    }
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print("book ok")
        return response.json()
    else:
        print("book status:", response.status_code)
        print("book response:", response.text)
        return None



def create_chapter():
    url = BASE_URL + '/chapter'
    data = {
        "score": random.randint(1,30),
        "collection": fake.word(),
        "title": fake.text(),
        "book": create_book(),
        "authors": [create_author(), create_author()]
    }
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print("chapter ok")
        return response.json()
    else:
        print("chapter status:", response.status_code)
        print("chapter response:", response.text)
        return None


# article, journal, affiliation, author, publisher,book , chapter działają
if __name__ == "__main__":
    for _ in range(12):
        create_article()
    for _ in range(12):
        create_journal()
    for _ in range(12):
        create_affiliation()
    for _ in range(12):
        create_author()
    for _ in range(12):
        create_publisher()
    for _ in range(12):
        create_book()
    for _ in range(12):
        create_chapter()