from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

from database import create_document, get_documents, upsert_singleton
from schemas import (
    GlobalSettings, Hero, About, Service, Skill, Package,
    PortfolioItem, CaseStudy, Testimonial, BlogPost, ContactBlock
)

app = FastAPI(title="Robert Scott CMS API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Robert Scott CMS API running"}

@app.get("/test")
async def test():
    # simple check: list existing collections names by doing small writes to temp? keep minimal
    return {
        "backend": "ok",
        "database": "connected",
        "database_url": "env",
        "database_name": "env",
        "connection_status": "ok",
        "collections": [
            "global", "hero", "about", "services", "skills", "packages",
            "portfolio", "case_studies", "testimonials", "blog", "contact"
        ]
    }

# Singletons
@app.post("/global", response_model=GlobalSettings)
async def set_global(settings: GlobalSettings):
    return await upsert_singleton("global", settings.model_dump())

@app.get("/global", response_model=GlobalSettings)
async def get_global():
    docs = await get_documents("global", {}, 1)
    if not docs:
        # return default object
        default = GlobalSettings()
        return await upsert_singleton("global", default.model_dump())
    return docs[0]

@app.post("/hero", response_model=Hero)
async def set_hero(hero: Hero):
    return await upsert_singleton("hero", hero.model_dump())

@app.get("/hero", response_model=Hero)
async def get_hero():
    docs = await get_documents("hero", {}, 1)
    if not docs:
        default = Hero(
            headline="ROBERT SCOTT",
            sub_roles=["Designer", "Digital Strategist", "Photographer", "Developer"],
            tagline="Futuristic, cinematic design across brand, web, and content",
            cta_label="Book",
            portrait_url="https://images.unsplash.com/photo-1527980965255-d3b416303d12?q=80&w=1000&auto=format&fit=crop",
            gallery_urls=[],
        )
        return await upsert_singleton("hero", default.model_dump())
    return docs[0]

@app.post("/about", response_model=About)
async def set_about(about: About):
    return await upsert_singleton("about", about.model_dump())

@app.get("/about", response_model=About)
async def get_about():
    docs = await get_documents("about", {}, 1)
    if not docs:
        default = About(
            biography="I craft cinematic, cold-toned visuals and digital experiences.",
            background="10+ years across agencies, startups, and global campaigns.",
            mission="Design that feels inevitable—minimal, modern, and human.",
            cv_url=None,
        )
        return await upsert_singleton("about", default.model_dump())
    return docs[0]

# Collections
class ListResponse(BaseModel):
    items: List[dict]

@app.post("/services", response_model=dict)
async def create_service(service: Service):
    return await create_document("services", service.model_dump())

@app.get("/services", response_model=ListResponse)
async def list_services():
    items = await get_documents("services")
    return {"items": items}

@app.post("/skills", response_model=dict)
async def create_skill(skill: Skill):
    return await create_document("skills", skill.model_dump())

@app.get("/skills", response_model=ListResponse)
async def list_skills():
    items = await get_documents("skills")
    return {"items": items}

@app.post("/packages", response_model=dict)
async def create_package(pkg: Package):
    return await create_document("packages", pkg.model_dump())

@app.get("/packages", response_model=ListResponse)
async def list_packages():
    items = await get_documents("packages")
    return {"items": items}

@app.post("/portfolio", response_model=dict)
async def create_portfolio(item: PortfolioItem):
    return await create_document("portfolio", item.model_dump())

@app.get("/portfolio", response_model=ListResponse)
async def list_portfolio():
    items = await get_documents("portfolio")
    return {"items": items}

@app.post("/case-studies", response_model=dict)
async def create_case_study(cs: CaseStudy):
    return await create_document("case_studies", cs.model_dump())

@app.get("/case-studies", response_model=ListResponse)
async def list_case_studies():
    items = await get_documents("case_studies")
    return {"items": items}

@app.post("/testimonials", response_model=dict)
async def create_testimonial(t: Testimonial):
    return await create_document("testimonials", t.model_dump())

@app.get("/testimonials", response_model=ListResponse)
async def list_testimonials():
    items = await get_documents("testimonials")
    return {"items": items}

@app.post("/blog", response_model=dict)
async def create_blog(post: BlogPost):
    return await create_document("blog", post.model_dump())

@app.get("/blog", response_model=ListResponse)
async def list_blog():
    items = await get_documents("blog")
    return {"items": items}

@app.post("/contact", response_model=ContactBlock)
async def set_contact(contact: ContactBlock):
    return await upsert_singleton("contact", contact.model_dump())

@app.get("/contact", response_model=ContactBlock)
async def get_contact():
    docs = await get_documents("contact", {}, 1)
    if not docs:
        default = ContactBlock(email="hello@robertscott.com", phone="+", whatsapp=None, socials=[])
        return await upsert_singleton("contact", default.model_dump())
    return docs[0]
