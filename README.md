# Flask QR Code Generator

This Flask application allows users to generate QR codes from URLs they provide. The generated QR code can then be downloaded or scanned to access the linked webpage.

### Features:

* User-friendly interface for entering URLs
* QR code generation based on user input
* Display of the generated QR code on a separate page

### Prerequisites:

- Python 3.x 
- Flask 
- qrcode library (pip install qrcode)


### Clone the Repository:

git clone https://github.com/your-username/flask_qr_code_generator.git

### Install Dependencies:

- cd flask_qr_code_generator
- pip install -r requirements.txt

### Run the Application:

- python app.py

This will start the Flask development server. Access the application at http://127.0.0.1:5000/ in your web browser.

### Usage:

Visit http://127.0.0.1:5000/ in your browser.
Enter the URL you want to convert into a QR code in the provided text box.
Click the "Generate QR Code" button.

You will be redirected to a new page displaying the generated QR code.

### Customization:

The code can be further customized by modifying the HTML templates (index.html and qr_code.html) to adjust the visual appearance.
You can also explore options within the qrcode library for more control over QR code generation parameters.

### Contributing:

We welcome contributions to improve this project. Please feel free to fork the repository and submit pull requests with your modifications.