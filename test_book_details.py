from book_details import book_details

def test_book_details():
    book_id = 101
    book_title = "Ikigai"
    author_name = "XYZ"
    year_of_pub = 2019

    expected = (
        "Book ID : 102\n"
        "Book Name : Ikigai\n"
        "Author Name : XYZ\n"
        "Year of Publication : 2019\n"
    )

    assert book_details(book_id, book_title, author_name, year_of_pub) == expected
