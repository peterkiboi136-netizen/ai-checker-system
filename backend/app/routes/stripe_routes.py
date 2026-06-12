import os
import stripe

from fastapi import APIRouter

router = APIRouter()

# ----------------------------------------
# STRIPE CONFIG
# ----------------------------------------
stripe.api_key = os.getenv(
    "STRIPE_SECRET_KEY"
)

PRICE_ID = os.getenv(
    "STRIPE_PRICE_ID"
)

# ----------------------------------------
# CREATE CHECKOUT SESSION
# ----------------------------------------
@router.post("/create-checkout-session")
def create_checkout_session():

    try:

        session = stripe.checkout.Session.create(

            payment_method_types=["card"],

            mode="subscription",

            line_items=[
                {
                    "price": PRICE_ID,
                    "quantity": 1,
                }
            ],

            success_url=
                "http://localhost:5173/success",

            cancel_url=
                "http://localhost:5173/cancel",
        )

        return {
            "checkout_url": session.url
        }

    except Exception as e:

        return {
            "error": str(e)
        }