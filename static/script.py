from tkinter import Tk, Label, Frame, Button
import scrollreveal  # Assuming a hypothetical Python equivalent for ScrollReveal
from typing import List

# toggle icon navbar
menu_icon = None  # Placeholder for the menu icon
navbar = None  # Placeholder for the navbar

def toggle_menu():
    menu_icon['class'] = 'bx-x' if 'bx-x' not in menu_icon['class'] else ''
    navbar['class'] = 'active' if 'active' not in navbar['class'] else ''

# scroll sections active links
sections = []  # Placeholder for sections
nav_links = []  # Placeholder for nav links

def on_scroll():
    top = 0  # Placeholder for window.scrollY
    for sec in sections:
        offset = sec['offsetTop'] - 150
        height = sec['offsetHeight']
        id = sec['id']

        if top >= offset and top < offset + height:
            for link in nav_links:
                link['class'] = ''
                # Assuming a method to find the link by id
                find_link_by_id(id)['class'] = 'active'

    # sticky navbar
    header = None  # Placeholder for header
    header['class'] = 'sticky' if top > 100 else ''

    # remove toggle icon and navbar when click navbar link (scroll)
    menu_icon['class'] = ''
    navbar['class'] = 'active'

# scroll reveal
scrollreveal.init({
    'distance': '80px',
    'duration': 2000,
    'delay': 200
})
scrollreveal.reveal('.home-content, .heading', {'origin': 'top'})
scrollreveal.reveal('.home-img, .services-container, .portfolio-box, .contact form', {'origin': 'bottom'})
scrollreveal.reveal('.home-content h1, .about-img', {'origin': 'left'})
scrollreveal.reveal('.home-content p, .about-content', {'origin': 'right'})

# typed JS
typed = Typed('.multiple-text', {
    'strings': ['Data Scientist', 'Data Scientist', 'Data Scientist'],
    'typeSpeed': 100,
    'backSpeed': 100,
    'backDelay': 100,
    'loop': True
})

