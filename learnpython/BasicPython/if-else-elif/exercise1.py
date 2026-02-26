def translate_error_code(error):
    if error == "404":
        showText = "404 Not found, The web pages that you searched is not found"
    elif error == "401":
        showText = "401 Unauthorized, Server received an unauthenticated request"
    elif error == "408":
        showText = "408 Request timeout, server request to close unused connection"
    else:
        showText = "unknown error!!"  
        
    return showText

print(translate_error_code("401"))




