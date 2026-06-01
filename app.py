from flask import Flask, render_template

# cria a aplicação flask
app = Flask(__name__)

# rota principal
@app.route('/')
def pagina_inicial():
    texto_para_html = "Esta mensagem veio do Python!"
    minha_lista = ["Maça", "Banana", "Mimosa", "Laranja"]

    return render_template(
        'index.html',
        mensagem=texto_para_html,
        minha_lista=minha_lista
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
