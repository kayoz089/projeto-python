import sqlite3

def adicionar(nome, idade, email):
    conn = sqlite3.connect("logins.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO logins (nome, idade, email) VALUES (?, ?, ?)", (nome, idade, email, ))

    conn.commit()
    conn.close()

    print("login completo! ")


def deletar(nome):
    conn = sqlite3.connect("logins.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM logins WHERE nome = ?", (nome, ))

    conn.commit()
    conn.close()

    print(f"O login da pessoa {nome} foi deletado da database!")   


def info():
    conn = sqlite3.connect("logins.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM logins")
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(cliente)

    conn.commit()
    conn.close()


def exportar_txt():
    conn = sqlite3.connect("logins.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM logins")
    logins = cursor.fetchall()

    with open("exportação.txt", "w") as arquivo:
        for login in logins:
            arquivo.write(f"{login} \n")
