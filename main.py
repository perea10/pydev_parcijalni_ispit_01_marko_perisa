import json
from typing import Dict
import os

OFFERS_FILE = "offers.json"
PRODUCTS_FILE = "products.json"
CUSTOMERS_FILE = "customers.json"
STARS = 40


def load_data(customers, offers, products):
    """Load data from a JSON file."""
    try:
        with open(customers, "r") as file_reader_customers:
            return json.load(file_reader_customers)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Error decoding {file_reader_customers}. Check file format.")
        return []
    try:
        with open(offers, "r") as file_reader_offers:
            return json.load(file_reader_offers)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Error decoding {file_reader_offers}. Check file format.")
        return []
    try:
        with open(products, "r") as file_reader_products:
            return json.load(file_reader_products)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Error decoding {file_reader_products}. Check file format.")
        return []


def save_data(offers, products):
    """Save data to a JSON file."""
    with open(offers, "w") as file_writer:
        json.dump(products, offers, indent=4)
    return products, offers

# TODO: Implementirajte funkciju za kreiranje nove ponude.
def create_new_offer(offers, products, customers):
    """
    Prompt user to create a new offer by selecting a customer, entering date,
    choosing products, and calculating totals.
    """
    offers = load_data(OFFERS_FILE)
    products = load_data(PRODUCTS_FILE)
    customers = load_data(CUSTOMERS_FILE)
    # Omogućite unos kupca

    # Print liste kupaca -> kupac upise broj ispred a vi onda pokupite te podatke
    # za ovo bi dobro dosla while True petlja s brake izlazom
    print('\n\n Kreiranje nove ponude ')
    print('*'*STARS)
    print(offers)
    print('1. Odabir kupca')
    print('2. Odabir proizvoda i količine')
    print('3. Izračun ukupne cijene')
    print('*'*STARS)

selected_items = []
while True:
        print("Dostupni proizvodi:")
        for product in products:
            print(f"{product['id']}. {product['name']} - {product['price']}")
        
        try:
            product_id = int(input('Unesite ID proizvoda: '))
            if product_id == 0:
                break
        product = ''
        for product in products:
            if product["id"] == product_id:
                break

        quantity = int(input("Unesite količinu: "))
        selected_items.append({
                "product_name": product["name"],
                "quantity": quantity,
                "price": product["price"],
                "total": product["price"] * quantity
            })
        except ValueError:
            print("Neispravan unos!")

    menu_choice = input()

    match menu_choice:
        case 1:
            print(offers)
        
        case 2:


    # Izračunajte sub_total, tax i total
    # mozda dodati novu funkciju koja racuna total, tax i total
    # Dodajte novu ponudu u listu offers



# TODO: Implementirajte funkciju za upravljanje proizvodima.
def manage_products(products: Dict):
    """
    Allows the user to add a new product or modify an existing product.
    """
    while True:
        print("\nUpravljanje proizvodima:")
        print("1. Dodaj novi proizvod")
        print("2. Ažuriraj postojeći proizvod")
        print("3. Povratak na glavni izbornik")
        choice = input("Odaberite opciju: ")
        id = 0
        products = {}
        choice = input()
        match choice:
            case 1:
                name = input("Unesite naziv proizvoda: ")
                description = input("Unesite opis proizvoda: ")
                try:
                    price = float(input("Unesite cijenu proizvoda: "))
                except:
                    print("Neispravan unos cijene!")
                    continue
                
                new_product = {
                    "id": id + 1,
                    "name": name,
                    "description": description,
                    "price": price
                }
                products.append(new_product)
                print("Proizvod uspješno dodan!")
            
        
            case 2:
                print('Proizvodi:')
                for product in products:
                    print(f"{product['id']} {product['name']} {product['price']}")

            case 3:
                break
                
            

    # Omogućite korisniku izbor između dodavanja ili izmjene proizvoda
    # Za dodavanje: unesite podatke o proizvodu i dodajte ga u listu products
    # Za izmjenu: selektirajte proizvod i ažurirajte podatke
    


# TODO: Implementirajte funkciju za upravljanje kupcima.
def manage_customers(customers: Dict):
    """
    Allows the user to add a new customer or view all customers.
    """
    while True:
        print("\nUpravljanje kupcima:")
        print("1. Dodaj novog kupca")
        print("2. Prikaži sve kupce")
        print("3. Povratak na glavni izbornik")
        choice = input("Odaberite opciju: ")
        
        match choice:
            case 1:
                name = input("Unesite ime kupca: ")
                email = input("Unesite email kupca: ")
                vat_id = input("Unesite VAT ID kupca: ")
            
                new_customer = {
                        "name": name,
                        "email": email,
                        "vat_id": vat_id
                    }
                customers.append(new_customer)
                print("Kupac uspješno dodan!")
        
            case 2:
                print("Popis svih kupaca:")
                for customer in customers:
                    print(f"Ime: {customer['name']}, Email: {customer['email']}, VAT ID: {customer['vat_id']}")
            
            case 3:
                break
                
    else:
        print("Neispravan unos, pokušajte ponovo.")
    # Za dodavanje: omogući unos imena kupca, emaila i unos VAT ID-a
    # Za pregled: prikaži listu svih kupaca
    


# TODO: Implementirajte funkciju za prikaz ponuda.
def display_offers(offers):
    """
    Display all offers, offers for a selected month, or a single offer by ID.
    """
    # Omogućite izbor pregleda: sve ponude, po mjesecu ili pojedinačna ponuda
    # Prikaz relevantnih ponuda na temelju izbora
    pass


# Pomoćna funkcija za prikaz jedne ponude
def print_offer(offer):
    """Display details of a single offer."""
    print(f"Ponuda br: {offer['offer_number']}, Kupac: {offer['customer']['name']}, Datum ponude: {offer['date']}")
    print("Stavke:")
    for item in offer["items"]:
        print(f"  - {item['product_name']} (ID: {item['product_id']}): {item['description']}")
        print(f"    Kolicina: {item['quantity']}, Cijena: ${item['price']}, Ukupno: ${item['item_total']}")
    print(f"Ukupno: ${offer['sub_total']}, Porez: ${offer['tax']}, Ukupno za platiti: ${offer['total']}")


def main():
    # Učitavanje podataka iz JSON datoteka
    offers = load_data(OFFERS_FILE)
    products = load_data(PRODUCTS_FILE)
    customers = load_data(CUSTOMERS_FILE)

    while True:
        print("\nOffers Calculator izbornik:")
        print("1. Kreiraj novu ponudu")
        print("2. Upravljanje proizvodima")
        print("3. Upravljanje korisnicima")
        print("4. Prikaz ponuda")
        print("5. Izlaz")
        choice = input("Odabrana opcija: ")

        if choice == "1":
            create_new_offer(offers, products, customers)
        elif choice == "2":
            manage_products(products)
        elif choice == "3":
            manage_customers(customers)
        elif choice == "4":
            display_offers(offers)
        elif choice == "5":
            # Pohrana podataka prilikom izlaza
            save_data(OFFERS_FILE, offers)
            save_data(PRODUCTS_FILE, products)
            save_data(CUSTOMERS_FILE, customers)
            break
        else:
            print("Krivi izbor. Pokusajte ponovno.")


if __name__ == "__main__":
    main()
