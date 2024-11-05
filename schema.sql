CREATE TABLE SeasonalFlavors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    available BOOLEAN DEFAULT 1
);

CREATE TABLE Ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    stock INTEGER DEFAULT 0
);

CREATE TABLE CustomerSuggestions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    flavor_name TEXT NOT NULL,
    allergy_warning TEXT
);
