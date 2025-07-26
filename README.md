# Language Translation Tool

A modern web-based language translation application built with Flask and Python 3.13. This tool provides real-time translation services with email integration capabilities.

## 🌟 Features

- **Multi-language Translation**: Support for 100+ languages
- **Web Interface**: Clean, responsive Flask web application
- **Email Integration**: Automatically send translated text via email
- **Real-time Translation**: Instant translation results
- **Error Handling**: Graceful error management and user feedback
- **Python 3.13 Compatible**: Uses modern Python features and libraries

## 🚀 Quick Start

### Prerequisites

- Python 3.13 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd Language-Translation-Tool
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables** (for email functionality)
   ```bash
   # Create a .env file or set environment variables
   export EMAIL_USER="your-email@gmail.com"
   export EMAIL_PASS="your-app-password"
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your browser and navigate to: `http://127.0.0.1:5000`

## 📋 Usage

1. **Enter Text**: Type or paste the text you want to translate
2. **Select Source Language**: Choose the language of your input text (or use Auto Detect)
3. **Select Target Language**: Choose the language you want to translate to
4. **Translate**: Click the "Translate" button
5. **View Results**: The translated text will appear below
6. **Email**: The translated text is automatically sent to the configured email address

## 🛠️ Technology Stack

- **Backend**: Flask (Python web framework)
- **Translation**: mintrans (Google Translate API wrapper)
- **Text-to-Speech**: gTTS (Google Text-to-Speech)
- **Email**: smtplib (Python email library)
- **Frontend**: HTML, CSS, JavaScript

## 📁 Project Structure

```
Language Translation Tool/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── static/            # Static files (CSS, JS, images)
│   └── static.py      # Static file handling
└── templates/         # HTML templates
    └── index.html     # Main web interface
```

## 🔧 Configuration

### Email Setup

To enable email functionality, you need to:

1. **Gmail Setup**:
   - Enable 2-factor authentication on your Gmail account
   - Generate an App Password
   - Use the App Password instead of your regular password

2. **Environment Variables**:
   ```bash
   EMAIL_USER=your-email@gmail.com
   EMAIL_PASS=your-app-password
   ```

### Supported Languages

The application supports 100+ languages including:
- English (en)
- Spanish (es)
- French (fr)
- German (de)
- Italian (it)
- Portuguese (pt)
- Russian (ru)
- Chinese (zh)
- Japanese (ja)
- Korean (ko)
- Hindi (hi)
- Arabic (ar)
- And many more...

## 🐛 Troubleshooting

### Common Issues

1. **Translation not working**:
   - Check your internet connection
   - Verify the language codes are correct
   - Ensure the mintrans library is properly installed

2. **Email not sending**:
   - Verify your email credentials
   - Check if 2-factor authentication is enabled
   - Ensure you're using an App Password, not your regular password

3. **App not starting**:
   - Check if all dependencies are installed
   - Verify Python version (3.13+)
   - Check for port conflicts (default: 5000)

## 📝 Dependencies

- `Flask`: Web framework
- `mintrans`: Translation library
- `gTTS`: Text-to-speech functionality
- `requests`: HTTP library for API calls

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [mintrans](https://github.com/DedInc/mintrans) for translation services
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Google Translate](https://translate.google.com/) for translation API

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the troubleshooting section above
2. Search existing issues in the repository
3. Create a new issue with detailed information

---

**Made with ❤️ using Python and Flask** 