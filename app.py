
from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")


# Database connection
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# All 20 recipes with ingredients
recipes_data = [

    ("Vegetable Biryani", "Veg", [
        ("Basmati Rice", 2, "cups"),
        ("Onion", 2, "pieces"),
        ("Tomato", 1, "piece"),
        ("Carrot", 1, "piece"),
        ("Beans", 0.5, "cup"),
        ("Potato", 1, "piece"),
        ("Green Peas", 0.5, "cup"),
        ("Curd", 0.5, "cup"),
        ("Mint Leaves", 0.25, "cup"),
        ("Coriander Leaves", 0.25, "cup"),
        ("Green Chilli", 2, "pieces"),
        ("Ginger Garlic Paste", 1, "tbsp"),
        ("Biryani Masala", 2, "tsp"),
        ("Turmeric Powder", 0.5, "tsp"),
        ("Chilli Powder", 1, "tsp"),
        ("Garam Masala", 1, "tsp"),
        ("Bay Leaf", 2, "pieces"),
        ("Cinnamon", 1, "inch"),
        ("Cloves", 4, "pieces"),
        ("Cardamom", 3, "pieces"),
        ("Cumin Seeds", 1, "tsp"),
        ("Oil", 3, "tbsp"),
        ("Ghee", 1, "tbsp"),
        ("Lemon Juice", 1, "tbsp"),
        ("Salt", 1, "tsp")
    ]),

    ("Chicken Biryani", "Non-Veg", [
        ("Basmati Rice", 2, "cups"),
        ("Chicken", 500, "grams"),
        ("Onion", 2, "pieces"),
        ("Tomato", 1, "piece"),
        ("Curd", 0.5, "cup"),
        ("Mint Leaves", 0.25, "cup"),
        ("Coriander Leaves", 0.25, "cup"),
        ("Green Chilli", 3, "pieces"),
        ("Ginger Garlic Paste", 2, "tbsp"),
        ("Biryani Masala", 2, "tsp"),
        ("Turmeric Powder", 0.5, "tsp"),
        ("Chilli Powder", 1, "tsp"),
        ("Garam Masala", 1, "tsp"),
        ("Bay Leaf", 2, "pieces"),
        ("Cinnamon", 1, "inch"),
        ("Cloves", 4, "pieces"),
        ("Cardamom", 3, "pieces"),
        ("Cumin Seeds", 1, "tsp"),
        ("Saffron", 1, "pinch"),
        ("Lemon Juice", 1, "tbsp"),
        ("Oil", 4, "tbsp"),
        ("Ghee", 2, "tbsp"),
        ("Salt", 1.5, "tsp")
    ]),

    ("Mutton Biryani", "Non-Veg", [
        ("Basmati Rice", 2, "cups"),
        ("Mutton", 500, "grams"),
        ("Onion", 2, "pieces"),
        ("Tomato", 1, "piece"),
        ("Curd", 0.5, "cup"),
        ("Mint Leaves", 0.25, "cup"),
        ("Coriander Leaves", 0.25, "cup"),
        ("Green Chilli", 3, "pieces"),
        ("Ginger Garlic Paste", 2, "tbsp"),
        ("Biryani Masala", 2, "tsp"),
        ("Turmeric Powder", 0.5, "tsp"),
        ("Chilli Powder", 1, "tsp"),
        ("Garam Masala", 1, "tsp"),
        ("Bay Leaf", 2, "pieces"),
        ("Cinnamon", 1, "inch"),
        ("Cloves", 4, "pieces"),
        ("Cardamom", 3, "pieces"),
        ("Cumin Seeds", 1, "tsp"),
        ("Oil", 4, "tbsp"),
        ("Ghee", 2, "tbsp"),
        ("Lemon Juice", 1, "tbsp"),
        ("Salt", 1.5, "tsp")
    ]),

    ("Egg Biryani", "Non-Veg", [
        ("Basmati Rice", 2, "cups"),
        ("Eggs", 4, "pieces"),
        ("Onion", 2, "pieces"),
        ("Tomato", 2, "pieces"),
        ("Curd", 0.25, "cup"),
        ("Mint Leaves", 0.25, "cup"),
        ("Coriander Leaves", 0.25, "cup"),
        ("Green Chilli", 2, "pieces"),
        ("Ginger Garlic Paste", 1, "tbsp"),
        ("Biryani Masala", 2, "tsp"),
        ("Turmeric Powder", 0.5, "tsp"),
        ("Chilli Powder", 1, "tsp"),
        ("Garam Masala", 1, "tsp"),
        ("Cumin Seeds", 1, "tsp"),
        ("Bay Leaf", 1, "piece"),
        ("Oil", 3, "tbsp"),
        ("Salt", 1, "tsp")
    ]),

    ("Tomato Rice", "Veg", [
        ("Rice", 2, "cups"),
        ("Tomato", 3, "pieces"),
        ("Onion", 1, "piece"),
        ("Green Chilli", 2, "pieces"),
        ("Ginger", 1, "inch"),
        ("Garlic", 4, "cloves"),
        ("Mustard Seeds", 1, "tsp"),
        ("Cumin Seeds", 0.5, "tsp"),
        ("Curry Leaves", 10, "leaves"),
        ("Turmeric Powder", 0.5, "tsp"),
        ("Chilli Powder", 1, "tsp"),
        ("Coriander Leaves", 2, "tbsp"),
        ("Oil", 2, "tbsp"),
        ("Salt", 1, "tsp")
    ]),

    ("Lemon Rice", "Veg", [
        ("Rice", 2, "cups"),
        ("Lemon", 2, "pieces"),
        ("Peanuts", 0.25, "cup"),
        ("Mustard Seeds", 1, "tsp"),
        ("Urad Dal", 1, "tbsp"),
        ("Chana Dal", 1, "tbsp"),
        ("Green Chilli", 2, "pieces"),
        ("Curry Leaves", 10, "leaves"),
        ("Turmeric Powder", 0.5, "tsp"),
        ("Asafoetida", 1, "pinch"),
        ("Oil", 2, "tbsp"),
        ("Salt", 1, "tsp")
    ]),

    ("Curd Rice", "Veg", [
        ("Rice", 2, "cups"),
        ("Curd", 1.5, "cups"),
        ("Milk", 0.5, "cup"),
        ("Mustard Seeds", 1, "tsp"),
        ("Urad Dal", 1, "tsp"),
        ("Green Chilli", 1, "piece"),
        ("Ginger", 1, "inch"),
        ("Curry Leaves", 8, "leaves"),
        ("Coriander Leaves", 2, "tbsp"),
        ("Pomegranate", 0.25, "cup"),
        ("Oil", 1, "tbsp"),
        ("Salt", 1, "tsp")
    ]),

    ("Fried Rice", "Veg", [
        ("Rice", 2, "cups"),
        ("Carrot", 1, "piece"),
        ("Beans", 0.5, "cup"),
        ("Capsicum", 1, "piece"),
        ("Spring Onion", 0.5, "cup"),
        ("Cabbage", 0.5, "cup"),
        ("Garlic", 4, "cloves"),
        ("Soy Sauce", 1, "tbsp"),
        ("Vinegar", 1, "tsp"),
        ("Black Pepper", 0.5, "tsp"),
        ("Green Chilli", 1, "piece"),
        ("Oil", 2, "tbsp"),
        ("Salt", 1, "tsp")
    ]),

    ("Chicken Fried Rice", "Non-Veg", [
        ("Rice", 2, "cups"),
        ("Chicken", 200, "grams"),
        ("Eggs", 2, "pieces"),
        ("Carrot", 1, "piece"),
        ("Beans", 0.5, "cup"),
        ("Capsicum", 1, "piece"),
        ("Spring Onion", 0.5, "cup"),
        ("Garlic", 4, "cloves"),
        ("Soy Sauce", 1, "tbsp"),
        ("Vinegar", 1, "tsp"),
        ("Black Pepper", 0.5, "tsp"),
        ("Oil", 2, "tbsp"),
        ("Salt", 1, "tsp")
    ]),

    ("Veg Pulao", "Veg", [
        ("Basmati Rice", 2, "cups"),
        ("Carrot", 1, "piece"),
        ("Beans", 0.5, "cup"),
        ("Green Peas", 0.5, "cup"),
        ("Potato", 1, "piece"),
        ("Onion", 1, "piece"),
        ("Mint Leaves", 0.25, "cup"),
        ("Coriander Leaves", 2, "tbsp"),
        ("Green Chilli", 2, "pieces"),
        ("Ginger Garlic Paste", 1, "tbsp"),
        ("Cumin Seeds", 1, "tsp"),
        ("Bay Leaf", 1, "piece"),
        ("Garam Masala", 1, "tsp"),
        ("Oil", 2, "tbsp"),
        ("Salt", 1, "tsp")
    ]),

    ("Paneer Pulao", "Veg", [
        ("Rice", 2, "cups"),
        ("Paneer", 200, "grams"),
        ("Onion", 1, "piece"),
        ("Green Peas", 0.5, "cup"),
        ("Mint Leaves", 0.25, "cup"),
        ("Coriander Leaves", 2, "tbsp"),
        ("Green Chilli", 2, "pieces"),
        ("Ginger Garlic Paste", 1, "tbsp"),
        ("Cumin Seeds", 1, "tsp"),
        ("Garam Masala", 1, "tsp"),
        ("Cashews", 10, "pieces"),
        ("Ghee", 1, "tbsp"),
        ("Oil", 2, "tbsp"),
        ("Salt", 1, "tsp")
    ]),

    ("Tomato Pasta", "Veg", [
        ("Pasta", 200, "grams"),
        ("Tomato", 3, "pieces"),
        ("Onion", 1, "piece"),
        ("Garlic", 4, "cloves"),
        ("Cheese", 50, "grams"),
        ("Oregano", 1, "tsp"),
        ("Chilli Flakes", 0.5, "tsp"),
        ("Black Pepper", 0.5, "tsp"),
        ("Basil Leaves", 5, "leaves"),
        ("Olive Oil", 2, "tbsp"),
        ("Salt", 1, "tsp")
    ]),

    ("White Sauce Pasta", "Veg", [
        ("Pasta", 200, "grams"),
        ("Milk", 1, "cup"),
        ("Butter", 2, "tbsp"),
        ("Flour", 2, "tbsp"),
        ("Cheese", 50, "grams"),
        ("Garlic", 3, "cloves"),
        ("Oregano", 1, "tsp"),
        ("Black Pepper", 0.5, "tsp"),
        ("Nutmeg", 1, "pinch"),
        ("Chilli Flakes", 0.5, "tsp"),
        ("Salt", 1, "tsp")
    ]),

    ("Masala Dosa", "Veg", [
        ("Dosa Batter", 2, "cups"),
        ("Potato", 3, "pieces"),
        ("Onion", 1, "piece"),
        ("Mustard Seeds", 1, "tsp"),
        ("Urad Dal", 1, "tsp"),
        ("Chana Dal", 1, "tsp"),
        ("Curry Leaves", 10, "leaves"),
        ("Green Chilli", 2, "pieces"),
        ("Ginger", 1, "inch"),
        ("Turmeric Powder", 0.5, "tsp"),
        ("Coriander Leaves", 2, "tbsp"),
        ("Oil", 2, "tbsp"),
        ("Salt", 1, "tsp")
    ]),

    ("Idli", "Veg", [
        ("Idli Batter", 2, "cups"),
        ("Salt", 0.5, "tsp"),
        ("Oil", 1, "tsp")
    ]),

    ("Poori", "Veg", [
        ("Wheat Flour", 2, "cups"),
        ("Water", 0.75, "cup"),
        ("Oil", 2, "tbsp"),
        ("Salt", 0.5, "tsp"),
        ("Ajwain", 0.5, "tsp")
    ]),

    ("Chapati", "Veg", [
        ("Wheat Flour", 2, "cups"),
        ("Water", 0.75, "cup"),
        ("Salt", 0.5, "tsp"),
        ("Oil", 1, "tbsp")
    ]),

    ("Paneer Butter Masala", "Veg", [
        ("Paneer", 200, "grams"),
        ("Tomato", 3, "pieces"),
        ("Onion", 1, "piece"),
        ("Cashews", 10, "pieces"),
        ("Butter", 2, "tbsp"),
        ("Cream", 0.5, "cup"),
        ("Ginger Garlic Paste", 1, "tbsp"),
        ("Chilli Powder", 1, "tsp"),
        ("Turmeric Powder", 0.5, "tsp"),
        ("Coriander Powder", 1, "tsp"),
        ("Garam Masala", 1, "tsp"),
        ("Kasuri Methi", 1, "tsp"),
        ("Coriander Leaves", 2, "tbsp"),
        ("Salt", 1, "tsp")
    ]),

    ("Chicken Curry", "Non-Veg", [
        ("Chicken", 500, "grams"),
        ("Onion", 2, "pieces"),
        ("Tomato", 2, "pieces"),
        ("Ginger Garlic Paste", 2, "tbsp"),
        ("Green Chilli", 2, "pieces"),
        ("Turmeric Powder", 0.5, "tsp"),
        ("Chilli Powder", 1, "tsp"),
        ("Coriander Powder", 2, "tsp"),
        ("Garam Masala", 1, "tsp"),
        ("Cumin Seeds", 1, "tsp"),
        ("Curry Leaves", 10, "leaves"),
        ("Coriander Leaves", 2, "tbsp"),
        ("Oil", 3, "tbsp"),
        ("Salt", 1.5, "tsp")
    ]),

    ("Dal Rice", "Veg", [
        ("Rice", 2, "cups"),
        ("Toor Dal", 1, "cup"),
        ("Tomato", 1, "piece"),
        ("Onion", 1, "piece"),
        ("Garlic", 4, "cloves"),
        ("Green Chilli", 1, "piece"),
        ("Mustard Seeds", 1, "tsp"),
        ("Cumin Seeds", 1, "tsp"),
        ("Turmeric Powder", 0.5, "tsp"),
        ("Chilli Powder", 0.5, "tsp"),
        ("Curry Leaves", 8, "leaves"),
        ("Coriander Leaves", 2, "tbsp"),
        ("Ghee", 1, "tbsp"),
        ("Oil", 2, "tbsp"),
        ("Salt", 1, "tsp")
    ])
]


# Create database tables and insert recipes
def create_tables():

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            category TEXT NOT NULL,
            servings INTEGER NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ingredients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recipe_id INTEGER NOT NULL,
            ingredient_name TEXT NOT NULL,
            quantity REAL NOT NULL,
            unit TEXT NOT NULL,
            FOREIGN KEY(recipe_id) REFERENCES recipes(id)
        )
    """)

    # Insert recipes and their ingredients
    for name, category, ingredients in recipes_data:

        cursor.execute(
            "SELECT id FROM recipes WHERE name = ?",
            (name,)
        )

        existing = cursor.fetchone()

        if existing is None:

            cursor.execute("""
                INSERT INTO recipes (name, category, servings)
                VALUES (?, ?, 2)
            """, (name, category))

            recipe_id = cursor.lastrowid

            for ingredient in ingredients:

                cursor.execute("""
                    INSERT INTO ingredients
                    (recipe_id, ingredient_name, quantity, unit)
                    VALUES (?, ?, ?, ?)
                """, (recipe_id, *ingredient))

    conn.commit()

    total = cursor.execute(
        "SELECT COUNT(*) FROM recipes"
    ).fetchone()[0]

    print("Database:", DB_PATH)
    print("Total recipes:", total)

    conn.close()


# Home page
@app.route("/")
def home():

    conn = get_db()

    recipes = conn.execute(
        "SELECT * FROM recipes ORDER BY name"
    ).fetchall()

    conn.close()

    return render_template(
        "index.html",
        recipes=recipes
    )


# Calculate ingredient quantities
@app.route("/calculate", methods=["POST"])
def calculate():

    data = request.get_json(silent=True) or {}

    try:
        recipe_id = int(data.get("recipe_id"))
        servings = int(data.get("servings"))

        if not 1 <= servings <= 1000:
            raise ValueError

    except (ValueError, TypeError):
        return jsonify({
            "error": "Enter valid recipe and servings"
        }), 400

    conn = get_db()

    recipe = conn.execute(
        "SELECT * FROM recipes WHERE id = ?",
        (recipe_id,)
    ).fetchone()

    if recipe is None:
        conn.close()

        return jsonify({
            "error": "Recipe not found"
        }), 404

    ingredients = conn.execute(
        "SELECT * FROM ingredients WHERE recipe_id = ?",
        (recipe_id,)
    ).fetchall()

    result = []

    for item in ingredients:

        quantity = (
            item["quantity"] * servings / recipe["servings"]
        )

        result.append({
            "name": item["ingredient_name"],
            "quantity": round(quantity, 2),
            "unit": item["unit"]
        })

    conn.close()

    return jsonify({
        "recipe": recipe["name"],
        "category": recipe["category"],
        "servings": servings,
        "ingredients": result
    })


# Start Flask application
if __name__ == "__main__":

    print("Starting Recipe Quantity Calculator...")

    create_tables()

    print("Database initialized successfully!")
    print("Starting Flask server...")

    app.run(debug=True)
