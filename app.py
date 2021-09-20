import flask

app = flask.Flask(__name__)

shows = ["Avatar:The Last Airbender", "Game of Thrones", "Attack on Titan","Top Gear", "Peaky Blinders"]
images = ["/static/230px-Avatar_The_Last_Airbender_North_and_South_Part_1_cover.jpg", 
        "/static/game-of-thrones-season-4.jpg",
        "/static/attack-on-titan-8.jpg",
        "/static/top-gear-banner-580op.jpg",
        "/static/peaky-blinders.jpg"]

@app.route('/')
def index():
    return flask.render_template("index.html", len = len(shows), shows = shows, images = images)

app.run(
    debug=True
)
