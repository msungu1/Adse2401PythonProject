# =====================================================
# ADSE-Restaurant - Python + MongoDB Complete Demo
# =====================================================

from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId

# ====================== CONNECT TO MONGODB ======================
client = MongoClient('mongodb://localhost:27017/')
db = client["ADSE-Restaurant"]

menu_col = db["menu"]
customers_col = db["customers"]
orders_col = db["orders"]

print("✅ Connected to MongoDB - ADSE-Restaurant\n")


# -----------------------------------------------------------------
# 1. MENU OPERATIONS
# -----------------------------------------------------------------

def add_menu_item(name, category, sizes_list):
    """Add a new menu item with multiple sizes"""
    item = {
        "name": name,
        "category": category,
        "sizes": sizes_list,
        "created_at": datetime.now()
    }
    result = menu_col.insert_one(item)
    print(f"✅ Menu item '{name}' added! ID: {result.inserted_id}")


def view_menu():
    """Display all menu items"""
    print("\n📋 === MENU ===")
    menu_items = menu_col.find()

    for item in menu_items:
        print(f"\n🍕 {item['name']} ({item['category']})")
        for size in item.get('sizes', []):
            print(f"   • {size['size'].capitalize()}: KES {size['price_kes']}")
    print("-" * 40)


# -----------------------------------------------------------------
# 2. CUSTOMER OPERATIONS
# -----------------------------------------------------------------

def add_customer(name, phone, email, sold=False):
    """Add a new customer"""
    customer = {
        "name": name,
        "phone": phone,
        "email": email,
        "sold": sold,
        "created_at": datetime.now()
    }
    result = customers_col.insert_one(customer)
    print(f"✅ Customer '{name}' added! ID: {result.inserted_id}")
    return result.inserted_id


def view_customers():
    """Show all customers"""
    print("\n👥 === ALL CUSTOMERS ===")
    for customer in customers_col.find():
        status = "✅ Sold" if customer.get("sold") else "⏳ Not Sold"
        print(f"• {customer['name']} | {customer['phone']} | {customer['email']} | {status}")
    print("-" * 40)


# -----------------------------------------------------------------
# 3. ORDER OPERATIONS
# -----------------------------------------------------------------

def create_order(customer_id, items_list):
    """
    Create a new order
    items_list example: [{"menu_item_id": id, "size": "medium", "quantity": 2}, ...]
    """
    order = {
        "customer_id": ObjectId(customer_id),
        "items": items_list,
        "status": "pending",
        "order_date": datetime.now(),
        "total_amount": 0  # You can calculate this later if needed
    }

    result = orders_col.insert_one(order)
    print(f"✅ Order created successfully! Order ID: {result.inserted_id}")


def view_orders():
    """View all orders"""
    print("\n📦 === ALL ORDERS ===")
    for order in orders_col.find().sort("order_date", -1):
        customer = customers_col.find_one({"_id": order["customer_id"]})
        customer_name = customer["name"] if customer else "Unknown"

        print(f"\n🧾 Order ID: {order['_id']}")
        print(f"Customer: {customer_name}")
        print(f"Date: {order['order_date'].strftime('%Y-%m-%d %H:%M')}")
        print(f"Status: {order['status'].upper()}")

        for item in order.get("items", []):
            menu_item = menu_col.find_one({"_id": ObjectId(item["menu_item_id"])})
            item_name = menu_item["name"] if menu_item else "Unknown Item"
            print(f"   • {item_name} ({item['size']}) x {item['quantity']}")
    print("-" * 40)


# -----------------------------------------------------------------
# UPDATE OPERATIONS
# -----------------------------------------------------------------

def update_menu_item(menu_id, new_name=None, new_category=None, new_sizes=None):
    """Update: Modify a menu item"""
    update_data = {}
    if new_name:      update_data["name"] = new_name
    if new_category:  update_data["category"] = new_category
    if new_sizes:     update_data["sizes"] = new_sizes

    if not update_data:
        print("❌ Nothing to update!")
        return

    result = menu_col.update_one(
        {"_id": ObjectId(menu_id)},
        {"$set": update_data}
    )

    if result.modified_count > 0:
        print(f"✅ Menu item updated successfully!")
    else:
        print(f"❌ No changes made or item not found.")


def update_customer(customer_id, name=None, phone=None, email=None, sold=None):
    """Update: Modify customer information"""
    update_data = {}
    if name:   update_data["name"] = name
    if phone:  update_data["phone"] = phone
    if email:  update_data["email"] = email
    if sold is not None: update_data["sold"] = sold

    result = customers_col.update_one(
        {"_id": ObjectId(customer_id)},
        {"$set": update_data}
    )

    if result.modified_count > 0:
        print(f"✅ Customer updated successfully!")
    else:
        print(f"❌ Customer not found or no changes made.")


def update_order_status(order_id, new_status):

    result = orders_col.update_one(
        {"_id": ObjectId(order_id)},
        {"$set": {"status": new_status.lower()}}
    )

    if result.modified_count > 0:
        print(f"✅ Order status updated to '{result.modified_count}' successfully!")



    def delete_customer(customer_id):
        result = customers_col.delete_one({"_id": (customer_id)})
        print(f"Customer deleted:{result.deleted_count}")

        #Entry point to our app===============================================
        if __name__ == "__main__":
            add_menu_item()

            customer_id = add_customer("alice", "0713800378","akidiva@robert.com")

            create_order(customer_id)

            view_orders()
            view_customers()
            view_customers()

# ====================== TEST / DEMO ======================

if __name__ == "__main__":
    print("🚀 Starting ADSE-Restaurant System...\n")

    # 1. Add some menu items (run only once)
    # add_menu_item("Pizza", "Food", [
    #     {"size": "small", "price_kes": 500},
    #     {"size": "medium", "price_kes": 800},
    #     {"size": "large", "price_kes": 1200}
    # ])
    # add_menu_item("Burger", "Food", [
    #     {"size": "regular", "price_kes": 450},
    #     {"size": "double", "price_kes": 750}
    # ])

    # 2. View Menu
    view_menu()

    # 3. Add Customers
    # customer1 = add_customer("Robert Kamau", "+254 712 345 678", "robert@example.com", sold=True)
    # customer2 = add_customer("Jane Wanjiku", "+254 723 456 789", "jane@example.com", sold=False)

    # 4. View Customers
    view_customers()

    # 5. Create Order Example (Uncomment and replace IDs after adding data)
    # create_order(customer1, [
    #     {"menu_item_id": "your_pizza_id_here", "size": "large", "quantity": 1},
    #     {"menu_item_id": "your_burger_id_here", "size": "regular", "quantity": 2}
    # ])

    # 6. View All Orders
    view_orders()

    print("\n🎉 Demo completed! Add your own data by uncommenting the functions.")