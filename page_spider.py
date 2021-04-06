import os
import argparse


def spider_main(database_url: str, file: str):
    print("Work with a database "+database_url)
    print("Scan file for urls "+file)


if __name__ == "__main__":

    argparse_object = argparse.ArgumentParser(description="Parse file with urls and database path")
    argparse_object.add_argument("-d", "--database", help="SQLite File Name ", type=str)
    argparse_object.add_argument("-f", "--file", help="File Containing urls ro read", type=str)
    args = argparse_object.parse_args()
    database_file = args.database
    url_file = args.file
    if database_file and url_file:
        spider_main(database_file, url_file)
    else:
        print("Please provide a file with urls and SQLite database file")
