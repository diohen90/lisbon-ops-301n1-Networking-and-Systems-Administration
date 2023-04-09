#!/usr/bin/python3

import requests

# Prompt the user for the destination URL
url = input("Enter the destination URL: ")

# Prompt the user for the HTTP method
http_method = input("Select a HTTP method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ")

# Print the request to the screen and ask for confirmation
print(f"Sending {http_method} request to {url}")
confirm = input("Confirm the request (y/n): ")

if confirm.lower() != 'y':
    print("Request cancelled.")
else:
    # Perform the request using the requests library
    response = requests.request(http_method, url)
    
    # Translate the response codes to plain terms
    code_dict = {
        100: 'Continue',
        101: 'Switching Protocols',
        200: 'OK',
        201: 'Created',
        202: 'Accepted',
        203: 'Non-Authoritative Information',
        204: 'No Content',
        205: 'Reset Content',
        206: 'Partial Content',
        300: 'Multiple Choices',
        301: 'Moved Permanently',
        302: 'Found',
        303: 'See Other',
        304: 'Not Modified',
        305: 'Use Proxy',
        307: 'Temporary Redirect',
        400: 'Bad Request',
        401: 'Unauthorized',
        402: 'Payment Required',
        403: 'Forbidden',
        404: 'Not Found',
        405: 'Method Not Allowed',
        406: 'Not Acceptable',
        407: 'Proxy Authentication Required',
        408: 'Request Timeout',
        409: 'Conflict',
        410: 'Gone',
        411: 'Length Required',
        412: 'Precondition Failed',
        413: 'Request Entity Too Large',
        414: 'Request-URI Too Long',
        415: 'Unsupported Media Type',
        416: 'Requested Range Not Satisfiable',
        417: 'Expectation Failed',
        500: 'Internal Server Error',
        501: 'Not Implemented',
        502: 'Bad Gateway',
        503: 'Service Unavailable',
        504: 'Gateway Timeout',
        505: 'HTTP Version Not Supported'
    }
    
    # Print the response headers
    print("Response Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")
        
    # Translate the response code and print it to the screen
    response_code = response.status_code
    if response_code in code_dict:
        response_msg = code_dict[response_code]
    else:
        response_msg = "Unknown Code"
    print(f"Response Code: {response_code} ({response_msg})")
