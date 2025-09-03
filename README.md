## Athena Misinformation Verifier

A comprehensive tool for verifying claims and detecting misinformation using AI and fact-checking techniques.

## Features

- **AI-Powered Fact Checking**: Utilizes advanced NLP models to analyze and verify claims
- **Source Verification**: Cross-references information with trusted sources
- **Real-time Analysis**: Provides quick assessment of claims
- **User-friendly Interface**: Intuitive web and mobile interfaces
- **API Access**: Easy integration with other systems
- **Extensible Architecture**: Modular design for adding new verification methods

## Installation

### Prerequisites
- Python 3.9+
- Node.js 18+ (for frontend)
- pip (Python package manager)
- npm or yarn (Node package manager)

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/24f2007780/Athena-MisinfoVerifier.git
   cd Athena-MisinfoVerifier
   ```

2. Create and activate a virtual environment:
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Update the values with your API keys and configuration

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

## Running the Application

### Development Mode

1. Start the backend server (from project root):
   ```bash
   python main.py
   ```

2. In a separate terminal, start the frontend development server:
   ```bash
   cd frontend
   npm start
   # or
   yarn start
   ```

3. Open [http://localhost:19006](http://localhost:19006) in your browser

### Production Mode

1. Build the frontend:
   ```bash
   cd frontend
   npm run build
   # or
   yarn build
   ```

2. Start the production server:
   ```bash
   python main.py
   ```

## API Documentation

Once the application is running, you can access:
- Interactive API documentation: [http://localhost:8000/docs](http://localhost:8000/docs)
- Alternative documentation: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Contributing

Contributions are welcome! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with FastAPI and React Native/Expo
- Uses Google's Gemini AI for claim verification
- Inspired by the need for reliable fact-checking tools
