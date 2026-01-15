# Install fastapi
```cmd
pip install fastapi uvicorn
```

# Run
```cmd
set API_KEY=test-key
python app.py
```

# Test
```cmd
curl -i -H "X-API-Key: test-key" http://127.0.0.1:8000/protected
curl -i -H "X-API-Key: wrong-key" http://127.0.0.1:8000/protected
```

# Evaluate authorization key
```
HTTP/1.1 200 OK
{"secret":"ok"}
```

```
HTTP/1.1 401 Unauthorized
{"detail":"Invalid API key"}
```
