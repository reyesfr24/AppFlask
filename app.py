from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hola, Flask'

@app.route('/create-article', methods=['GET', 'POST'])
def create_article():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        return f'Artículo creado: {title}, Contenido: {content}'
    return '''
        <form method='POST' action="create-article">
            <label for='title'>Título del artículo:</label><br>
            <input type='text' id='title' name='title'><br><br>
            <label for='content'>Contenido del artículo:</label><br>
            <textarea name='content' id='content'></textarea><br><br>
            <input type='submit' id='title' value='Crear Articulo'>

'''

# Crear endpoint con variable que llega a través de la url
@app.route('/article/<int:article_id>')
def view_article(article_id):
    return f'Estas viendo el articulo número {article_id}'















if __name__ == '__main__':
    app.run(debug=True)