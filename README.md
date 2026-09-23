# Application for Mathematical Modeling of HIV and Human Immune System Interaction

## Running without Docker

### Running the backend

1. Clone the project

2. ```bash
   cd backend
   ```
3. Create a virtual environment
```bash
    python -m venv venv
   ```
4. Install dependencies
```bash
    pip install -r requirements.txt
   ```
5. Start the server
```bash
   uvicorn app.api:app --reload --port 8000
```

### Running the frontend

1. ```bash
   cd frontend

2. Install dependencies
    ```bash
   cd frontend
   npm install
    ```
3. Start the dev server
    ```bash
   npm run dev
   ```

### Subsequent launches
```bash
cd frontend ; npm run dev 
```
```bash
 cd backend;  uvicorn app.api:app --reload --port 8000;
```

The frontend will start at: http://127.0.0.1:5173 (but it's better to check the port in the console, it might be 5174, 5175)