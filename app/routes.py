import os
import app.classifier as appclassifier
import app.nearest as nearest
import app.randomfacts as randomfacts
from app import app
from flask import render_template, request, redirect

@app.route('/')
def template_test():
    return render_template('index.html', name="Luigi")


@app.route('/punto-verde')
def template_greenpoint():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if lat is None or lon is None:
        return render_template('greenpoint-redirect.html');
    else:
        src = nearest.getNearest(float(lat), float(lon))
        return render_template('greenpoint.html', embed_url=src);


@app.route('/a-donde-va', methods = ['GET', 'POST'])
def template_classifier_img():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            image.save(os.path.join(os.path.abspath("static/tmp/"), image.filename))
        return redirect("/va-aqui?src=" + image.filename)
    ff = randomfacts.randomfact()
    return render_template('classifier-img.html', fun_fact=ff);
        #return render_template('classifier.html', page_text="Hola");

@app.route('/va-aqui')
def template_classifier():
    src = request.args.get('src')
    res = appclassifier.get_result(src)
    os.remove(os.path.abspath('static/tmp/'+src))
    if res == "unknown" or res == "negro":
        return render_template('classifier_mal.html')
    else:
        return render_template('classifier.html', contenedor=res);

@app.route('/report', methods = ['GET', 'POST'])
def template_report():
    if request.files:
        action = request.files["action"]
        return redirect("reporte?action=" + action)
    success = request.args.get('success')
    print(success)
    if success is None:
        return render_template('report.html');

@app.route('/reporte')
def template_reporte():
    action = request.args.get('action')
    # Update points
    if action == "1":
        appupdate.update_user_score(1,3)
    elif action == "2":
        appupdate.update_container(1,1)
    return render_template('report.html')
