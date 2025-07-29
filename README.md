### 🥗 Populating the Food Database with Sample Data

To quickly add initial food entries to your database without manually using the admin panel or writing migration scripts, you can insert them directly via the Django shell.

#### 🔧 Steps to Add Sample Food Data:

1. **Open the Django Shell**:

```bash
python manage.py shell
```

2. **Paste the following Python code into the shell**:

```python
from myapp.models import Food 

foods = [
    {"name": "Egg, raw (medium 44gm)", "carbs": 0.3, "protein": 6.0, "fats": 4.2, "calories": 63},
    {"name": "Chicken breast, cooked (100g)", "carbs": 0.0, "protein": 31.0, "fats": 3.6, "calories": 165},
    {"name": "Rice, white, cooked (100g)", "carbs": 28.0, "protein": 2.7, "fats": 0.3, "calories": 130},
    {"name": "Broccoli, boiled (100g)", "carbs": 7.0, "protein": 2.8, "fats": 0.4, "calories": 35},
    {"name": "Olive oil (1 tbsp)", "carbs": 0.0, "protein": 0.0, "fats": 14.0, "calories": 119},
    {"name": "Banana (medium, 118g)", "carbs": 27.0, "protein": 1.3, "fats": 0.3, "calories": 105},
    {"name": "Almonds (28g, ~23 almonds)", "carbs": 6.1, "protein": 6.0, "fats": 14.0, "calories": 164},
    {"name": "Whole milk (1 cup, 244g)", "carbs": 12.0, "protein": 8.0, "fats": 8.0, "calories": 149},
    {"name": "Apple (medium, 182g)", "carbs": 25.0, "protein": 0.5, "fats": 0.3, "calories": 95},
    {"name": "Oats, cooked (100g)", "carbs": 12.0, "protein": 2.4, "fats": 1.4, "calories": 71},
]

for food in foods:
    Food.objects.get_or_create(**food)
```

This script uses `get_or_create` to prevent duplicate entries if you run it more than once.

---

### 📌 Notes:

* These nutritional values are approximate and based on standard sources like USDA and NutritionData.
* You can add more food entries by appending to the `foods` list in the same format.
* Ideal for development, testing, or creating a demo environment.

