from fastapi import APIRouter
from pydantic import BaseModel
import os
import requests
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

API_KEY = os.getenv("LEMON_SQUEEZY_API_KEY")
STORE_ID = os.getenv("LEMON_SQUEEZY_STORE_ID")
VARIANT_ID = os.getenv("LEMON_SQUEEZY_VARIANT_ID")


class CheckoutRequest(BaseModel):
    user_id: str
    email: str


@router.post("/create-checkout")
def create_checkout(request: CheckoutRequest):

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/vnd.api+json",
        "Content-Type": "application/vnd.api+json",
    }

    payload = {
        "data": {
            "type": "checkouts",
            "attributes": {
                "checkout_data": {
                    "email": request.email,
                    "custom": {
                        "user_id": request.user_id
                    }
                }
            },
            "relationships": {
                "store": {
                    "data": {
                        "type": "stores",
                        "id": STORE_ID,
                    }
                },
                "variant": {
                    "data": {
                        "type": "variants",
                        "id": VARIANT_ID,
                    }
                },
            },
        }
    }

    response = requests.post(
        "https://api.lemonsqueezy.com/v1/checkouts",
        headers=headers,
        json=payload,
    )

    return response.json()