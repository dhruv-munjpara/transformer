"""
SESSION 6 - Task 2: Food Delivery Customer Support Chatbot Flow
Simulating Swiggy/Zomato Support Flow using Python with if-else decision logic
Handling: Order Status, Refund Request, and Delivery Delay.
"""

import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

def food_delivery_support_bot():
    print("=" * 60)
    print("🍔 Welcome to ZomaBites 24x7 Customer Support! 🛵")
    print("=" * 60)
    print("Hello! I am your automated assistant. How can I help you today?")
    print("You can ask about:\n1. Order Status\n2. Refund Request\n3. Delivery Delay\n(Type 'exit' to quit)\n")

    # Mock order database for demonstration
    mock_order = {
        "order_id": "ZB-98214",
        "restaurant": "Honest Pav Bhaji, Ahmedabad",
        "status": "Out for delivery with Valet Rahul",
        "eta_minutes": 12,
        "amount": 340,
        "is_delayed": True
    }

    while True:
        user_input = input("\nYou: ").strip().lower()

        if user_input in ["exit", "quit", "bye"]:
            print("ZomaBites Bot: Thank you for contacting ZomaBites. Enjoy your meal! 👋")
            break

        # 1. Order Status Flow
        elif any(keyword in user_input for keyword in ["status", "where is my food", "track", "order location", "track order"]):
            print(f"\nZomaBites Bot: 📦 Order #{mock_order['order_id']} from '{mock_order['restaurant']}':")
            print(f"👉 Current Status: {mock_order['status']}")
            print(f"⏱️ Estimated Time of Arrival: ~{mock_order['eta_minutes']} minutes.")

        # 2. Refund Request Flow
        elif any(keyword in user_input for keyword in ["refund", "cancel", "money back", "return", "wrong item"]):
            print(f"\nZomaBites Bot: 💳 Refund Request for Order #{mock_order['order_id']}:")
            reason = input("ZomaBites Bot: Please specify the reason (1: Cancelled Order, 2: Missing/Spilled Item, 3: Quality Issue): ")
            if "1" in reason or "cancel" in reason:
                print(f"ZomaBites Bot: ✅ A full refund of ₹{mock_order['amount']} has been initiated to your original payment method. Ref ID: REF-44821. It will reflect in 2-4 hours.")
            elif "2" in reason or "missing" in reason or "spill" in reason:
                print(f"ZomaBites Bot: 📸 We are sorry to hear that! An instant partial refund credit of ₹150 has been added to your ZomaBites Wallet.")
            else:
                print(f"ZomaBites Bot: 📝 Ticket #TCK-1092 logged. Our human executive will review your photos and process refund within 1 hour.")

        # 3. Delivery Delay Flow
        elif any(keyword in user_input for keyword in ["delay", "late", "taking too long", "not delivered", "stuck"]):
            print(f"\nZomaBites Bot: ⚠️ We sincerely apologize for the delay!")
            if mock_order["is_delayed"]:
                print("ZomaBites Bot: Our delivery partner encountered heavy traffic near SG Highway. They are currently 1.8 km away.")
                print(f"ZomaBites Bot: Updated ETA is {mock_order['eta_minutes']} mins. We have credited a ₹50 Late Delivery compensation voucher to your account!")
            else:
                print("ZomaBites Bot: Your order is on schedule and arriving within estimated delivery time.")

        # Default fallback
        else:
            print("\nZomaBites Bot: I'm sorry, I didn't quite catch that. Please choose from:")
            print("1. 'Check order status' (Track delivery)")
            print("2. 'Request a refund' (Payment or missing item)")
            print("3. 'Delivery delay issue' (Late arrival assistance)")

if __name__ == "__main__":
    food_delivery_support_bot()
