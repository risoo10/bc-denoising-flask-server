import io
from PIL import Image
from flask import Flask, request, Response, abort

app = Flask(__name__)
model = None

width, height, number_of_channels = 32, 32, 3

def load_keras_model(filename=""):
    pass


def preprocess_image(image, target):
    return None

@app.route("/")
def hello():
    return "Hello, This is my perfect site!"

@app.route("/predict", methods=["POST"])
def return_hello_world():

    try:
        if request.method == "POST":
            if request.files.get("image"):

                # Read Image from bytes
                image = request.files["image"].read()
                image = Image.open(io.BytesIO(image))

                greyscale_image = image.convert("L")

                output = io.BytesIO()
                greyscale_image.save(output, format("JPEG"))

                return Response(output.getvalue(), mimetype="image/jpg")
    except IOError:
        abort(404)


# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server... please wait until server has fully started"))
    app.run()
