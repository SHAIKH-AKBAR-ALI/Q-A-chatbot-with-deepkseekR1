🤖 Advanced AI Chat Assistant
A modern, interactive AI-powered chat assistant built with Streamlit, Python, LangChain, and Ollama. This application provides a feature-rich conversational interface with customizable models, role-based prompts, and an intuitive UI.

📌 Overview
The Advanced AI Chat Assistant is designed to provide a seamless and engaging conversational experience. It leverages the power of LangChain and Ollama to integrate advanced language models like DeepSeek, LLaMA, and Mistral. Users"Can interact with the assistant in various roles (e.g., Assistant, Creative Writer, Code Helper, Teacher) and customize settings like temperature and max tokens through a sleek sidebar interface.
The app features a visually appealing, animated chat UI, stores conversation history in session state, and allows exporting chats as JSON. It also includes chat statistics and quick action prompts for enhanced usability.

✨ Features

Multiple AI Models: Choose from DeepSeek, LLaMA, or Mistral for varied conversational capabilities.
Role-Based Prompts: Switch between roles like Assistant, Creative Writer, Code Helper, or Teacher to tailor responses.
Animated Chat UI: A modern, responsive interface with custom CSS for a polished user experience.
Chat History: Persist conversation history using Streamlit's session state.
Quick Action Prompts: Predefined prompts for common tasks to streamline interaction.
Export Chat History: Save conversations as JSON files for easy sharing or backup.
Chat Statistics: View insights like total messages and user-specific message counts.
Advanced Configuration: Adjust model parameters (temperature, max tokens) via a sidebar.


⚡ Installation & Usage
Follow these steps to set up and run the Advanced AI Chat Assistant locally:
Prerequisites

Python 3.8+
Ollama installed and running locally (with desired models like DeepSeek, LLaMA, or Mistral)
Git

Steps

Clone the Repository:
git clone https://github.com/your-username/advanced-ai-chat-assistant.git
cd advanced-ai-chat-assistant


Install Dependencies:
pip install -r requirements.txt


Run the Application:
streamlit run app.py


Open your browser and navigate to http://localhost:8501 to interact with the app.


Requirements
The requirements.txt includes:

streamlit
langchain
ollama
Other dependencies for UI and functionality


📸 Screenshots
Placeholder for screenshots. Add images of the chat interface, sidebar, and exported JSON output here.

<img width="2542" height="1046" alt="image" src="https://github.com/user-attachments/assets/ca390e5e-bee4-407f-9696-5266cd625a8e" />


<img width="2519" height="1180" alt="image" src="https://github.com/user-attachments/assets/d447a471-d3bf-4217-85ee-75052770c537" />


🛠️ Tech Stack

Frontend: Streamlit (Python-based web framework)
Backend: Python, LangChain, Ollama
AI Models: DeepSeek, LLaMA, Mistral
Styling: Custom CSS for animated UI
Storage: Streamlit session state for chat history
Export Format: JSON


🚀 Roadmap / Future Improvements

Add support for additional AI models and providers.
Implement real-time collaboration for multi-user chats.
Enhance UI with theme customization (light/dark mode).
Add voice input/output capabilities.
Integrate cloud-based model hosting for scalability.
Improve chat statistics with visualizations (e.g., message frequency charts).

Contributions and suggestions for new features are welcome! See the Contributing section below.

🤝 Contributing
We welcome contributions to make the Advanced AI Chat Assistant even better! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature-name).
Commit your changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature-name).
Open a Pull Request with a detailed description of your changes.

Please ensure your code follows the project's coding style and includes appropriate tests.

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

Built with ❤️ by [SHAIKH AKBAR ALI]
