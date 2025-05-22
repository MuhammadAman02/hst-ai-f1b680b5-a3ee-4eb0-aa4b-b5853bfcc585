from nicegui import ui

def create_skills_section():
    with ui.card().classes('w-full my-4') as card:
        card.set_id('skills')
        ui.label('Skills').classes('text-2xl font-bold mb-2')
        skills = [
            'Machine Learning', 'Deep Learning', 'Natural Language Processing',
            'Computer Vision', 'Python', 'TensorFlow', 'PyTorch', 'Scikit-learn',
            'Data Analysis', 'Big Data', 'Cloud Computing (AWS, GCP)', 'Docker'
        ]
        with ui.grid(columns=3).classes('gap-4'):
            for skill in skills:
                ui.label(skill).classes('p-2 bg-blue-100 rounded')