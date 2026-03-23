def get_root_cause_hint(error):
    if error is None:
        return "Website is healthy and reachable."

    hints = {
        "DNS_OR_CONNECTION_ERROR": "Domain not reachable or DNS issue. Check domain name and DNS records.",
        "SSL_ERROR": "SSL certificate issue. Check expiry or certificate validity.",
        "TIMEOUT": "Server is slow or overloaded.",
        "SERVER_ERROR": "Website server is down or crashing (5xx error).",
    }
    return hints.get(error, "Unknown issue. Check server logs.")