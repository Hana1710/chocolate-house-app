Chocolate House App

Welcome to the Chocolate House App! If you’ve ever dreamed of a place where seasonal chocolate flavors are created and shared, you’re in the right spot. This application is designed to manage our delightful chocolate offerings, keep track of ingredient inventories, and gather customer flavor suggestions—while also considering any allergy concerns.

What’s Inside?

- **Seasonal Flavor Offerings**: Discover new and exciting chocolate flavors based on the season!
- **Ingredient Inventory**: Stay updated on what’s in stock and what needs replenishing.
- **Customer Suggestions**: We value your input! Share your chocolate dreams and let us know about any allergies.

Getting Started

Requirements

Before you dive in, make sure you have the following:

- Python 3.9 or higher
- pip (Python package installer)

Installation Steps

1. Clone the Repository: Start by grabbing the code from GitHub bash
   git clone https://github.com/Hana1710/chocolate-house-app.git
   cd chocolate-house-app

2. Create a Virtual Environment (optional but highly recommended)
    python -m venv venv
     venv\Scripts\activate

3. Install the Required Packages:
    pip install -r requirements.txt

4. Initialize the Database
    python -c "from app import init_db; init_db()"

Running the Application
    python app.py

Testing the App
    pytest

Using Docker
    Build the Docker Image:
        docker build -t chocolatehouseapp .
    Run the Docker Container:
        docker run -p 5000:5000 chocolatehouseapp

