from flask import request, jsonify
from data.usuarios import usuarios, adicionar_usuario


def cadastrar_usuario():
    dados = request.get_json()

    if not dados:
        return jsonify({
            "error": "O corpo da requisição deve conter dados em formato JSON."
        }), 400

    if "nome" not in dados or not isinstance(dados["nome"], str) or not dados["nome"].strip():
        return jsonify({
            "error": "O campo 'nome' é obrigatório."
        }), 400

    if "email" not in dados or not isinstance(dados["email"], str) or not dados["email"].strip():
        return jsonify({
            "error": "O campo 'email' é obrigatório."
        }), 400

    usuario = adicionar_usuario(
        dados["nome"].strip(),
        dados["email"].strip()
    )

    return jsonify({
        "data": usuario
    }), 201


def listar_usuarios():
    return jsonify({
        "data": usuarios
    }), 200


def buscar_usuario(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            return jsonify({
                "data": usuario
            }), 200

    return jsonify({
        "error": "Usuário não encontrado"
    }), 404


def atualizar_usuario(id):
    dados = request.get_json()

    if not dados:
        return jsonify({
            "error": "O corpo da requisição deve conter dados em formato JSON."
        }), 400

    for usuario in usuarios:
        if usuario["id"] == id:

            if "nome" in dados:
                if not isinstance(dados["nome"], str) or not dados["nome"].strip():
                    return jsonify({
                        "error": "O campo 'nome' não pode ser vazio."
                    }), 400

                usuario["nome"] = dados["nome"].strip()

            if "email" in dados:
                if not isinstance(dados["email"], str) or not dados["email"].strip():
                    return jsonify({
                        "error": "O campo 'email' não pode ser vazio."
                    }), 400

                usuario["email"] = dados["email"].strip()

            return jsonify({
                "data": usuario
            }), 200

    return jsonify({
        "error": "Usuário não encontrado"
    }), 404


def remover_usuario(id):
    for indice, usuario in enumerate(usuarios):
        if usuario["id"] == id:
            usuarios.pop(indice)

            return "", 204

    return jsonify({
        "error": "Usuário não encontrado"
    }), 404