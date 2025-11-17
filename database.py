import os
from typing import Any, Dict, List, Optional
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

DATABASE_URL = os.getenv("DATABASE_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "appdb")

_client: Optional[AsyncIOMotorClient] = None
_db: Optional[AsyncIOMotorDatabase] = None

async def get_db() -> AsyncIOMotorDatabase:
    global _client, _db
    if _db is None:
        _client = AsyncIOMotorClient(DATABASE_URL)
        _db = _client[DATABASE_NAME]
    return _db

async def create_document(collection: str, data: Dict[str, Any]) -> Dict[str, Any]:
    db = await get_db()
    payload = {**data, "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()}
    result = await db[collection].insert_one(payload)
    doc = await db[collection].find_one({"_id": result.inserted_id})
    if doc:
        doc["id"] = str(doc.pop("_id"))
    return doc or {}

async def get_documents(collection: str, filter_dict: Optional[Dict[str, Any]] = None, limit: int = 100) -> List[Dict[str, Any]]:
    db = await get_db()
    cursor = db[collection].find(filter_dict or {}).limit(limit)
    results: List[Dict[str, Any]] = []
    async for doc in cursor:
        doc["id"] = str(doc.pop("_id"))
        results.append(doc)
    return results

async def upsert_singleton(collection: str, data: Dict[str, Any]) -> Dict[str, Any]:
    db = await get_db()
    data["updated_at"] = datetime.utcnow()
    await db[collection].update_one({}, {"$set": data}, upsert=True)
    doc = await db[collection].find_one({})
    if doc:
        doc["id"] = str(doc.pop("_id"))
    return doc or {}
