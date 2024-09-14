# Docker commands

## Overview

### Building a Docker Image

```bash
docker build -t my-docker-image .
```

### Running a Docker Container

```bash
docker run -d --name my-docker-container -p 8000:8000 -v .:/app my-docker-image
```

### Running a Docker Container from a Docker Compose file in detached mode

```bash
docker compose up -d
```
