# AI Meal Planner App 🍽️🤖

An intelligent meal planning application powered by AI that helps users create personalized meal plans, manage dietary preferences, and discover nutritious recipes. Built with Python and Streamlit for an interactive user experience.

## 📌 Project Overview

The AI Meal Planner App uses artificial intelligence to generate customized meal plans based on user preferences, dietary restrictions, nutritional goals, and available ingredients. It provides an intuitive interface for users to plan their meals efficiently and maintain a healthy lifestyle.

## ✨ Features

- 🤖 **AI-Powered Meal Suggestions** - Intelligent meal recommendations based on preferences
- 📊 **Nutritional Analysis** - Track calories, macros, and nutritional information
- 🥗 **Dietary Preferences** - Support for various diets (vegetarian, vegan, keto, etc.)
- 📅 **Meal Planning** - Weekly meal plan generation and management
- 🛒 **Shopping List** - Automatic grocery list generation
- 💬 **Interactive Chat** - Conversational AI for meal planning assistance
- 📱 **Responsive UI** - User-friendly Streamlit interface

## 📂 Project Structure
```
AI-Meal-Planner-App/
├── .idea/                          # IDE configuration files
├── .streamlit/                     # Streamlit configuration
├── chat.py                         # Chat interface and conversation handling
├── data.py                         # Data management and processing
├── kba.py                          # Knowledge base and algorithms
├── main.py                         # Main application entry point
├── prompts.py                      # AI prompt templates and management
├── streamlit_meal_planner.py       # Streamlit UI components
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore rules
├── LICENSE                         # MIT License
└── README.md                       # Project documentation
```

## 🛠️ Technologies Used

- **Python** - Core programming language
- **Streamlit** - Web application framework
- **AI/ML Libraries** - For intelligent recommendations
- **Data Processing** - Pandas, NumPy
- **Natural Language Processing** - For chat functionality

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/shettynaviya/AI-Meal-Planner-App.git
cd AI-Meal-Planner-App
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
streamlit run streamlit_meal_planner.py
```

The app will open in your default browser at `http://localhost:8501`

## 📖 Usage

### 1. **Set Your Preferences**
- Enter dietary restrictions (vegetarian, vegan, gluten-free, etc.)
- Specify calorie goals and macronutrient targets
- Add any food allergies or dislikes

### 2. **Generate Meal Plans**
- Select the number of days for meal planning
- Choose meals (breakfast, lunch, dinner, snacks)
- Generate AI-powered meal suggestions

### 3. **Interactive Chat**
- Ask questions about recipes
- Get cooking tips and substitutions
- Request modifications to meal plans

### 4. **Shopping List**
- View automatically generated grocery lists
- Organize ingredients by category
- Export lists for easy shopping

## 🎯 Key Components

### `main.py`
Main application entry point that initializes the app and coordinates between different modules.

### `streamlit_meal_planner.py`
Streamlit UI implementation with interactive components for meal planning interface.

### `chat.py`
Handles conversational AI functionality for user interactions and queries.

### `data.py`
Manages data processing, storage, and retrieval of meal and nutritional information.

### `kba.py`
Knowledge base algorithms for meal recommendations and nutritional calculations.

### `prompts.py`
AI prompt templates and engineering for generating contextual responses.

## 🍴 Supported Diet Types

- 🥗 Vegetarian
- 🌱 Vegan
- 🥑 Keto
- 🍖 Paleo
- 🌾 Gluten-Free
- 🥛 Dairy-Free
- 🌊 Mediterranean
- ⚖️ Balanced/General

## 📊 Features in Detail

### AI-Powered Recommendations
- Personalized meal suggestions based on preferences
- Nutritional balance optimization
- Variety in meal planning to avoid repetition

### Nutritional Tracking
- Calorie counting
- Macronutrient breakdown (proteins, carbs, fats)
- Micronutrient information
- Dietary fiber tracking

### Smart Shopping Lists
- Ingredient aggregation across meals
- Quantity calculations
- Category organization
- Pantry item suggestions

## 🔧 Configuration

The app can be configured through the Streamlit configuration files in the `.streamlit/` directory.

### Custom Settings
- Theme customization
- Default dietary preferences
- Calorie targets
- API configurations (if applicable)

## 📝 Requirements

See `requirements.txt` for a complete list of dependencies. Key packages include:
```txt
streamlit
pandas
numpy
requests
python-dotenv
(and other dependencies)
```

## 🤝 Contributing

Contributions are welcome! If you'd like to improve the AI Meal Planner App:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Known Issues

- Currently tracking issues in the GitHub Issues section
- Report bugs by opening a new issue

## 🔮 Future Enhancements

- [ ] Recipe image generation
- [ ] Meal preparation time estimates
- [ ] Cost estimation per meal
- [ ] Integration with grocery delivery services
- [ ] Mobile app version
- [ ] Multi-user support for families
- [ ] Meal history and favorites
- [ ] Advanced nutritional analytics

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Shetty Naviya**
- GitHub: [@shettynaviya](https://github.com/shettynaviya)
- Repository: [AI-Meal-Planner-App](https://github.com/shettynaviya/AI-Meal-Planner-App)

## 🙏 Acknowledgments

- Thanks to the Streamlit community for the excellent framework
- Nutritional data sources and APIs
- Open-source AI/ML libraries
- Contributors and testers

## 📞 Support

For support, questions, or feedback:
- Open an issue on GitHub
- Contact through GitHub profile

## 🌟 Show Your Support

If you find this project helpful, please consider:
- ⭐ Starring the repository
- 🍴 Forking for your own use
- 📢 Sharing with others who might benefit

## 📚 Documentation

For more detailed documentation on specific features:
- See inline code comments
- Check the `/docs` folder (if available)
- Review the Wiki section on GitHub

---

**Made with ❤️ and 🤖 AI** | Helping people eat better, one meal at a time!

💡 *"Let AI plan your meals, so you can focus on enjoying them!"*
