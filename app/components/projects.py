from nicegui import ui

def create_projects_section():
    with ui.card().classes('w-full my-4') as card:
        card.set_id('projects')
        ui.label('Projects').classes('text-2xl font-bold mb-2')
        projects = [
            {
                'title': 'Sentiment Analysis Engine',
                'description': 'Developed a real-time sentiment analysis engine for social media data using BERT.',
            },
            {
                'title': 'Computer Vision for Autonomous Vehicles',
                'description': 'Implemented object detection and lane recognition algorithms for self-driving cars.',
            },
            {
                'title': 'AI-powered Chatbot',
                'description': 'Created a conversational AI chatbot using GPT-3 for customer support automation.',
            }
        ]
        for project in projects:
            with ui.card():
                ui.label(project['title']).classes('text-lg font-bold')
                ui.label(project['description'])