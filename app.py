from flask import Flask, render_template, send_from_directory, Response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    with open('static/sitemap.xml') as f:
        sitemap_content = f.read()
    return Response(sitemap_content, mimetype='application/xml')

if __name__ == '__main__':
    app.run(debug=True)
