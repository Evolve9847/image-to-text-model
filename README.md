# Image-to-Text AI Prompt Generator

This is a Flask-based web application that allows users to upload an image and generate an AI-generated description using OpenAI's `gpt-4o-mini` model.

## Features
- Upload an image via a web interface
- Convert the image to base64 format for processing
- Generate a detailed text description of the image using OpenAI's GPT-4o-mini
- Display the uploaded image along with the generated AI prompt

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.7+
- Pip
- A valid OpenAI API key

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/image-to-text-ai.git
   cd image-to-text-ai
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add your OpenAI API key:
   ```sh
   OPENAI_API_KEY=your_api_key_here
   ```

5. Run the Flask app:
   ```sh
   python app.py
   ```

6. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Usage
- Upload an image via the web interface.
- The AI model will analyze the image and generate a text description.
- The result will be displayed on the webpage.

## File Structure
```
image-to-text-ai/
│── static/
│   ├── uploads/        # Stores uploaded images
│── templates/
│   ├── index.html      # HTML template for UI
│── app.py              # Main Flask application
│── .env                # API key storage (not included in repo)
│── requirements.txt    # Dependencies
│── README.md           # Project documentation
```

## Contributing
Feel free to submit issues or pull requests for improvements.

## License
This project is licensed under the MIT License.

