import flask
import datetime

DEBUG = False
SECRET_KEY = '89d164a62543df6a53b5ee157c18515c'

app = flask.Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('PARTY_SETTINGS', silent=True)

@app.route('/')
def home():
    now = datetime.datetime.now()
    stuff = {'leet': 0}
    varnames = ['h_10', 'h_1', 'm_10', 'm_1']

    for cur, leet, var in  zip(now.strftime('%H%M'), '1337', varnames):
        stuff[var] = cur

        if cur == leet:
            stuff['leet'] += 25
            stuff[var+'_party'] = 'party'
        else:
            stuff[var+'_party'] = 'noparty'

    stuff['full_leet'] = 'full_leet' if stuff['leet'] == 100 else 'partial_leet'

    return flask.render_template('home.html', **stuff)

if __name__ == '__main__':
    app.run()
