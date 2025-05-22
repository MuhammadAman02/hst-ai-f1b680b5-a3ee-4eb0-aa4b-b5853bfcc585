from nicegui import ui

def create_about_section():
    with ui.card().classes('w-full my-4') as card:
        card.set_id('about')
        ui.label('About Me').classes('text-2xl font-bold mb-2')
        ui.markdown('''
        I am a passionate AI Engineer with expertise in machine learning, deep learning, and natural language processing. 
        With 5+ years of experience, I've developed and deployed AI solutions that have made significant impacts in various industries.
        
        My goal is to push the boundaries of AI technology and create innovative solutions that can positively transform businesses and society.
        ''')