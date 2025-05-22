from nicegui import ui

def create_header():
    with ui.header().classes('bg-blue-600 text-white p-4'):
        ui.label('John Doe - AI Engineer').classes('text-2xl font-bold')
        with ui.row():
            ui.link('Home', '#').classes('text-white mx-2')
            ui.link('About', '#about').classes('text-white mx-2')
            ui.link('Skills', '#skills').classes('text-white mx-2')
            ui.link('Projects', '#projects').classes('text-white mx-2')
            ui.link('Contact', '#contact').classes('text-white mx-2')