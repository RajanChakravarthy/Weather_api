from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv('data_small/stations.txt', skiprows=17)
stations = stations[['STAID','STANAME                                 ']]

@app.route("/")
def home():
    # .to_html() produces raw html. safe keyword in home.html renders the data in tabular format
    return render_template('home.html', data=stations.to_html())

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = 'TG_STAID' + str(station).zfill(6) + '.txt'
    df = pd.read_csv(f'data_small/{filename}', skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() /10
    return {'station': station,
            'date': date,
            'temperature': (temperature)}

if __name__ == '__main__':
    app.run(debug=True)
