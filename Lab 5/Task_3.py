import random
# Sample product categories and products
products = {
    "soap": ["Dove Soap", "Lux Soap", "Pears Soap"],
    "mobile": ["iPhone 14", "Samsung Galaxy S23", "OnePlus 11"],
    "toys": ["Lego Set", "Barbie Doll", "Hot Wheels Car"],
    "games": ["FIFA 23", "Minecraft", "Chess Board"],
    "shampoo": ["Head & Shoulders", "Pantene", "Clinic Plus"],
    "laptop": ["Dell Inspiron", "MacBook Air", "HP Pavilion"]
}

# User search history
user_history = []

def recommend_products(history):
    recommendations = []
    for item in history:
        item = item.lower()
        if item in products:
            recommendations.extend(products[item])
    # If no history, recommend random products
    if not recommendations:
        for prod_list in products.values():
            recommendations.extend(random.sample(prod_list, 1))
    return list(set(recommendations))

def main():
    print("Welcome to the Product Recommendation System!")
    print("Type your search (e.g., soap, mobile, toys, games). Type 'exit' to finish.")
    while True:
        search = input("Search for a product category: ").strip()
        if search.lower() == 'exit':
            break
        user_history.append(search)
        recs = recommend_products([search])
        print(f"Recommended products for '{search}': {', '.join(recs)}\n")
    # Final recommendations based on all history
    final_recs = recommend_products(user_history)
    print("Based on your search history, we recommend:")
    print(", ".join(final_recs))

if __name__ == "__main__":
    main()