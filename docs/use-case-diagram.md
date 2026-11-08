
# AIMS-mini — Use Case Diagram

## 1. Actor
- Customer: Người sử dụng hệ thống AIMS-mini.

## 2. Use Cases
- Add DVD to Cart
- Remove DVD from Cart
- View Cart
- Search DVD by Title
- Calculate Total Cost

## 3. Use Case Diagram

```mermaid
flowchart LR
    Customer[Customer]
    Add([Add DVD to Cart])
    Remove([Remove DVD from Cart])
    View([View Cart])
    Search([Search DVD by Title])
    Total([Calculate Total Cost])

    Customer --> Add
    Customer --> Remove
    Customer --> View
    Customer --> Search
    Customer --> Total
```
