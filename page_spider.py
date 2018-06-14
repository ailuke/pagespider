import argparse
import os

from utilities import url_utilities, database_utilities


def main(database: str, url_list_file: str):
    big_word_list = []
    print("we are going to work with " + database)
    print("we are going to scan " + url_list_file)
    urls = url_utilities.load_urls_from_file(url_list_file)
    for url in urls:
        print("reading " + url)
        page_content = url_utilities.load_page(url=url)
        words = url_utilities.scrape_page(page_contents=page_content)
        big_word_list.extend(words)

    # database code
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    path = os.path.join(os.getcwd(), "words.db")
    database_utilities.create_database(database_path=path)
    database_utilities.save_words_to_database(database_path=path, words_list=big_word_list)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="SQLite File Name")
    parser.add_argument("-i", "--input", help="File containing urls to read")
    args = parser.parse_args()

    if not args.database:
        raise ValueError("Missing database (-db) argument")
    if not args.input:
        raise ValueError("Missing input (-i) argument")

    database_file = args.database
    input_file = args.input

    main(database=database_file, url_list_file=input_file)
