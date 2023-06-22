#  Serializing JSON means turning a structure into a JSON string, while deserializing is the reverse, turning a JSON
#  string into a structure that a programming language can work with. Remember that even though JSON is based on the
#  object notation used in JavaScript, JSON can be used across languages and platforms.

# YAML Yet Another Markup Language
# XML Extensible Markup Language

# import json
# from json import JSONDecodeError

# try:
#     json.loads(JsonString)
# except JSONDecodeError:
#     print("Could not parse JSON")

#  JSON-P stands for JSON with padding. JSON-P is a technique for fetching data for a webpage that's intended to work
#  around some security limits that web browsers impose on web applications. One aspect of web security is based on
#  origins, which you can think of as the web addresses associated with particular web apps. Web browsers prevent
#  scripts from making requests to other origins. This is a same origin policy, and it's intended to prevent malware
#  from injecting a request to another domain that accesses a user' sensitive information, it's a useful limitation.
#  And on the modern web servers have many configuration options that enable them to work with selected other domains
#  they trust. But earlier in the web's evolution, this same origin policy was a blunt tool. JSON-P was developed as
#  a creative workaround. As part of the site's own code a statement is included that adds a script element to the page.
#
#And there are ways to accomplish everything that JSON-P can do while still maintaining security over all the data being
# transmitted. The most common approach is CORS which includes using the access control allow origin header within your
# HTTP requests and responses. For this reason it's best to you use these alternatives rather than relying on JSON-P.

