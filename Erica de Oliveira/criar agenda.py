
conn.comit()
conn.close()


def inserir_contato():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    apelido = entry_apelido.get()

    if nome and telefone and email and apelido:
        conn = sqlite3.connect("agenda_contatos.db")
        cursor = conn.cursor()