# 🐧 Linux System Monitor

A simple Flask web dashboard that shows live Linux system stats (CPU, memory, disk and uptime), packaged with Docker.

## Features

- CPU usage
- Memory usage
- Disk usage
- System uptime
- Runs in a Docker container
- Includes a standalone `monitor.sh` script for the terminal

## Tech Stack

- Python 3.12, Flask
- Docker, Docker Compose
- Bash

## Project Structure

```
linux-system-monitor/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── monitor.sh
├── README.md
└── .dockerignore
```

## Getting Started

### Prerequisites

- Docker (Docker Desktop with WSL integration on Windows)

### Run with Docker

```bash
docker build -t linux-system-monitor .
docker run -p 5000:5000 linux-system-monitor
```

### Run with Docker Compose

```bash
docker compose up -d --build
```

Then open **http://localhost:5000** in your browser.

To stop:

```bash
docker compose down
```

## Terminal Script

```bash
chmod +x monitor.sh
./monitor.sh
```

## Notes

- Stats shown are from the container's host Linux environment. On Windows with Docker Desktop, this is the Docker Linux VM, not the Windows host.
- The `procps` package is installed in the image because `top`, `free` and `uptime` are not included in `python:slim`.
- Flask's built-in server is used, which is fine for learning but not for production.

## Future Improvements

- Auto-refresh the dashboard
- Add charts for CPU and memory history
- Use `psutil` instead of shell commands

## Author

Manish Kumar
