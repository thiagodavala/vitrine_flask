from flask import Flask, render_template, request
 
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/produto')
def produto():
     produto = request.args.get('codigo')
     if produto == "1":    
         nome="Chinelo"
         descricao="Chinelo muito bom!"
         imagem="/static/chinelo.jpeg"
         return render_template('produto.html', nome=nome, descricao=descricao, imagem=imagem)
     if produto == "2":
         nome="Boné"
         descricao="Boné muito bom!"
         imagem="/static/bone.jpg"
         return render_template('produto.html', nome=nome, descricao=descricao, imagem=imagem)
   
if __name__ == '__main__':
    app.run(debug=True)