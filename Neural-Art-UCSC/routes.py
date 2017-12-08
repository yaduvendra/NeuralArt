import sys
import requests
############################### Modifications #########################
import shutil
############################### End Modifications #########################
from flask import Flask, render_template, request, session, redirect, url_for
from forms import ArtForm
import urllib.request

app = Flask(__name__)
app.secret_key = "development-key"

@app.route("/", methods=['GET','POST'])
def index():
  form = ArtForm()
  if form.is_submitted():

      ############################### Modifications #########################
      if form.urlName.data and form.urlLink.data:
          urlName = "./images/" + form.urlName.data + ".jpg"
          urlLink = form.urlLink.data


          response = requests.get(urlLink, stream=True)
          with open(urlName, "wb+") as out_file:
              shutil.copyfileobj(response.raw, out_file)
          del response
          imageName = form.urlName.data + ".jpg"
          ckpoint = request.form['style']
          endpoint = form.endpoint.data
          print("image: " + urlName + " ckpoint: " + ckpoint + " endpoint: " + endpoint, file=sys.stderr)
          make_request(urlName, imageName, ckpoint, endpoint)
          session['ImageName'] = "static/imgs/" + ckpoint + imageName;
          ImageName = session.get('ImageName', None)
          return render_template("index.html",form=form, valueImage = ImageName, scroll = 'result1')

      ############################### End Modifications #########################

  return render_template("index.html", form=form)


def make_request(image, imgName, ckpoint, endpoint):
    files = {
        'file': (image, open(image, 'rb')),

    }
    payload = {'checkpoint': ckpoint}
    r = requests.post(endpoint, data = payload, files = files)

    #Open file, names it, write image to file, closes it, stores in output folders.
    fileImage = open("static/imgs/" + ckpoint + imgName,"wb+")
    fileImage.write(r.content)
    fileImage.close()
    return

if __name__ == '__main__':
    app.run(host='0.0.0.0')
