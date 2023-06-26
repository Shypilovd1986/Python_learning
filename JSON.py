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

# JSON Schema is a standard for creating schemas for JSON data. It was created by the internet engineering task force.
# To create a schema using JSON Schema, you create JSON using a specific structure and keywords along with values you
# specify.

#                                            JSON SCHEMA
# The content of the schema is simply a set of keys and values, so a JavaScript object. By convention, I start with the
# dollar schema keyword as the first key. And this makes it clear that this object is a JSON schema, rather than just
# generic JSON. Remember that JSON requires key names as well as values to be double quoted.
# this is a special value that's defined in the JSON schema specification.
# productSchema = {
#     "$schema": "http://json-schema.org/draft-07/schema#",
#     "$id": "http://hplussport.com/schemas/product.json",
#     "title": "h+ Sport products",
#     "description": "schema for h+ sport product data",
#     "type": "array",
#     "items": {
#         "type": "object",
#         "properties": {
#             "id": {
#                 "type": "string"
#             },
#             "name": {
#                 "type": "string"
#             },
#             "description": {
#                 "type": "string"
#             }
#         },
#         "required": ["id", "name", "description"]
#     }
# }

# JSON-LD, which stands for JSON for linking data. JSON-LD follows the rules of JSON, but adds a couple standards to
# convey the meaning of content. First, it references common vocabularies that are maintained by a variety of
# organizations, including schema.org, productontology.org, and the W3C. Data built on the JSON-LD standard also
# implements key names based on vocabularies that are references. Together, these two JSON-LD features enable an
# application to parse data and make decisions about what it contains and how it should be used.

#
