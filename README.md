This is DermaScan AI, a virtual dermatology assistant developed to analyze user-inputted skin symptoms and provide instant, intelligent feedback on possible skin conditions.

The project combines a Flask-based Python backend with a sleek, chatbot-style frontend built using HTML, CSS, and JavaScript.

At its core, DermaScan AI functions by accepting free-text symptom input from the user. The frontend sends this data to a backend API endpoint (/analyze), where the system processes it using a predefined set of keywords associated with common skin conditions. Alternatively, it can be enhanced with AI models such as Gemini for smarter interpretation.

The backend then returns a structured JSON response, including the potential skin condition, a brief description, and helpful recommendations for care or follow-up. These responses are dynamically rendered in the chat interface, simulating the experience of interacting with a virtual medical assistant.

Designed with simplicity and accessibility in mind, the system is easy to deploy. Users need only configure a .env file, install dependencies, and run the Python app locally.

DermaScan AI also presents opportunities for future development, such as integrating real-time machine learning models, supporting image-based diagnoses, enabling multilingual capabilities, and connecting to dermatological databases or APIs.

This project stands as a promising demonstration of how AI and software engineering can support preliminary healthcare assistance—especially in regions with limited access to specialists.

It is open-source and available for contributions. Feedback, suggestions, and stars are welcome on GitHub.

