from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# @app.route('/verificar', methods=['GET'])
# def verifica_status():
#   try:
#     resposta = request.get('http://localhost:5000/status')

#     if resposta.status_code == 200:
#       return jsonify({'menssagem':'API está funcionando'}), 200

#     else:
#       return jsonify({'erro':'API retornou status {repos.status_code}'}), resposta.status_code

#   except request.exceptions.ResquestException as e:
#     return jsonify({'errr':'Não foi possivel conectar à API!','detalhes': str(e)}), 500#

livros = [
  {
    'id': 1,
    'titulo':'O Senhor dos Anéis = A Sociedade do Anel',
    'autor':'J.R.R Tolkien'
  },
  {
    'id': 2,
    'titulo':'Harry Poter e a Pedra Filosofal',
    'autor':'J.K Howlling'
  },
  {
    'id': 3,
    'titulo':'Habitos Atômicos',
    'autor':'James Atômicos'
  }
]

# Consultar(todos)
@app.route('/livros', methods=['GET'])
def obetr_livros():
    return jsonify(livros)

# Consultar(Id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
  for livro in livros:
    if livro.get('id') == id:
      return jsonify(livro)

# Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
          livros[indice].update(livro_alterado)
          return jsonify(livros[indice])

# Criar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
  novo_livro = request.get_json()
  livros.append(novo_livro)

  return jsonify(livros)


# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
  for indice, livro in enumerate(livros):
    if livro.get('id') == id:
      del livros[indice]

  return jsonify(livros)


if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
