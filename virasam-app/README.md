# VIRASAM: The Living Cultural Archive

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF6B6B.svg)](https://streamlit.io/)

VIRASAM is a community-driven platform designed to preserve, share, and discover cultural heritage. It enables communities to document and maintain their folk culture, traditions, local history, and traditional recipes through an interactive web application.

## 🌟 Features

### Core Functionality
- **Folk Culture Documentation**: Preserve traditional stories, songs, dances, and customs
- **Traditions Archive**: Document ceremonies, festivals, and cultural practices
- **Local History**: Capture historical events, landmarks, and community stories
- **Traditional Recipes**: Maintain culinary heritage and cooking traditions

### Technical Features
- **AI-Powered Responses**: Integrated Ollama LLM for intelligent content generation
- **Multilingual Support**: Telugu language translation support
- **Database Integration**: Supabase backend for reliable data storage
- **User Authentication**: Secure user registration and login system
- **Responsive Design**: Mobile-friendly interface built with Streamlit

### Advanced Capabilities
- **Smart Search**: Query existing cultural content database
- **Content Contribution**: Community-driven content submission
- **Question-Answer System**: AI fallback for unanswered queries
- **Media Support**: Upload images, audio, and video files
- **Real-time Updates**: Live content synchronization

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Supabase account and project
- Ollama installed and running (for AI features)

### Installation

1. **Clone the repository**
git clone https://github.com/yourusername/virasam-app.git
cd virasam-app

text

2. **Install dependencies**
pip install -r requirements.txt

text

3. **Set up Supabase**
- Create a new project on [Supabase](https://supabase.com)
- Run the SQL schema from `database/schema.sql`
- Configure RLS policies using `database/rls_policies.sql`

4. **Configure environment**
Create `.streamlit/secrets.toml`:
[secrets]
SUPABASE_URL = "your-supabase-url"
SUPABASE_ANON_KEY = "your-supabase-anon-key"

text

5. **Set up Ollama (for AI features)**
Install Ollama
curl https://ollama.ai/install.sh | sh

Pull required models
ollama pull llama3.2:1b
ollama pull llama3:latest

Start Ollama service
ollama serve

text

6. **Run the application**
streamlit run frontend/app.py

text

## 📁 Project Structure

virasam-app/
├── frontend/
│ ├── app.py # Main Streamlit application
│ ├── pages/ # Feature-specific pages
│ │ ├── folk.py # Folk culture module
│ │ ├── tradition.py # Traditions module
│ │ ├── history.py # Local history module
│ │ ├── recipes.py # Traditional recipes module
│ │ ├── search.py # Search functionality
│ │ ├── contribute.py # Content contribution
│ │ └── community.py # Community features
│ └── utils/
│ ├── ai_fallback.py # AI integration
│ └── translation.py # Language support
├── backend/
│ └── database.py # Database operations
├── database/
│ ├── schema.sql # Database schema
│ └── sample_data.sql # Sample content
├── docs/ # Additional documentation
└── .streamlit/
└── config.toml # Streamlit configuration

text

## 💾 Database Schema

The application uses the following main tables:

### Core Tables (per category: folk, traditions, history, recipes)
- `{category}_questions` - User questions
- `{category}_content` - Searchable content
- `{category}_answers` - AI-generated responses
- `{category}_contributions` - User-submitted content

### Key Features
- UUID primary keys for all tables
- Foreign key relationships between questions and answers
- Row Level Security (RLS) for data protection
- Automatic timestamps for all records

## 🔧 Configuration

### Environment Variables
- `SUPABASE_URL` - Your Supabase project URL
- `SUPABASE_ANON_KEY` - Your Supabase anonymous key

### Ollama Models
- `llama3.2:1b` - Fast model for quick responses
- `llama3:latest` - Comprehensive model for detailed responses

## 🌐 Usage

### For Users
1. **Register/Login**: Create an account to start contributing
2. **Explore Categories**: Browse folk culture, traditions, history, or recipes
3. **Ask Questions**: Get AI-powered responses about cultural topics
4. **Contribute Content**: Share your cultural knowledge with the community
5. **Search Content**: Find existing cultural information

### For Administrators
1. **Content Moderation**: Review and approve user contributions
2. **Database Management**: Monitor and maintain cultural content
3. **User Management**: Handle user accounts and permissions

## 🤝 Contributing

We welcome contributions from the community! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on:
- Code contribution guidelines
- Development setup
- Pull request process
- Code style standards

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **Documentation**: [docs/](docs/)
- **Issues**: [GitHub Issues](https://github.com/yourusername/virasam-app/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/virasam-app/discussions)

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/) for the web interface
- Powered by [Supabase](https://supabase.com/) for backend services
- AI capabilities provided by [Ollama](https://ollama.ai/)
- Community-driven cultural content from contributors

## 📞 Support

For support, please:
1. Check the [documentation](docs/)
2. Search [existing issues](https://github.com/yourusername/virasam-app/issues)
3. Create a new issue with detailed information

---

**VIRASAM** - Preserving Cultural Heritage for Future Generations 🌍