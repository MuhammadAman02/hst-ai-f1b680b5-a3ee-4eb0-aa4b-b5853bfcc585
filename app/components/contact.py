from nicegui import ui

def create_contact_section():
    with ui.card().classes('w-full my-4') as card:
        card.set_id('contact')
        ui.label('Contact Me').classes('text-2xl font-bold mb-2')
        ui.label('Email: john.doe@example.com')
        ui.label('LinkedIn: linkedin.com/in/johndoe')
        ui.label('GitHub: github.com/johndoe')
        
        with ui.row():
            ui.input(label='Name').style('width: 200px')
            ui.input(label='Email').style('width: 200px')
        ui.textarea(label='Message').style('width: 400px')
        ui.button('Send', on_click=lambda: ui.notify('Message sent!'))