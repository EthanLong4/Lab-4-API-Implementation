import requests

BASE_URL = "https://dune-api-a4iq.onrender.com"

def get_data(path):
        # had to raise timeout time because the API is hosted on a free service and responses slow if not used for a while??
    try:
        response = requests.get(BASE_URL + path, timeout=60)
        response.raise_for_status()
        data = response.json()
        if isinstance(data, dict):
            data = [data]
        return data
    except requests.RequestException as error:
        print(f"Something went wrong: {error}")
        return None


#prints a list of quotes
def show_quotes(quotes):
    for q in quotes:
        print(f'[{q["id"]}] "{q["quote"]}"')


#prints a list of books
def show_books(books):
    for b in books:
        author = b["author"]
        if isinstance(author, list):
            author = ", ".join(author)
        print(f'[{b["id"]}] {b["title"]} ({b["year"]}) by {author}')





last_quote = None


#User menu and main loop
print("Welcome to Using The Dune API!")

while True:
    print("\n1. Random quote")
    print("2. Several quotes")
    print("3. Quote by ID")
    print("4. Random book")
    print("5. Several books")
    print("6. Book by ID")
    print("7. Save last quote")
    print("8. Quit")
    choice = input("Choose an option: ").strip()




    if choice == "1":
        quotes = get_data("/quotes")
        if quotes:
            last_quote = quotes[0]
            show_quotes(quotes)

    elif choice == "2":
        number = input("How many quotes? ").strip()
        if number.isdigit():
            quotes = get_data("/quotes/" + number)
            if quotes:
                last_quote = quotes[-1]
                show_quotes(quotes)
        else:
            print("Please enter a whole number.")

    elif choice == "3":
        quote_id = input("Quote ID: ").strip()
        if quote_id.isdigit():
            quotes = get_data("/quotes/id/" + quote_id)
            if quotes:
                last_quote = quotes[0]
                show_quotes(quotes)
        else:
            print("Please enter a whole number.")

    elif choice == "4":
        books = get_data("/books")
        if books:
            show_books(books)

    elif choice == "5":
        number = input("How many books? ").strip()
        if number.isdigit():
            books = get_data("/books/" + number)
            if books:
                show_books(books)
        else:
            print("Please enter a whole number.")

    elif choice == "6":
        book_id = input("Book ID: ").strip()
        if book_id.isdigit():
            books = get_data("/books/id/" + book_id)
            if books:
                show_books(books)
        else:
            print("Please enter a whole number.")


    elif choice == "7":
        if last_quote is None:
            print("No quote to save yet. Get one first.")
        else:
            with open("favorites.txt", "a", encoding="utf-8") as file:
                file.write(f'{last_quote["id"]}: "{last_quote["quote"]}"\n')
            print("Saved to favorites.txt.")

    elif choice == "8":
        print("Goodbye!")
        break


    else:
        print("Please choose a number from 1 to 8.")