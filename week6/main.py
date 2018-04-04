import bottle

app = bottle.Bottle()

@app.route('/')
def index():

    consent = bottle.request.get_cookie('consent')
    print(consent)
    if not consent:
        return bottle.template('main.html',n=0,consent="unknown")
    else:
        visits = bottle.request.get_cookie('visited')
        if visits:
            visits = int(visits)+1
            bottle.response.set_cookie('visited',str(visits))
            return bottle.template('main.html',n=visits,consent="yes")
        else:
            bottle.response.set_cookie('visited',str(1))
            return bottle.template('main.html',n=0,consent="yes")

@app.route('/', method="POST")
def form():
    if bottle.request.forms.get('consent') == "yes":
        bottle.response.set_cookie('consent','yes')
    bottle.redirect('/')
    return


if __name__ == "__main__":
    app.run()