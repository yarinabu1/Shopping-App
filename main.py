from fastapi import FastAPI

# Initialize FastAPI app
app = FastAPI()

# Define a sample route
@app.get("/")
async def read_root():
    return {"message": "Welcome to your shopping app!"}

# Example endpoint to get products (we'll add more here later)
@app.get("/products/")
async def get_products():
    # Placeholder logic for fetching products
    return {"data": "List of products will go here"}
