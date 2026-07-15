from fastapi import APIRouter, Request
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_SERVICE_ROLE_KEY"),
)

@router.post("/lemon")
async def lemon_webhook(request: Request):
    try:
        payload = await request.json()

        print("========== WEBHOOK RECEIVED ==========")
        print(payload)

        event = payload.get("meta", {}).get("event_name")
        print("Event:", event)

        if event != "subscription_created":
            return {"status": "ignored"}

        attributes = payload["data"]["attributes"]
        customer_email = attributes.get("user_email")

        print("Customer Email:", customer_email)

        users = supabase.auth.admin.list_users()

        print("LIST USERS RESPONSE:")
        print(users)

        return {"status": "received"}

    except Exception as e:
        print("========== WEBHOOK ERROR ==========")
        import traceback
        traceback.print_exc()
        raise