# Refactoring Report

## Overview
This report outlines the refactoring process applied to the project. The original code was analyzed, and a refactored version was developed using 10 techniques from Refactoring Guru to improve code readability, maintainability, and testability. Each technique is justified below with applied changes and expected improvements.

---

## Applied Refactoring Techniques

### 1. **Extract Method**
- **Where:** `Order` class – the logic to compute total price was extracted.
- **Why:** To simplify and isolate the logic for reusability.
- **Benefit:** Improves readability and testability.

### 2. **Rename Method**
- **Where:** Changed `get_total()` to `calculate_total()` in `Order`.
- **Why:** To follow naming conventions and improve semantic clarity.
- **Benefit:** Easier for developers to understand purpose of method.

### 3. **Move Method**
- **Where:** Moved responsibility of attaching observer from `main.py` to `OrderObserver` constructor.
- **Why:** Respect SRP by encapsulating observer setup.
- **Benefit:** Clearer separation of concerns.

### 4. **Extract Class**
- **Where:** Separated `OrderDatabase` responsibilities from business logic.
- **Why:** To decouple logic and ensure single responsibility.
- **Benefit:** Improves maintainability.

### 5. **Encapsulate Field**
- **Where:** Converted `_dishes` in `Order` to use getter methods.
- **Why:** Prevents uncontrolled modification of internal state.
- **Benefit:** Encourages safe access patterns.

### 6. **Inline Variable**
- **Where:** Simplified temporary variable usage in price calculation.
- **Why:** Reduces unnecessary variables.
- **Benefit:** Shorter, cleaner code.

### 7. **Replace Magic Number with Symbolic Constant**
- **Where:** Default dish price replaced with constant `DEFAULT_DISH_PRICE = 0.0`.
- **Why:** Improves clarity of default behavior.
- **Benefit:** Easier to update and maintain.

### 8. **Introduce Parameter Object**
- **Where:** Introduced parameter object in order creation.
- **Why:** To simplify method signature and improve scalability.
- **Benefit:** Better code extensibility.

### 9. **Replace Constructor with Factory Method**
- **Where:** Order instantiation moved from `Order()` to `OrderFactory().create_order()`.
- **Why:** Better abstraction and flexibility in order creation.
- **Benefit:** Supports future extension (e.g., bulk orders).

### 10. **Replace Data Value with Object**
- **Where:** `Dish` class encapsulates name and price instead of using raw strings/floats.
- **Why:** Enables richer behavior and validation.
- **Benefit:** Increases object expressiveness.

---

## Summary of Improvements
- **Readability:** Improved method names, class responsibilities.
- **Maintainability:** Better modularization and separation of concerns.
- **Testability:** Simpler unit testing due to smaller, isolated methods.
- **Flexibility:** Easier to extend codebase due to cleaner abstractions.

---

## Future Work
- Apply Linter (e.g., Pylint) to maintain code style.
- Integrate static analysis (SonarQube).
- Extend to support multiple types of orders (bulk, scheduled).

---

Prepared by: [Your Name]  
Date: [Today’s Date]

