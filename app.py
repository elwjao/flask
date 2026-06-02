from flask import Flask, render_template, request
# cria a aplicação flask
app = Flask(__name__)

@app.route('/')
def Exibir_formulario():

    return render_template(
        'index.html',
        mensagem ='Formulario.html',
        resultado = ' Aguardando o envio...')
def Processar_formulario():

    nome = request.form['nome']
    idade = request.form['idade']
    curso = request.form['curso']

    if not nome or not idade or not curso:
        mensagem_resultado = "Erro: todos os campos sao obrigatorio"
        return mensagem_resultado

    else:
     idade_int = int(idade)
     mensagem_base = f"ola {nome}, voce tem {idade_int} anos e esta no curso de {curso}"

    if  idade_int < 18:
        mensagem_resultado = "Você é menor de idade"

    elif idade_int > 18 and idade_int < 60:
        mensagem_idade = "Você é adulto"

    else:
         mensagem_idade =  "Voce é experiente. "

    if curso == "python":
        mensagem_curso =  "otima escolha, você é versatil"
