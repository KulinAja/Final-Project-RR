# 💪 Personalized Fitness & Nutrition App

A comprehensive web application built with Streamlit that provides personalized fitness and nutrition recommendations based on user profiles, health data, and lifestyle preferences.

## 🌟 Features

### Core Functionality
- **Personal Health Assessment**: Calculate BMI and health status based on height, weight, and age
- **Customized Recommendations**: Get tailored fitness and nutrition advice based on your goals
- **AI-Powered Insights**: Advanced recommendations using OpenRouter AI integration
- **Multi-language Support**: Interface in Indonesian language

### Data Collection
- **Basic Information**: Gender, weight, height, age
- **Fitness Profile**: Exercise type, frequency, duration preferences
- **Health Considerations**: Food allergies, medical history, dietary preferences
- **Personal Goals**: Weight loss, muscle gain, general health maintenance

### Recommendation System
- **Rule-based Recommendations**: Immediate suggestions based on BMI and goals
- **AI-Enhanced Advice**: Detailed, personalized recommendations using machine learning
- **Safety Warnings**: Alerts for users with allergies or medical conditions

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- Streamlit
- OpenRouter API key (optional, for AI recommendations)

### Installation

1. **Clone or download the application files**
   ```bash
   # Save the Final-Project.py file to your local directory
   ```

2. **Install required dependencies**
   ```bash
   pip install streamlit requests python-dotenv
   ```

3. **Set up environment variables (optional)**
   
   For AI recommendations, you'll need an OpenRouter API key:
   
   **Option 1: Using .env file**
   ```bash
   # Create .env file in the same directory
   echo "OPENROUTER_API_KEY=your_api_key_here" > .env
   ```
   
   **Option 2: Using Streamlit secrets**
   ```toml
   # Create .streamlit/secrets.toml file
   OPENROUTER_API_KEY = "your_api_key_here"
   ```

### Running the Application

```bash
streamlit run Final-Project.py
```

The application will open in your default web browser at `http://localhost:8501`

## 📖 How to Use

### Step 1: Basic Information
- Select your gender
- Enter your weight (kg) and height (cm)
- Specify your age

### Step 2: Fitness Profile
- Choose your preferred exercise type:
  - Home Exercise
  - Running
  - Lifting Weights
- Select exercise frequency (from very rare to very routine)
- Set typical workout duration

### Step 3: Health & Preferences
- Specify any food allergies
- Choose your primary fitness goal
- Select dietary preference (Omnivore/Vegetarian/Vegan)
- Add any relevant medical history
- Optionally provide email for recommendations

### Step 4: Get Recommendations
Click "Dapatkan Rekomendasi 🚀" to receive:
- BMI calculation and health status
- Basic rule-based fitness recommendations
- Personalized nutrition advice
- AI-powered detailed suggestions (if API key configured)
- Safety warnings based on health conditions

## 🔧 Configuration

### API Setup
The app supports OpenRouter AI integration for enhanced recommendations:

1. Sign up at [OpenRouter](https://openrouter.ai/)
2. Get your API key
3. Add it to your environment using one of the methods above

### Customization
You can modify the following aspects:
- Age, weight, and height ranges in the input fields
- Exercise types and frequency options
- Recommendation logic in the rule-based system
- AI prompt for different recommendation styles

## 📋 Technical Details

### Dependencies
- `streamlit`: Web app framework
- `requests`: HTTP requests for AI API
- `python-dotenv`: Environment variable management
- `typing`: Type hints support

### File Structure
```
├── Final-Project.py          # Main application file
├── .env                      # Environment variables (optional)
├── .streamlit/
│   └── secrets.toml         # Streamlit secrets (optional)
└── README.md                # This file
```

### AI Integration
- Uses OpenRouter API with the `moonshotai/kimi-dev-72b:free` model
- Configurable temperature and token limits
- Fallback to rule-based recommendations if AI is unavailable

## ⚠️ Important Notes

### Health Disclaimer
This application provides general fitness and nutrition recommendations for informational purposes only. It is not a substitute for professional medical advice. Users with medical conditions should consult healthcare providers before starting new fitness or nutrition programs.

### Data Privacy
- No user data is stored permanently
- Optional email collection for recommendation delivery
- API calls to OpenRouter follow their privacy policy

### Limitations
- Recommendations are based on general guidelines
- BMI calculations may not account for muscle mass variations
- AI recommendations depend on API availability and limits

## 🤝 Contributing

To improve this application:
1. Fork or copy the code
2. Make your enhancements
3. Test thoroughly with various user profiles
4. Share improvements with the community

## 📝 License

This project is open source and available for educational and personal use.

## 🆘 Support

If you encounter issues:
1. Check that all dependencies are installed correctly
2. Verify API key configuration if using AI features
3. Ensure you're using a compatible Python version
4. Check the Streamlit documentation for deployment issues

## 🔄 Version History

- **v1.0**: Initial release with basic recommendations and AI integration
- Features BMI calculation, rule-based suggestions, and OpenRouter AI support

---

**Built with ❤️ using Streamlit and OpenRouter AI**
