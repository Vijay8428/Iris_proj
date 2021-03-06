from flask import Flask ,render_template,request
import iris as m

app=Flask(__name__)

pred = 0
@app.route("/",methods=['GET','POST'])
def hello():
        if request.method == 'POST':
            global pred
            sepal_l=request.form['sepal_length']
            sepal_w=request.form['sepal_width']
            petal_l=request.form['petal_length']
            petal_w=request.form['petal_width']
            pred= m.flower_prediction(sepal_l, sepal_w, petal_l, petal_w)

        return render_template("index.html",pred1=pred)

if __name__ == "__main__":
    app.run(debug=True)