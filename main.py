import os
from dotenv import load_dotenv
from nicegui import ui, app

# Load environment variables
load_dotenv()

# Import our portfolio components
from app.components.header import create_header
from app.components.about import create_about_section
from app.components.skills import create_skills_section
from app.components.projects import create_projects_section
from app.components.contact import create_contact_section

# Custom CSS
custom_css = '''
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f4f4f4;
}
.card {
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
}
'''

@ui.page('/')
def portfolio_page():
    ui.add_head_html(f'<style>{custom_css}</style>')
    with ui.column().classes('w-full max-w-3xl mx-auto p-4'):
        create_header()
        create_about_section()
        create_skills_section()
        create_projects_section()
        create_contact_section()

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    ui.run(port=port, title="AI Engineer Portfolio")