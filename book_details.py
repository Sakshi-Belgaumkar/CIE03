def book_details(book_id, book_title, autor_name, year_of_pub):
    result = (
        f"Book ID : {book_id}\n"
        f"Book Name : {book_title}\n"
        f"Author Name : {autor_name}\n"
        f"Year of Publication : {year_of_pub}\n"
    )
    return result

if __name__ == "__main__":
    # sample input
    book_id = 101
    book_title = "The Alchemist"
    author_name = "Paulo Coelho"
    year_of_pub = 2016

    print(book_details(book_id, book_title, author_name, year_of_pub))
