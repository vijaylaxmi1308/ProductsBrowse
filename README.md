# Product Browser Backend

## Overview

This project is a backend application built using FastAPI to browse a large product catalog of approximately 200,000 products.

## Tech Stack

* FastAPI
* SQLAlchemy
* PostgreSQL (Neon)
* SQLite
* Render
* Faker

## Features

* Browse products
* Newest products first
* Filter products by category
* Cursor-based pagination
* Generated dataset of approximately 200,000 products

## Database Schema

### Product Table

| Column     | Type                  |
| ---------- | --------------------- |
| id         | Integer (Primary Key) |
| name       | String                |
| category   | String                |
| price      | Float                 |
| created_at | DateTime              |
| updated_at | DateTime              |

### Sample Record

{
"id": 1,
"name": "Wireless Mouse",
"category": "Electronics",
"price": 799.99,
"created_at": "2026-06-23T17:12:57.411399",
"updated_at": "2026-06-23T17:12:57.411399"
}

## Running the Project

Install dependencies:

pip install -r requirements.txt

Start the server:

uvicorn main:app --reload

Open:

http://127.0.0.1:8000/docs

## API Endpoints

### Get Products

GET /products

After Executing it Returns the first 20 products sorted by newest first.

### Filter by Category

GET /products?category=Books

Returns only products belonging to the specified category.

### Pagination

The response contains a `next_cursor` value.

Use it to fetch the next page:

GET /products?cursor=<next_cursor>

Example:

GET /products?cursor=2026-06-23T17:12:57.411399

### Category + Pagination

GET /products?category=Books&cursor=<next_cursor>

## Design Decisions

Products are sorted by created_at in descending order so that the newest products appear first.

Cursor pagination is used instead of offset pagination because it prevents duplicate and missing records when new products are added while users are browsing.

## Future Improvements

* Composite cursor using (created_at, id)
* Automated testing
* Improved error handling
