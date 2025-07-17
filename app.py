# app.py (Simplified)
from flask import Flask, render_template, request, redirect, url_for, flash
from sweetshop import SweetShop

app = Flask(__name__)
app.secret_key = 'a_simple_secret_key_for_easy_mode' # CHANGE THIS FOR REAL APPS!

shop = SweetShop()

# --- Helper for Flash Messages ---
def show_message(message, category):
    flash(message, category)

# --- Routes ---

@app.route('/')
def index():
    try:
        sweets = shop.view_sweets()
    except ValueError:
        sweets = {} # No sweets available
    return render_template('index.html', sweets=sweets)

@app.route('/add', methods=['GET', 'POST'])
def add_sweet_page():
    if request.method == 'POST':
        try:
            sweet_id = request.form['id']
            name = request.form['name']
            category = request.form['category']
            price = float(request.form['price'])
            quantity = int(request.form['quantity'])

            sweet = {"id": sweet_id, "name": name, "category": category, "price": price, "quantity": quantity}
            shop.add_sweet(sweet)
            show_message(f"Sweet '{name}' added successfully!", 'success')
            return redirect(url_for('index'))
        except ValueError as e:
            show_message(f"Error: {e}. Please check inputs.", 'error')
        except Exception as e:
            show_message(f"An unexpected error occurred: {e}", 'error')
    return render_template('add_sweet.html')

@app.route('/delete/<sweet_id>', methods=['POST'])
def delete_sweet_action(sweet_id):
    try:
        shop.delete_sweet(sweet_id)
        show_message(f"Sweet with ID '{sweet_id}' deleted successfully!", 'success')
    except ValueError as e:
        show_message(f"Error deleting sweet: {e}", 'error')
    except Exception as e:
        show_message(f"An unexpected error occurred: {e}", 'error')
    return redirect(url_for('index'))

@app.route('/search', methods=['GET', 'POST'])
def search_sweets_page():
    results = {}
    if request.method == 'POST':
        search_type = request.form.get('search_type')
        query = request.form.get('query') # Generic query field

        try:
            if search_type == 'name':
                results = shop.search_sweets(name=query)
            elif search_type == 'category':
                results = shop.search_sweets(category=query)
            elif search_type == 'price_range':
                # For simplicity, assume query is "min-max" like "10-20"
                min_price, max_price = map(float, query.split('-'))
                results = shop.search_sweets(price_range=(min_price, max_price))
            else:
                show_message("Invalid search type.", 'error')
        except ValueError as e:
            show_message(f"Invalid input for search: {e}. Use 'min-max' for price range.", 'error')
        except Exception as e:
            show_message(f"An unexpected error occurred during search: {e}", 'error')
    return render_template('search_sweets.html', results=results)

@app.route('/purchase/<sweet_id>', methods=['GET', 'POST'])
def purchase_sweet_page(sweet_id):
    sweet = None
    try:
        sweet = shop.view_sweets().get(sweet_id)
        if not sweet:
            show_message("Sweet not found.", 'error')
            return redirect(url_for('index'))
    except ValueError: # No sweets in shop
        show_message("No sweets available to purchase.", 'error')
        return redirect(url_for('index'))

    if request.method == 'POST':
        try:
            quantity = int(request.form['quantity'])
            shop.purchase_sweet(sweet_id, quantity)
            show_message(f"Purchased {quantity} of {sweet['name']}!", 'success')
            return redirect(url_for('index'))
        except ValueError as e:
            show_message(f"Error purchasing: {e}", 'error')
        except Exception as e:
            show_message(f"An unexpected error occurred: {e}", 'error')
    return render_template('purchase_sweet.html', sweet=sweet)

@app.route('/restock/<sweet_id>', methods=['GET', 'POST'])
def restock_sweet_page(sweet_id):
    sweet = None
    try:
        sweet = shop.view_sweets().get(sweet_id)
        if not sweet:
            show_message("Sweet not found.", 'error')
            return redirect(url_for('index'))
    except ValueError: # No sweets in shop
        show_message("No sweets available to restock.", 'error')
        return redirect(url_for('index'))

    if request.method == 'POST':
        try:
            quantity = int(request.form['quantity'])
            shop.restock_sweet(sweet_id, quantity)
            show_message(f"Restocked {quantity} of {sweet['name']}!", 'success')
            return redirect(url_for('index'))
        except ValueError as e:
            show_message(f"Error restock: {e}", 'error')
        except Exception as e:
            show_message(f"An unexpected error occurred: {e}", 'error')
    return render_template('restock_sweet.html', sweet=sweet)

if __name__ == '__main__':
    app.run(debug=True)
