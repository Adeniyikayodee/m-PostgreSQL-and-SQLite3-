import pyscopg2

def create_table():
    conn=pyscopg2.connect("dbname='database' user='..' password='..' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=pyscopg2.connect("dbname='database' user='..' password='..' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item,quanity,price))
    conn.commit()
    conn.close()

def view():
    conn=pyscopg2.connect("dbname='database' user='..' password='..' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=pyscopg2.connect("dbname='database' user='..' password='..' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn=pyscopg2.connect("dbname='database' user='..' password='..' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s item WHERE item=%s",(quanity,price,item))
    conn.commit()
    conn.close()

#delete()
#view()
#update()
#inser()
#create_table()
#print(view())




