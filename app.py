from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

# Load environment variables
load_dotenv()

# Configure Gemini - USING LATEST MODEL NAME
genai.configure(api_key=os.getenv("AIzaSyBKLKH5ewQcgnP94z9qpA-r3oBdhvfp0Ss"))

# Initialize model - USE THE CORRECT MODEL NAME
model = genai.GenerativeModel('gemini-1.5-pro-latest')  # Updated model name

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        symptoms = data.get('symptoms', '').strip()
        
        if not symptoms:
            return jsonify({"status": "error", "message": "No symptoms provided"}), 400

        # Generate response with proper formatting instructions
        response = model.generate_content(
            f"""Analyze these skin symptoms: "{symptoms}".
            Provide:
            1. Most likely condition name
            2. Brief description
            3. 3-5 recommendations
            
            Respond in this EXACT JSON format:
            {{
                "condition": "condition_name",
                "description": "...",
                "recommendations": ["...", "..."]
            }}
            Do not include any additional text or markdown symbols."""
        )
        
        # Clean and parse the response
        response_text = response.text.replace('```json', '').replace('```', '').strip()
        result = eval(response_text)  # In production, use json.loads() with proper validation
        
        return jsonify({
            "status": "success",
            "analysis": [result]
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Analysis failed: {str(e)}"
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
