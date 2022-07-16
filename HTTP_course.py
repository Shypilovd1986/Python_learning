#    a protocol is a system of rules that allow communication of information between different entities, like computers.
#      Hypertext is a somewhat outdated word for text that is displayed on a computer screen that contains hyperlinks to
# other text. So web documents.
# Get
# Post
# Put
# Delete
# Connect
# Head

# . When requests and responses are sent back and forth over HTTP, we can include HTTP headers with additional
# information. These headers can carry information about everything from what type of client sent the requests, the
# server configuration and the time and date of the response to how and for how long the client should store the data,
# what format the data is in, those cookies used to track sessions and so on. Which brings us to the last basic
# principle. HTTP works based on request/response pairs. Every action performed over HTTP starts with a request using
# one of the HTTP methods and ends with a response containing an HTTP status code saying what happened to the request
# along with the data like headers and content.

#       most important points are HTTP/2 is faster and more secure. It uses compression algorithms to speed up requests,
# allows for multi-plexing, meaning multiple files are sent over connection at the same time and requires an encrypted
# connection between the client and the server through HTTPS. By contrast, HTTP/1 sends uncompressed headers, transfers
# only one file at a time over a connection, and has no default encryption. What does all this mean? Well, in an ideal
# world, every HTTP transaction would be done over an encrypted HTTPS connection using the HTTP/2 protocol. In the real
# world, it means most HTTP transactions will use HTTPS over HTTP/2, and when that doesn't work, they'll fall back on
# unencrypted HTTP/1.1,

#                               shortened abrv
#    The browser is an application used to access and navigate between HTML documents, nothing more, nothing less.
#    A user agent is an application that is acting on behalf of the user, so a literal user agent. It is also commonly
# referred to as a client application. When we talk about HTTP, the user agent in question is whatever application is
# transporting information from the user to a server and back. That job typically falls to the browser, but it's not
# limited to the browser. It can also be middleware or a service like Google or even a server.
#    TCP is short for Transmission Control Protocol. It is one of the main internet protocols used by, among other
# things,the World Wide Web, email, FTPs, a file transfer protocol, and remote administration. When you connect to
# a service over the internet, you are probably using a TCP connection.
#   IP is short for Internet Protocol, the protocol used to actually transfer data between computers over a network.
# Each computer connected to the internet has a dedicated IP address which is used to connect to it.
#   The URL is quite literally a Universal Resource Locator, a universally understood address pointing at a resource
# somewhere on the web. URLs are human-readable addresses stored in Domain Name Servers and configured to point to the
#   IP addresses of web servers. When you type in a web address in the address bar of your browser, that address is
# automatically prefixed with either HTTP or HTTPS, telling you are using the Hypertext Transfer Protocol to access
# the resource at the other end of that universal locator.
#   A server is a computer on the internet running some form of data storage and sharing application, most commonly a
# web server application, allowing users to access its data through the HTTP protocol.
#   HTTP is a client server protocol, meaning the clients, or user agent, most commonly the browser, sends request to
# the server and the server serves responses back to the client.
#   A proxy is a service, either software or hardware, acting as a middle person between clients and servers. Proxies
# are often used when the IP address of a server needs to be hidden or when a server or client sits behind some sort
# of network barrier like a firewall. The proxy is quite literally a proxy handing data back and forth.
#   Clients and servers communicate over HTTP using request-response pairs.

#       If the client is trying to send information to the server, that information is also packaged in the request as a
#  payload. The response is the literal response to the request. It contains a status response code explaining what
#  happened, information about how the response was handled, and any data requested if the response was successful.
#  Requests and responses use HTTP headers to identify themselves and explain what they want. Every request and response
#  has a header and some also have payloads, the data that's transferred. The header contains metadata about the request
#  facilitating communication between clients and servers. The headers of an HTTP request always contain a request
#  method, or verb. These methods are words like get to get something, put to put something, update to update something,
#  delete to delete something, et cetera. The header of an HTTP response always contains a status response code.
#  These are numerical codes in the 100 to 500 range describing what type of response the client is receiving, 200 OK,
#  404 Not Found, 500 Server Error, et cetera. Web servers and clients can cache, so literally store data for a
#  specified length of time to speed up transfers and performance.

#     HTTP is a stateless protocol, meaning there is no link between two requests being sent between the client and the
#  server. When we need to create a stateful session, we can use cookies, small pieces of information passed back and
#  forth between the client and the server in the HTTP header to notify each party of the state the other is in.

#    This is the flow of all HTTP transactions.
#    First, the browser opens a TCP connection to the server. This ensures data can be sent back and forth over the
#    network and that the data sent from one end is put together the same way at the other end. If the connection
#    happens over HTTPS, TLS certificates are exchanged to ensure only the computer and the server can encrypt and
#    decrypt the transmitted data. This prevents anyone from being able to eavesdrop on the conversation between the
#    client and the server and steal the data they are transmitting. Second, the browser sends an HTTP message. This
#    message always contains an HTTP method, like GET, PUT, DELETE or something similar, and a URL pointing at the
#    requested resource. It can also contain headers like cookies or authentication data and data if the browser is
#    submitting data to the server using the post, put, or path methods. Third, the server performs the requested
#    actions and sends a response back to the browser. This response will contain an HTTP status message indicating what
#    happened, headers with information about the response, and whatever data was requested. This data could be an HTML
#    document or a style sheet or a JavaScript file or image or any other type of content used in a standard website.
#    Finally, once the response is fully received, the TCP connection is closed. Since HTTP is stateless, we are now
#    back to a clean slate.

#    A URL is a human-readable address, describing exactly where on the web and in what location on a server the
# information you are requesting is located.

#  The URL has two main pieces, a protocol declaration, and a Universal Resource Name, or URN. This URN provides the
#  location of the resource. The protocol declaration states how we are accessing that resource using the http methods
#  and transport layer. The URN itself is made up of several pieces. First, we have the host. This is the domain which
#  is registered at a domain name service, or DNS. And this domain points to a dedicated server IP address, somewhere
#  on the web. Next, we have the implied, and usually invisible, connection port, stating which port we want to access
#  on the server. For http connections, the default port is 80. For https connections, the default port is 443. As long
#  as the server uses either of these ports, we don't see the port declared. If the server uses another port or we want
#  to access another port, say 8080, that port can be declared using a colon, localhost:8080. After the host and port
#  comes the resource path. This is the file location within the server. The default names for web documents are
# index.html and default.html, or just htm, or something like that. If we request a folder without a file specification,
# the server and browser automatically look for files named either index.html or default.html or index.php or similar
# and returns that file to us. If the file is called anything else, like about.html or contact.php, etc., the resource
# path needs to list the filename specifically, so mysite.com/folder/about.html. Finally, we have the optional URL
# query. This is one or more queries added to the end of the resource path that can perform further actions on the
# server.

# URN  uniform resource name
# URL queries start with a question mark and then each query comprises an argument and a value like ?u=1234.

#               HTTP methods
#  Every request sent over the HTTP protocol includes a method, aka a verb. This method tells the server what type of
#  action we want to perform with the request. There are a limited set of these methods available and some are more
#  used than others. For standard web transactions, we typically only use three. GET, POST, and DELETE. But these are
#  not the only methods available to use. Each of the HTTP methods has it's own request response pair and some require
#  more information than others to work.

#  Get request - get the specified resources if available
# Success  - 200 Ok,
# Failure 404 Not Found, 405 Not Allowed, 403 Forbidden

#  To send data from the client to the server, we have three different methods to perform different types of actions.
#  POST, PUT, and PATCH. POST is the most common of these methods, as it is the one useD when you submit a form on a
#  webpage. A POST request asks the server to create a new resource and give it an ID for future retrieval. Because POST
#  requests make changes to the server, they typically need an authorization header. A successful POST request returns
#  a 201 Created HTTP status along with a link to the new resource ID and the response header. If the resource already
#  exists, the server returns a 409 Conflict status and if the resource is sent to a resource that can't create new
#  resources then you get a 404 Not Found HTTP status in return. PUT is used to update an existing resource by replacing
#  some or all of its contents with the contents of the request. Like POST, PUT typically requires an authorization
#  header. Unlike POST, which just contains the contents, a PUT request contains the ID of a resource and the new
#  content to be added to that resource. If the resource already exists, the existing content is replaced with the
#  contents in the PUT request. If no resource with this ID exists, the server will in some cases allow the new resource
#  to be created with the user defined ID or you'll get an error message. A successful PUT request returns a 200 OK
#  status. If there is no content on the server, a 204 No Content status is returned. If the ID doesn't match an
#  existing resource, a 404 Not Found status is returned. If a PUT request is sent to a resource that can't be updated,
#  a 405 Method Not Allowed status is returned. PATCH is used to modify an existing resource. Where PUT updates the
#  resource by replacing content, Patch can carry along instructions on how to modify the existing resource without
#  necessarily replacing data. PATCH also typically requires an authorization header and returns the same status as PUT.
#  DELETE does exactly what it sounds like. It deletes a specified resource. A DELETE request must contain the ID for
#  the resource and an authorization header. If you try to delete a resource you are not allowed to delete, you'll get
#  a 405 Method Not Allowed status. What actually happens on the server when you send a DELETE request varies from
#  server to server. In some cases you delete a database entry. In other cases, you change the status of a database
#  entry without actually removing content. It all depends on the design of the system you're interacting with. In
#  addition to these content methods, HTTP also has three methods to get information from the server without really
#  touching the content. They are HEAD, which returns just the HEAD section of the response, OPTIONS which returns a
#  description of the communication options for the target resource, and TRACE, which creates a loop back of the request
#  message effectively telling the client where the request ended up.

# - Anytime you send an HTTP request to a server, you'll get a response, even if the response is that something went
# wrong. This response starts with an HTTP status code, explaining what happened on the server and how your request was
# handled. The client can use these status codes to identify successes and failures and automatically respond with next
# steps. The HTTP response status codes are split into five main groupings. 100, 200, 300, 400, and 500 codes. Status
# codes of the 100 format are informational and rarely encountered. They're used to inform the client of the status of
# the server, typically 102 Processing, which tells the client to wait for the server to finish. Or 100 Continue, which
# simply tells the client the server has received the request headers, and is ready for the rest of the request body.
# This last one is typically encountered when sending POST requests with a large data body. Status codes of the 200
# format are success messages. Here you find common codes including, 200 OK, which means the request was successful,
# 201 Created which means the request was successful and a new resource was created. And 204 No Content, meaning the
# server processed the request, but returned no content. Status codes of the 300 format indicate redirection. The
# clienis provided with a new URL to follow to get to the requested resource. These codes include 301 Moved Permanently,
# which tells the client, "Use this new URI for all future requests." 302 Found which technically means "resource
# temporarily redirected to this other URI" but is most often used to mean "the response to this resource is actually
# found at this other URI," which is the real job of 303 See Other. Just to confuse things, there's also 307 for
# Temporary Redirects, and 308 for Permanent Redirects because reasons. Status codes for the 400 format signal client
# errors. Here you'll find 400 Bad Request, meaning the request is mal-formed or too large or something else.
# 401 Unauthorized meaning the client lacks proper authentication to access the resource. 403 Forbidden meaning the
# request is refused by the server, typically because the client is not logged in, or does not have the correct
# permissions. And the well-known 404 Not Found which means the resource doesn't exist. You can also encounter 405
# Method Not Allowed, which kicks in if you try to use an HTTP verb like "POST" on a resource that can only receive
# "GET" requests. And they're also a myriad of other error messages under this 400 heading. The last group, status
# codes of the 500 format, signal server errors. Here we have 500 Internal Error meaning something went wrong on the
# server. 502 Bad Gateway meaning the serve acts as a literal gateway or proxy and received an invalid response from
# wherever it was trying to connect to. And the fairly common 503 Service Unavailable, which is encountered when a
# server is overloaded or temporarily unavailable, or something else goes wrong. There are more HTTP status messages,
# but these are the ones you're most likely to encounter when working with regular websites.

# f a server wants, or needs, the client to remember where it has been or what state it is in, like what movie the
# client is currently watching in this course, it can use a set cookie header, to give the client a cookie, a small
# piece of data. The next time the client visits the server, it sends the cookie back, and the server brings the client
# to the right state. Cookies like this are used everywhere on the web.

#  If you need to send custom request headers to a server to test the response, you can do so using a REST client.
# REST, or representational state transfer, is a set of rules that describe how data is transferred and managed between
# clients and servers. All you need to know here is that the entire web is a giant RESTful API, and you can use a REST
# client to interface with it.

#  My browser sends a get request along with a series of headers to the server in the hopes of a return. This is what
#  that full request header looks like and this is how one computer talks to another to make sure the communication
#  between them is crystal clear. First, the client states what method it's using get and what resource it's requesting
#  using a regular URL. As you learned earlier, that URL contains the protocol declaration, in this case HTTPS and the
#  URN, which is the address to the resource. Next, the client adds in a user-agent header to identify itself, lists out
#  what file types, language types and encoding types it accepts, tells the server where it came from, using the refer
#  header, tells it to keep the connection alive for future requests and sets the cache-control of the current file to
#  zero seconds, meaning it will not be saved when it arrives. Just a side note, that user-agent header you see here is
#  how the server and any scripts on the website knows what browser is being used. This is also how some browsers
#  pretend to be other browsers to get around browser-sniffing scripts targeting specific browsers to block content or
#  do other strange things. In addition to this header, the HTTP request can contain a payload of data. Things like form
#  submissions or upload media files. All of this info is passed on to the server via HTTP and the browser waits
#  patiently for a response.

#  If there is a server at the requested address specified in the request header, that server will return a response
#  even if that response is simply not found. In our example, the request is successful and we get a more comprehensive
#  response header. This response header declares the status of the response 200 OK, the server type, the date and time
#  of the response message, the content type of the return data, and other information. What you see here is just the
#  response headers in addition comes the entire payload which in this case is html document. The client in our case,
#  the Firefox browser, receives this header and processes whatever data is returned in the payload according to the
#  header content. In this example that is to render the content of the return of the html document.

#