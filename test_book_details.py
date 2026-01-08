from book_details import book_details

def test_book_details():
    book_id = 101
    book_title = "The Alchemist"
    author_name = "Paulo Coelho"
    year_of_pub = 2016

    expected = (
        "Book ID : 101\n"
        "Book Name : The Alchemist\n"
        "Author Name : Paulo Coelho\n"
        "Year of Publication : 2016\n"
    )

    assert book_details(book_id, book_title, author_name, year_of_pub) == expected
