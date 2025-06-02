from flask import Flask, render_template, url_for, request, redirect, flash

app = Flask(__name__)
app.secret_key = "una_clave_segura"

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/software")
def software():
    return render_template("paginas/software.html")

@app.route("/redes")
def redes():
    return render_template("paginas/redes.html")

@app.route("/soporte")
def soporte():
    return render_template("paginas/soporte.html")

@app.route("/contacto", methods=["POST"])
def contacto():
    email = request.form.get("email")
    mensaje = request.form.get("mensaje")

    if not email or not mensaje:
        flash("Por favor, completa todos los campos.", "danger")
        return redirect(url_for("inicio"))

    print(f"Mensaje recibido de {email}: {mensaje}")
    flash("Mensaje enviado correctamente.", "success")
    return redirect(url_for("inicio"))

if __name__ == '__main__':
    app.run(debug=True)
