from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("."))

def add_hearts(text):
    return f"aaaaaaaaa {text} aaaaaaaaaa"

env.filters["add_hearts"] = add_hearts
template = env.get_template("email.template.txt")

data = {
    "name": "Bruno",
    "products": [
        {"name": "iphone", "price": 13000.320},
        {"name": "ferrari", "price": 900000.430},
    ],
    "special_customer": True
}

print(template.render(**data))