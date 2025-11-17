# Examples of content documents to seed or guide the CMS structure
from typing import List

seed_services: List[dict] = [
    {"title": "Graphic Design", "description": "Brand systems, posters, album art, and cinematic key visuals.", "price": "From $1200", "cta_label": "Inquire"},
    {"title": "Digital Marketing", "description": "Data-driven funnels, ad creative, and lifecycle campaigns.", "price": "Custom", "cta_label": "Request Plan"},
    {"title": "Social Media Management", "description": "Content calendars, community, and creator partnerships.", "price": "From $800/mo", "cta_label": "Book"},
    {"title": "Photography & Videography", "description": "Editorial portraiture and product cinematography.", "price": "Custom", "cta_label": "See Reel"},
    {"title": "Events Management", "description": "Immersive brand experiences from concept to execution.", "price": "Custom", "cta_label": "Pitch Event"},
    {"title": "AI Integration", "description": "Automation, agents, and AI-driven creative pipelines.", "price": "From $2,500", "cta_label": "Discuss AI"},
    {"title": "Web Design & Development", "description": "Ultra-fast, SEO-first sites with modern interactions.", "price": "From $3,500", "cta_label": "Start a Site"},
]

seed_skills: List[dict] = [
    {"name": "Adobe Suite", "icon": "adobe"},
    {"name": "Canva", "icon": "canva"},
    {"name": "Figma", "icon": "figma"},
    {"name": "WordPress", "icon": "wordpress"},
    {"name": "AI Tools", "icon": "ai"},
    {"name": "Camera gear", "icon": "camera"},
]

seed_packages: List[dict] = [
    {"title": "Starter", "features": ["1 landing page", "Basic brand kit", "Email capture"], "price": "$1,500"},
    {"title": "Professional", "features": ["5 pages", "Brand system", "Social kit", "CMS"], "price": "$4,500"},
    {"title": "Enterprise", "features": ["Custom scope", "Strategy sprint", "A/B testing", "Retainer"], "price": "Contact for quote"},
]
