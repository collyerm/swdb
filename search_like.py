import sqlite3

def query_search_like(search_string):
    connie = sqlite3.connect('sw.db')
    c = connie.cursor()
    search_term = search_string + '%'
    c.execute("SELECT charID, name FROM characters WHERE name LIKE ?", (search_term,))
    list = c.fetchall()
    return (list)

char_list = query_search_like('Lu')

for char in char_list:
    print(char)
