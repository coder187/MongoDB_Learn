import os
from flask import (Flask, flash, render_template, redirect,
                    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

# create an instance of Flask and set it to the variable app
app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBANME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

# We need to setup an instance of PyMongo, 
# and add the app into that using something called a constructor method, so type:
mongo = PyMongo(app)

@app.route("/")
@app.route("/get_list")
def get_list():
    print ("db call starty")
    tasks = list(mongo.db.test.find())
       
    for t in tasks:
        print (t)
        # print the ratings array
        rats = t['rating']
        for r in rats:
            print (r)

        # print each object int method array
        meth = t['method']
        for m in meth:
            print(m)
            print('STEP:')
            print (m['step'])
            print('DESCRIPTION:')
            print (m['descr'])
            
    print ("db call end")
    # The first 'tasks' is what the template will use, and that's equal to the second 'tasks', 
    # which is our variable defined above.
    return render_template("list.html", tasks=tasks)


@app.route("/add_tolist.html", methods=['POST', 'GET'])
def add_tolist():
    print ('get')
    if request.method == "POST":
        print ('post')
        name = request.form.get("test_name")
        descr = request.form.get("test_descr")
        rating = request.form.get("test_rating")
        step = request.form.get("test_method_step")
        desc = request.form.get("test_method_desc")
        o = request.form.get("obj")
        o2 = request.form.getlist('obj')
        print (name)
        print (descr)
        print (step)
        print (desc)
        print (o[0])
        print (o[1])
        print (o2)



        for i in o2:

            print (i['step'])


    return render_template("add_tolist.html")

# set host and ip from env.py
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)