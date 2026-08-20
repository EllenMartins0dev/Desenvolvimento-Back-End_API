from flask import Blueprint

from controllers.usuarios_controller import (
    cadastrar_usuario,
    listar_usuarios,
    buscar_usuario,
    atualizar_usuario,
    remover_usuario
)


usuarios_routes = Blueprint("usuarios", __name__)


@usuarios_routes.route("/usuarios", methods=["POST"])
def criar_usuario():
    return cadastrar_usuario()


@usuarios_routes.route("/usuarios", methods=["GET"])
def obter_usuarios():
    return listar_usuarios()


@usuarios_routes.route("/usuarios/<int:id>", methods=["GET"])
def obter_usuario(id):
    return buscar_usuario(id)


@usuarios_routes.route("/usuarios/<int:id>", methods=["PUT"])
def editar_usuario(id):
    return atualizar_usuario(id)


@usuarios_routes.route("/usuarios/<int:id>", methods=["DELETE"])
def excluir_usuario(id):
    return remover_usuario(id)