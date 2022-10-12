import youtube_dl
from flask import Flask, render_template, redirect, request

ulink = ""

app = Flask(__name__)


# To show Home page!
@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template("index.html")


# To show Terms and Conditions!
@app.route("/terms-conditions")
def terms():
    return render_template("terms-conditions.html")


# To show privacy policies!
@app.route("/privacy-policy")
def privacy():
    return render_template("privacy-policy.html")


# To show availbale formats!
@app.route("/formats", methods=["GET","POST"])
def formats():
    uLink = request.form['url']
    with youtube_dl.YoutubeDL() as ydl:
        url = ydl.extract_info(uLink, download=False)
        vidFormats = url["formats"]
    return render_template("formats.html", vFormats=vidFormats, iFr=url, tLink=uLink)


# To download videos!
@app.route("/download", methods=["GET", "POST"])
def download():
    dnLink = request.form['fUrl']
    formatsID = int(request.form["fId"])
    with youtube_dl.YoutubeDL() as ydl:
        url = ydl.extract_info(dnLink, download=False)
        downloadLink = (url["formats"][formatsID]["url"])
        
    return redirect(downloadLink+"&dl=1")
    # return render_template("download.html", vals=formatsID)


# # To download the best available video!
# @app.route("/downloadBest", methods=["GET", "POST"])
# def downloadBest():
#     dnLink = request.form['fUrl']
#     formatsID = int(request.form["fId"])
#     with youtube_dl.YoutubeDL() as ydl:
#         url = ydl.extract_info(dnLink, download=False)
#         downloadLink = (url["formats"][-1]["url"])
        
#     return redirect(downloadLink+"&dl=1")
#     # return render_template("download.html", vals=formatsID)


if __name__ == "__main__":
    app.run(debug=True)