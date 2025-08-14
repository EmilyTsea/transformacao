#https://www.youtube.com/watch?v=K2ejI4z8Mbg
from flask import Flask, render_template

app = Flask(__name__) # cria o site, mas está vazio

# Criar a 1ª página do site
#route -> qual link vai fica aquela página, caminho depois do domínio https://tseaenergiatransformacao.aevoinnovate.net/#/dashboard/ideias
#função-> o que você quer exibir naquela página
#template
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html") # parte visual - html css

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario = nome_usuario)

# Colocar o site no ar

if __name__ == "__main__": # vou executar esse arquivo quando tiver rodando ele diretamente
    app.run(debug=True, port=8080) # coloca o site no ar
# servidor do heroku

# debug=True -> vai exibir todas as mudanças que eu fizer no site