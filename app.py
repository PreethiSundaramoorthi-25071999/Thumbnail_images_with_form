from flask import Flask,render_template,request,url_for,redirect
app=Flask(__name__)
list1=[]        
@app.route('/')
def home():
     return render_template("home.html",list2=list1)

@app.route('/a',methods=["POST","GET"])
def home1():
     if request.method=="POST":
          Thumbnail=request.form.get("Thumbnail")
          Picture=request.form.get("Picture")
          Description=request.form.get("Description")
          Views=request.form.get("Views")
          Channel_Name=request.form.get("Channel_Name")
          Uploaded_Time=request.form.get("Uploaded_Time")
          dict1={}
          dict1.update({"Thumbnail":Thumbnail})
          dict1.update({"Picture":Picture})
          dict1.update({"Description":Description})
          dict1.update({"Views":Views})
          dict1.update({"Channel_Name":Channel_Name})
          dict1.update({"Uploaded_Time":Uploaded_Time})
          list1.append(dict1)
          return redirect("/")
     return render_template("form.html", list2=list1)

if __name__=="__main__":
    app.run(debug=True)