"""File to handle all inventory related works."""

import json
from datetime import datetime
from typing import Dict, List, Optional


# Global variable (module-level state kept simple for this exercise)
stock_data: Dict[str, int] = {}


def add_item(item: object = "default", qty: object = 0, logs: Optional[List[str]] = None) -> None:
    """Add `qty` amount of `item` to the inventory and append a log entry."""
    if logs is None:
        logs = []

    if not item:
        return

    # Normalize types and validate
    name = str(item)
    try:
        quantity = int(qty)
    except (TypeError, ValueError) as exc:
        raise ValueError("qty must be an integer or convertible to int") from exc

    if quantity == 0:
        # nothing to do
        return

    stock_data[name] = stock_data.get(name, 0) + quantity
    logs.append(f"{datetime.now()}: Added {quantity} of {name}")


def remove_item(item: object, qty: object) -> None:
    """Remove `qty` amount of `item` from the inventory."""
    name = str(item)
    try:
        quantity = int(qty)
    except (TypeError, ValueError) as exc:
        raise ValueError("qty must be an integer or convertible to int") from exc

    try:
        current = stock_data[name]
    except KeyError as exc:
        # Item not present: give a clear message rather than silently ignoring.
        raise KeyError(f"Item '{name}' not found in inventory") from exc

    if quantity <= 0:
        raise ValueError("Quantity to remove must be positive")

    if quantity >= current:
        del stock_data[name]
    else:
        stock_data[name] = current - quantity


def get_qty(item: object) -> int:
    """Return the quantity available for `item`. Returns 0 if not present."""
    return stock_data.get(str(item), 0)


def load_data(file: str = "inventory.json") -> Dict[str, int]:
    """Load inventory from a JSON file and return it."""
    try:
        with open(file, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as exc:
        raise ValueError(f"Failed to parse JSON inventory file: {exc}") from exc

    if not isinstance(data, dict):
        raise ValueError("Inventory file must contain a JSON object mapping names to integers")

    normalized: Dict[str, int] = {}
    for k, v in data.items():
        try:
            normalized[str(k)] = int(v)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"Invalid quantity for item {k}: {v}") from exc

    return normalized


def save_data(file: str = "inventory.json", data: Optional[Dict[str, int]] = None) -> None:
    """Save the provided inventory mapping to a JSON file using UTF-8 encoding."""
    if data is None:
        data = stock_data
    with open(file, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, sort_keys=True)


def print_data() -> None:
    """Print the item quantities in a human-readable format."""
    if not stock_data:
        print("Inventory is empty.")
        return

    print(f"{'Item':<20}{'Quantity':>10}")
    print("-" * 30)
    for name, qty in sorted(stock_data.items()):
        print(f"{name:<20}{qty:>10}")


def check_low_items(threshold: int = 5) -> List[str]:
    """Return a list of item names whose quantity is strictly less than threshold."""
    if threshold < 0:
        raise ValueError("Threshold must be non-negative")
    return [name for name, qty in stock_data.items() if qty < threshold]


def main() -> None:
    """Main function to demonstrate basic inventory operations cleanly."""
    # Use a local logs list to demonstrate add_item logging behavior.
    logs: List[str] = []

    # Add some items
    try:
        add_item("apple", 10, logs)
    except ValueError as exc:
        print("Error adding apple:", exc)

    # Demonstrate adding a negative quantity
    # If you want to disallow negative adds, add validation in add_item.
    try:
        add_item("banana", -2, logs)
    except ValueError as exc:
        print("Error adding banana:", exc)

    # Demonstrate invalid input handling: this will raise, so we catch and print it.
    try:
        add_item(123, "ten", logs)
    except ValueError as exc:
        print("Error adding invalid item:", exc)

    # Remove items (with error handling)
    try:
        remove_item("apple", 3)
    except (KeyError, ValueError) as exc:
        print("Error removing apple:", exc)

    try:
        remove_item("orange", 1)
    except KeyError as exc:
        print("Warning:", exc)

    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())

    # Save current inventory to file
    # inside main()
    try:
        save_data("inventory.json")
    except (OSError, TypeError) as exc:
        print("Failed to save data:", exc)

    # Load inventory from file and update module-level state (replace safely)
    try:
        loaded = load_data("inventory.json")
        stock_data.clear()
        stock_data.update(loaded)
    except ValueError as exc:
        print("Failed to load data:", exc)

    print_data()

    # Show logs if any
    if logs:
        print("\nOperation logs:")
        for entry in logs:
            print(entry)


if __name__ == "__main__":
    main()
