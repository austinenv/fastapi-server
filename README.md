### Build the image
```
docker build -t fastapi-image .
```

### Start the Container
```
docker run -d --name fastapi-container -p 80:80
```