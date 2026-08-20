usuarios = []

proximo_id = 1


def gerar_id():
    global proximo_id

    id_atual = proximo_id
    proximo_id += 1

    return id_atual


def adicionar_usuario(nome, email):
    usuario = {
        "id": gerar_id(),
        "nome": nome,
        "email": email
    }

    usuarios.append(usuario)

    return usuario