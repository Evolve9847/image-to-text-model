import os
import base64
from openai import OpenAI
from dotenv import load_dotenv
from flask import Flask, request, render_template

# ✅ Load API Key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# ✅ Function to Generate AI Prompt using GPT-4o-mini with Image
def generate_prompt(image_path):
    try:
        # Convert image to base64
        with open(image_path, "rb") as image_file:
            image_base64 = base64.b64encode(image_file.read()).decode("utf-8")

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an AI that analyzes images and provides detailed descriptions."},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Describe this image in detail."},
                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_base64}"}}
                    ],
                },
            ],
            max_tokens=200
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error generating prompt: {str(e)}"

# ✅ Flask Route for Image Upload & Processing
@app.route("/", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if "image" not in request.files:
            return "No file uploaded", 400

        file = request.files["image"]
        if file.filename == "":
            return "No selected file", 400

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        ai_prompt = generate_prompt(filepath)

        return render_template("index.html", ai_prompt=ai_prompt, image_url=filepath)

    return render_template("index.html", ai_prompt=None, image_url=None)

# ✅ Run Flask App
if __name__ == "__main__":
    app.run(debug=True)
