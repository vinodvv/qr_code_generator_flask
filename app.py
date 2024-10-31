from flask import Flask, request, render_template, redirect, url_for
import qrcode

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']

        qr = qrcode.main.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=20,
            border=1,
        )

        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save("static/qr_code.png")
        return redirect(url_for('display_qr'))
    return render_template('index.html')


@app.route('/display_qr')
def display_qr():
    return render_template('qr_code.html')


if __name__ == "__main__":
    app.run(debug=True)
