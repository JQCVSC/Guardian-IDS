GuardianIDS is a basic Intrusion Detection System that monitors network traffic and alerts on suspicious activities.

## Features

- Real-time packet capture and analysis
- Web interface for viewing alerts and statistics
- Docker support for easy deployment

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `sudo python app/main.py` (needs sudo for packet capture)

## Docker Setup

1. Build the Docker image: `docker build -t guardian-ids .`
2. Run the container: `docker run --net=host -it guardian-ids`

Note: The `--net=host` option is required for packet capture inside the container.

## Running Tests

Run the tests using the following command:
python -m unittest tests/test_packet_analyzer.py
Copy
## Security Considerations

This is a basic IDS for educational purposes. For production use, consider additional security measures and more sophisticated detection rules.
