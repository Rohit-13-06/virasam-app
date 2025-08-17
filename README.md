VIRASAM: The Living Cultural Archive



VIRASAM is a community-driven platform designed to preserve, share, and discover cultural heritage.
It enables communities to document and maintain their folk culture, traditions, local history, and traditional recipes through an interactive web application.


🌟 Features
Core Functionality


Folk Culture Documentation: Preserve traditional stories, songs, dances, and customs

Traditions Archive: Document ceremonies, festivals, and cultural practices

Local History: Capture historical events, landmarks, and community stories

Traditional Recipes: Maintain culinary heritage and cooking traditions

Technical Features


AI-Powered Responses: Integrated Ollama LLM for intelligent content generation

Multilingual Support: Telugu language translation support

Database Integration: Supabase backend for reliable data storage

User Authentication: Secure user registration and login system

Responsive Design: Mobile-friendly interface

Advanced Capabilities


Smart Search: Query the cultural content database

Content Contribution: Community-driven content submission

Question-Answer System: AI fallback for unanswered queries

Media Support: Upload images, audio, and video

Real-time Updates: Live content sync



🚀 Quick Start

Prerequisites

Python 3.8 or higher
Supabase account and project
Ollama installed and running (for AI features)


Installation
Clone the repository
git clone https://code.swecha.org/yourusername/virasam-app.git
cd virasam-app
text
Install dependencies
pip install -r requirements.txt
text
Set up Supabase

Create a project on Supabase

Run the SQL schema from database/schema.sql

Configure RLS policies as shown in database/rls_policies.sql


Configure environment
Create .streamlit/secrets.toml:
SUPABASE_URL = "your-supabase-url"
SUPABASE_ANON_KEY = "your-supabase-anon-key"
text
Set up Ollama (for AI)
curl https://ollama.ai/install.sh | sh
ollama pull llama3.2:1b
ollama pull llama3:latest
ollama serve
text
Run the application
streamlit run frontend/app.py
text


📁 Project Structure
virasam-app/
├── frontend/
│ ├── app.py # Main Streamlit application
│ ├── pages/
│ │ ├── folk.py
│ │ ├── tradition.py
│ │ ├── history.py
│ │ ├── recipes.py
│ │ ├── search.py
│ │ ├── contribute.py
│ │ └── community.py
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
└── config.toml
text


💾 Database Schema
Core Tables for each category


{category}_questions - User questions

{category}_content   - Searchable content

{category}_answers   - AI-generated responses

{category}_contributions - User-submitted content

Key Features

UUID primary keys on all tables
Foreign key relationships between questions and answers
Row Level Security (RLS)
Automatic timestamps



🔧 Configuration


SUPABASE_URL – Your Supabase project URL

SUPABASE_ANON_KEY – Your Supabase anon key

Ollama Models


llama3.2:1b – Fast and concise

llama3:latest – Detailed and comprehensive



🌐 Usage
For Users

Register/Login to contribute
Browse and search folk culture, traditions, history, or recipes
Ask questions – get AI-powered responses
Contribute your cultural knowledge
Find cultural information

For Admins

Moderate user submissions
Manage Supabase database
Edit content directly if needed



🤝 Contributing
We welcome contributions from the community!
Please see CONTRIBUTING.md for:

Guidelines
Development setup
Pull request process
Code style



📜 License
This project is licensed under the GNU Affero General Public License v3.0 (AGPLv3).
See LICENSE or online for details.


🔗 Links


Documentation: docs/


Report Issues: Use GitLab issues for this repo

Main Website: Streamlit




🙏 Acknowledgments

Built with Streamlit

Powered by Supabase

AI by Ollama

Community knowledge from contributors


VIRASAM – Preserving Cultural Heritage for Future Generations 🌍
