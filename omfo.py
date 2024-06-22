from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            df = pd.read_csv(file)
            fig = px.scatter(df, x='x_column', y='y_column', color='category_column')
            graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            return render_template('index.html', graphJSON=graphJSON)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
