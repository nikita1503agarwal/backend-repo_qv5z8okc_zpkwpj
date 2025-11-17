from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional

# Global content blocks
class GlobalSettings(BaseModel):
    site_title: str = Field(default="Robert Scott — Portfolio")
    tagline: str = Field(default="Cinematic design, strategy, and visual storytelling")
    email: str = Field(default="hello@robertscott.com")
    phone: str = Field(default="+")
    whatsapp: Optional[str] = None
    social_links: List[str] = Field(default_factory=list)
    copyright_text: str = Field(default="© 2025 Robert Scott. All rights reserved.")

# Home/About
class Hero(BaseModel):
    headline: str
    sub_roles: List[str]
    tagline: str
    cta_label: str
    portrait_url: HttpUrl
    gallery_urls: List[HttpUrl] = Field(default_factory=list)

class About(BaseModel):
    biography: str
    background: str
    mission: str
    cv_url: Optional[HttpUrl] = None

# Services/Skills/Pricing
class Service(BaseModel):
    title: str
    description: str
    image_url: Optional[HttpUrl] = None
    price: Optional[str] = None
    cta_label: Optional[str] = None

class Skill(BaseModel):
    name: str
    icon: Optional[str] = None  # store icon key

class Package(BaseModel):
    title: str
    features: List[str]
    price: Optional[str] = None

# Portfolio/Case Studies
class PortfolioItem(BaseModel):
    title: str
    category: str
    main_image: HttpUrl
    images: List[HttpUrl] = Field(default_factory=list)
    description: str

class CaseStudy(BaseModel):
    name: str
    problem: str
    approach: str
    tools: List[str]
    results: str
    media: List[HttpUrl] = Field(default_factory=list)

# Testimonials/Blog/Contact/Footer
class Testimonial(BaseModel):
    client_name: str
    review: str
    client_photo: Optional[HttpUrl] = None
    brand_logo: Optional[HttpUrl] = None
    screenshots: List[HttpUrl] = Field(default_factory=list)

class BlogPost(BaseModel):
    title: str
    thumbnail: Optional[HttpUrl] = None
    body: str
    category: Optional[str] = None
    publish_date: Optional[str] = None

class ContactBlock(BaseModel):
    email: str
    phone: Optional[str] = None
    whatsapp: Optional[str] = None
    socials: List[str] = Field(default_factory=list)

