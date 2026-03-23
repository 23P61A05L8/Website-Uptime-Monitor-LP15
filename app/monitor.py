import requests
import time
import socket
import ssl

def check_website(url):
    result = {
        "url": url,
        "status": "UP",
        "response_time": None,
        "error": None
    }

    try:
        start = time.time()
        response = requests.get(url, timeout=5)
        result["response_time"] = round(time.time() - start, 2)

        if response.status_code >= 500:
            result["status"] = "DOWN"
            result["error"] = "SERVER_ERROR"

    except requests.exceptions.SSLError:
        result["status"] = "DOWN"
        result["error"] = "SSL_ERROR"

    except requests.exceptions.ConnectionError:
        result["status"] = "DOWN"
        result["error"] = "DNS_OR_CONNECTION_ERROR"

    except requests.exceptions.Timeout:
        result["status"] = "DOWN"
        result["error"] = "TIMEOUT"

    return result