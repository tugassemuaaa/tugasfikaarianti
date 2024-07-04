from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def daftar():
    return redirect("login")

@app.route("/login", methods =["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = "fika"
        password = "1203"
        
        input_username = request.form.get("username")
        input_password= request.form.get("password")
        
        if input_username == username and input_password == password :
            return redirect(url_for("home"))
        else :
             return redirect(url_for("login"))

@app.route("/home", methods =["POST", "GET"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    elif request.method =="POST":
        return redirect(url_for("menu"))

@app.route("/menu", methods=["GET", "POST"])
def menu():
    if request.method == "GET":
        return render_template("menu.html")
    elif request.method == "POST":
        namakue = request.form.get('namakue') 
        return redirect(url_for('order', namakue=namakue))

@app.route("/order", methods=["GET", "POST"])
def order():
    if request.method == "GET":
        return render_template("order.html")
    if request.method == "POST":
        action = request.form.get("action")
        if action == "order now":
            nama = "fika"
            alamat = "kancinaa"
            kota = "buton"
            kecamatan = "pasarwajo"
            no_telepon = "082250116233"
            metode_pembayaran ="BNI"

            input_nama = request.form.get("nama")
            input_alamat = request.form.get("alamat")
            input_kota = request.form.get("kota")
            input_kecamatan = request.form.get("kecamatan")
            input_no_telepon = request.form.get("no_telepon")
            input_metode_pembayaran = request.form.get("metode_pembayaran")


            if (input_nama == nama and input_alamat == alamat and
                input_kota == kota and input_kecamatan == kecamatan and
                input_no_telepon == no_telepon and metode_pembayaran == metode_pembayaran):
                return redirect(url_for("penutup",nama=nama, 
                                alamat=alamat, 
                                kota=kota, 
                                kecamatan=kecamatan, 
                                no_telepon=no_telepon))
            else:
                return redirect(url_for("order"))
        elif action == "batal":
            return redirect(url_for("menu"))

@app.route("/penutup")
def penutup():
    nama = request.args.get("nama")
    alamat = request.args.get("alamat")
    kota = request.args.get("kota")
    kecamatan = request.args.get("kecamatan")
    no_telepon = request.args.get("no_telepon")
    metode_pembayaran = request.args.get("metode_pembayaran")


    return render_template('penutup.html',nama=nama, 
                                alamat=alamat, 
                                kota=kota, 
                                kecamatant=kecamatan, 
                                no_telepon=no_telepon,metode_pembayaran=metode_pembayaran)