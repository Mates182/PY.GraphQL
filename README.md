# 🎥 Python GraphQL API

A GraphQL API built with Python using FastAPI and Strawberry to fetch details about movies.  

## 🚀 Getting Started  

### 🛠️ Clone the Repository  
```bash
git clone https://github.com/Mates182/PY.GraphQL
```
```bash
cd PY.GraphQL
```

### 🌟 Create a Virtual Environment  
- **For Windows**:  
  ```bash
  python -m venv tenv
  ```

- **For Mac/Linux**:  
  ```bash
  python3 -m venv tenv
  ```

### 🔑 Activate the Virtual Environment  

  ```bash
  source tenv/bin/activate
  ```

### 📦 Install Dependencies  
```bash
pip install -r requirements.txt
```

### ▶️ Run the Application  
```bash
python main.py
```

The API will be available at:  
- **Homepage**: [http://localhost:8000](http://localhost:8000)  
- **GraphQL Endpoint**: [http://localhost:8000/graphql](http://localhost:8000/graphql)  



## 🔍 Example Usage  

### Fetch All Movies  
You can test the GraphQL API via the `/graphql` endpoint. Use a query like the following:  

#### Query  
```graphql
{
  movies {
    title
    director
  }
}
```

#### Response  
```json
{
  "data": {
    "movies": [
      {
        "title": "The Silence of the Lambs",
        "director": "Jonathan Demme"
      },
      {
        "title": "Lady Snowblood",
        "director": "Toshiya Fujita"
      },
      {
        "title": "Pulp Fiction",
        "director": "Quentin Tarantino"
      },
      {
        "title": "Scarface",
        "director": "Brian De Palma"
      },
      {
        "title": "Fight Club",
        "director": "David Fincher"
      }
    ]
  }
}
```

### ⛔ Deactivate the Virtual Environment  
When done, you can deactivate the virtual environment:  
```bash
deactivate
```

## 📝 Additional Information  
- This API was created for learning purposes and demonstrates how to set up a GraphQL endpoint with Python.
