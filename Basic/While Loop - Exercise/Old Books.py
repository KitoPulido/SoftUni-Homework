book_needed = input()
book = input()
num = 0
while book_needed != book:
    book = input()
    num += 1
    if book == 'No More Books':
        print(f'The book you search is not here!')
        print(f'You checked {num} books.')
        break

if book_needed == book:
    print(f'You checked {num} books and found it.')
