class Book:
    def __init__(self, author: str, title: str, pages: int) -> None:
        self.author = author 
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

    
def main():
    my_str = "hello"
    print(len(my_str))
    my_list = [1, 2, 3, 4, 5]
    print(len(my_list))
    my_book = Book('Robert', 'ClenCode', 347)
    print(len(my_book))


if __name__ == '__main__':
    main()