# first we have to decide what functionality we want to expose.
# Then we have to determine how to expose it.
# Then you have to figure out the best ways to expose it.
# Then you have to adjust and improve as you figure out your assumptions and use cases were wrong, or just sometimes
# incomplete. Finally, as you learn about your customers and unexpected use cases, you have to rethink some things from
# the ground up. Overall, it touches on some of the hardest problems in computer science.

# . The challenge is that good API design involves naming things well, while simultaneously describing how to interact
# with those things. Even worse, as the API sees the real world, the goals and the purpose of the API will evolve. This
# may require us to find better words to describe our efforts and adjust accordingly, which gets in to versioning and
# backwards compatibility. All of this brings us to the first concept we'll cover, affordances. In the simplest terms,
# an affordance is something which allows you to perform an action or accomplish a goal.

#      The potential risk is that we have three different aspects in play.
#   First, we have what the API allows you to do.
#   Second, we have what the API makes easy.
#   Finally, we have what you want to do, the user, what do you want to accomplish?
#   When these three things don't fit, we may have a useless API or maybe a powerful API that doesn't do what we need.
#   But when all three of these are aligned, we have a unique combination that's incredibly powerful, but so subtle you
#   don't even notice.

#                               Approaches to adding an API
#           There are three approaches that allow you to add an API to your system. Some are easier than others.
#   First, we have the bolt-on strategy. This is when you have an existing application and add an API after the fact.
# This is often considered a brute-force approach, but is the fastest way to get value from the API since the underlying
# system is functional the whole time. This takes advantage of existing code and systems so you don't have to re-figure
# out anything. Unfortunately, there are some drawbacks. Poor architectural decisions and bad name decisions made years
# ago tend to seep through the system and cause problems in external interfaces with helper libraries and all the
# supporting client code in every single piece. As a result, these oddities never go away.

#                               the Greenfield strategy.
# This is when there's no underlying application or even necessarily business logic that you have to interact with. You
# have complete freedom and flexibility to do whatever you want and however you want to do it. This is the strategy
# behind the API first or mobile-first approach and is the easiest scenario to develop an API. This offers us the
# opportunity that other strategies don't. Since you're starting from scratch, you can make use of technologies and
# concepts that may not have been available before. This can reinvigorate your team to learn new things and expand their
# skills. This also tends to be the hardest option because there's a biggest gap between when the requirements are
# defined and when you actually receive real business value from the system.

#                               the facade strategy,
# and this is actually my recommended approach, most of the time. It's somewhere between the
# Greenfield and the bolt-on. In this case, you take advantage of existing business systems, yet shape them to what you
# prefer and need. I'm working with a number of companies where we're doing this right now. They have a huge number of
# soap services that power their backend and they're wrapping each of these with services with re-architected REST
# interfaces. This gives them the ability to keep working systems in place while making the underlying architecture
# better. Now the drawback for that is if you're not careful, this can be a place where you have naming translation and
# conversion layers that easily get out of control. In some cases, you can end up with completely divergent mindsets in
# the system, which can make it look schizophrenic for people who can see both systems.

#  Regardless of which of the API strategies you follow, modeling will be a key to our success.
#  Toward that goal, before we get into the technical side of the process, I want to lay out three simple rules.
# -First, don't worry about the tools. It doesn't matter if you're using note cards, post-it notes, or the latest Kanban
#  tool, just choose a tool that works best for your process.
# -the key aspect is having a consistent process. If you always document things the same way and using the same steps,
# you can reduce the likelihood that things are missed, ideas are misunderstood, or requirements are incomplete. If you
# don't document these, you stand the risk of losing them, potentially even putting your entire project at risk.
#
#                                           Identifying participants
#  The first thing we need to do is have a clear understanding of our business process. (process, goals, requirements)
#  If we don't know what that is and what it accomplishes, we'll never be able to build an API to support it. This is
#  the process we're going to be stepping through. And notice,

# **********************       API modeling process          ******************

# Step 1 - identify participants
# Step 2 - identify activities
# Step 3 - break into steps
# Step 4 - create API definitions
# Step 5 - validate API

#  Step 1 is identifying the participants. To put it simply, our participants are the ones who will be involved in the
#  business process that eventually uses our API. Actually, let me rephrase that. Our participants are the entities who
#  will be involved in the business process using the API.  Our first step of this is to figure out who is involved in
#  our business process.  For each participant we need to capture who they are. I go as far as giving them a name. So
#  we're not just talking about a developer, but developer Dan or developer Diane. Next, we need to know if they're
#  internal or external to our organization. Getting adoption of our API is probably easy if we're building it for
#  another team at our company.  Finally, we need to know whether they're active, taking an action, or passive, waiting
#  for an action.

# Step 2 identify activities ,we should instead define the business processes or goal involved. Our overarching activity
# is simple. We're ordering a cup of coffee. Now what are the steps in our activity? First, you place an order. Then you
# wait for the order. Finally, you receive the order.
#  let's just consider the happy path for version one. Let's assume that everything is working out the way we hope. I'd
#  recommend flagging all these branches, all these choices and assumptions that we're making and talk to our product
#  owner as soon as possible to see if they're a priority. Do not guess here. I really recommend going back to the
#  product owner, because for all you know, there are other teams working on those issues already and there have already
#  been decisions made.
#
# Step 3. creating and grouping API methods or more properly creating our API definitions.

# HTTP
# POST GET PUT DELETE
# GET. GET is used to retrieve data. You should never use it to modify information. Not surprisingly,
# DELETE is used to delete data. You should not use it for anything else. Next, we have PUT.
# PUT will update an existing record. You should not use it to create or delete or anything else.
# POST. POST is the catch-all for HTTP. You can use it to create new records and basically anything else that modifies
# a record but doesn't directly map into one of the other verbs. This kind of makes it an odd ball but it's really
# important to remember.

#  viewing an order is pretty easily a GET.
#  So we POST to create a new cart. Then we use PUT to put items into the cart to modify the attributes about it.
# . And then finally, we have the check out process. The check out process we're assuming is a post because it doesn't
# map cleanly into any of the other verbs.

# ************       There's three particular types of relationships that we're interested in.       ***************
# The first type of relationship is independent. It means that this resource can exist on its own.

# The second type of relationship is dependent, which means one resource can only exist if a different resource already
# exists. To look back at our ordering book scenario, a order cannot exist without a cart previously existing.

# And then finally, we have the third type of relationship and this is associative. This means that additional
# information is required to describe the relationship.
#
# . And alternatively, and probably my favorite approach is to use a microframework. You can use something like hapi.js
# in Node or Slim in PHP to accept incoming requests, validate the corresponding verbs and URL patterns, and return
# static HTTP response codes and payloads. In most cases, as long as you're familiar with your framework, you should be
# able to implement the basic API calls in a manner of hours to a few days. In my opinion, this is the absolute best
# approach because as we build the real functionality of our API, we can plug it into this framework and eventually
# watch things come alive together.

#  The final and most common approach for validating the API is by documentation. In this case, we want to write the
#  documentation as if the API already existed. That means we need to describe the end points, list out the individual
#  parameters, include the response codes and how you get each, and show the individual fields which are returned in the
#  API. Our goal here is to write documentation that we can hand to other teams and have them accomplish their goals
#  with our API.

# HTTP is a protocol. XML is a markup language. JSON is a notation. There are XML standards that can add structure and
# meaning to it. And there are JSON specifications that can add context and descriptions to that. Unfortunately, REST is
# none of the above. It's not a standard. It's not a specification and it's not a protocol. In fact, there are all kinds
# of debates about what is RESTful, RESTish, all the variations of that. While there are specifications for things like
# URLs and XML and JSON and HTTP, there are very few formal requirements for REST itself.

#  SOAP, or the previous way of designing APIs, is a lot like getting a mortgage. There's a very fixed process. It's a
#  very detailed process with numerous instructions throughout. There's a ton of documentation upfront to tell you about
#  every step of the process. There's detailed scenarios. If this happens, then do that. And there's complex error
#  handling. If something doesn't happen the right way, there's a detailed process for resolving that as quickly and
#  easily as possible.

#  REST is like borrowing money from a friend for lunch. There's very few requirements. They have to have enough trust
#  that you're going to compensate them, that you're going to return that in some way. There's no documentation at the
#  beginning. As you learn more about the interaction, you learn how to improve it next time around. Most importantly,
#  it's flexible based on the needs of both you and the other party. This flexibility is great. It gives you the
# opportunity to maybe buy them lunch tomorrow, to return the money, to give them a gift. There's a variety of different
# options. Unfortunately, this introduces ambiguity. This ambiguity has to be figured out and resolved, which brings us
# back to HTTP.

#  HTTP is a well understood protocol that is both simple and powerful in its implementation. Every HTTP request and
# response has two parts. There are the headers and the payload. The payload is the HTML, the JSON, the XML, or whatever
# comes back that you can view, interact with and process. If it's just HTML, it's usually presented to the user on the
# screen.

#   **************            HTTP header and response codes      *****************

# sudo apt install curl        install curl on ubuntu
# curl is a command-line tool to transfer data to or from a server, using any of the supported protocols (HTTP, FTP,
# IMAP, POP3, SCP, SFTP, SMTP, TFTP, TELNET, LDAP, or FILE). curl is powered by Libcurl. This tool is preferred for
# automation since it is designed to work without user interaction. curl can transfer multiple files at once.
# Syntax:
#
# curl [options] [URL...]
# URL: The most basic use of curl is typing the command followed by the URL.
#
# curl https://www.geeksforgeeks.org
# This should display the content of the URL on the terminal. The URL syntax is protocol dependent and multiple URLs can
# be written as sets like:
#
# curl http://site.{one, two, three}.com
# URLs with numeric sequence series can be written as:
#
# curl ftp://ftp.example.com/file[1-20].jpeg
# Progress Meter: curl displays a progress meter during use to indicate the transfer rate, amount of data transferred,
# time left, etc.
#
# curl -# -O ftp://ftp.example.com/file.zip
# curl --silent ftp://ftp.example.com/file.zip
# If you like a progress bar instead of a meter, you can use the -# option as in the example above, or –silent if you
# want to disable it completely.

#                   HTTP Response Codes 2xx
# 200 Ok    Request was successful
# 201 Created      resource was created
# 202 Accepted Action has started
# 204 No content  Delete a resource

#  The first one we have that we just saw with the GitHub API is '200 OK'. Because it starts with a '2', it means the
#  request was successful. There are other codes that begin with a '2' that also means success, but are more specific.
#  We may also run into the '201 Created'. This is used to signify that a resource has been successfully created. For
#  example, earlier, when we are creating a shopping cart, we might return back a '201'. The next up is '202 Accepted'.
# This is used to identify that the action you just performed is underway, but it's not complete yet. The '202' is often
# used with systems that use some sort of queuing or other asynchronous process behind the scenes, or the work is
# started, or it will be started, but it's not done yet. Finally, there's the '204 No Content', which is primarily used
# when you delete a resource. Because after all, if you just deleted resources, you can't just show it now.

#                    HTTP Response Codes  30x
# The next series is the '300' series. These are pretty simple and are used when a resource moves from its original URL.
# There are more than two, but these are the ones we care about.

# '301 Moved Permanently', as in the thing you're looking for is no longer available here, it's now over in a different
# URL. And most responsible APIs will then give you the URL to then go retrieve it. And the other one is

# '302 Move Temporarily'. This works exactly the same way, but instead of keeping that new URL indefinitely, you may
# want to check back occasionally to see if the old one is available now.

#                    HTTP Response Codes  40x
# 400   bad request
# 401 authentication
# 403 forbidden
# 404 not found

#  your API can be incredibly descriptive with just a bites. The first error code or the '400' denotes the client that
#  the most recent attempt failed due to the client itself. While this is a perfectly valid code to use, I recommend
#  being more specific whenever possible. One way to get more specific is with a '401'.

#  The '401 Authentication Required Error' says authentication is required. It doesn't signify whether the operation
#  would have worked or not. Simply that authentication is required before you can do anything else. Next, we have the

#  '403', which is almost the exact opposite. In this case, the user was authenticated, the request was understood, but
#  they explicitly failed. You might see this if you attempt to delete a resource with incorrect permissions. Finally,
#  we run it to the commonly seen

#  '404 Response Code'. This signifies that whatever resource you are looking for was not  found. It doesn't mean it did
#  exist and you didn't find it. It means it does not exist.

# 100-199   Informational
# 200-299   Success
# 300-399   Redirect
# 400-499   Client error
# 500 599   Server error

# . All of the '200' mean success. All of the '300' mean redirect. All the '400' means the client had an error as in you
# interacting with the API had an error. The '500' series means the server itself or the API has an error. From a
# developer's point of view, there's absolutely nothing you can do to fix a '500' error. That's entirely on the server
# side. And the one we skipped was a '100' series. While they're available, you're unlikely to see them in the world. As
# you build your API, you may want to create additional response codes to be more specific to your errors or even your
# industry. Don't, response codes work so well because they're standard across all industries and widely understood.

#  The next header we want to look at is the content type. You can see that on the third line here. This simply
#  identifies the type of payload being provided by the server. For normal web browsing, it'll normally be text HTML,
#  but for APIs, we'll normally see application JSON and potentially text XML.

#  If we want to understand how it's structured, we need to look at the media type. In this case, 'X-GitHub-Media-Type.
#  Media types are specifically named and structured payloads that allow a client to be customized to handle them. In
#  this case, the 'X-GitHub-Media-Type' tells us that it's the GitHub media type version three. There are specifications
#  for media types that are under active development.

#  **************        REST APIs: Constraints       **************

#  REST is not a formal specification or standard itself, but it often uses some standards and some principles or
#  constraints.
#  The six constraints serve to establish the expectations and create some structure and patterns around the flexibility
# of REST These are not hard and fast rules, which should be considered guidelines and best practices for implementation

#    The first constraint is that an API should be designed for a client-server architecture. This is the internet, so
# that shouldn't be too surprising. The single biggest benefit to the setup is that it allows us to vary the
# implementation details, upgrade paths, and scalability of each independently of the other.
#
#       The second constraint, that's that the API should be stateless. This allows each and every request to stand on
# its own and be processed or rejected independently of any other request in any order that they're received.
# The ability to process requests independently of each other allows us to isolate request failures and still continue
# and scale our systems better. Specifically, this gives us the ability to add more servers when our API is successful
# and as we get more users. We don't have to worry about shared sessions, sticky sessions, other complexity that comes
# through a shared state.

#        The third constraint is cacheability, or how to detect if a request response pair can be cached. It requires
# that each message describes if it can be cached and for how long. The biggest benefit of caching is to improve network
# performance and application usage overall, by reducing or in some cases eliminating requests. After all, the fastest
# request is the one you don't have to perform.

#        the first three build into the fourth constraint, and this is a layered system. Basically it means that your
# client should not be built on the assumption that it's communicating directly with the server. There can and  often
# will be additional layers between the client and the server itself. Those layers can be caching and a variety of other
# components.  We do this on the web every day when we have web servers talk to database servers.
# Either way, you've broken things by depending on the network configuration instead of using something as simple as DNS
# By not counting on the client interacting directly with the server, we can insert components and even entire
# subsystems between the two without disrupting the flow or the application itself. This architecture gives us the
# ability to add things like logging, access control, and caching to the system without architecting them in on day one.
# The API management companies like Apigee and MuleSoft and many others take advantage of this aspect, to insert logging
# access control, and even load balancing between you and the actual API. Basically, layers give us flexibility to
# improve and evolve our system as our requirements and our architecture changes.
#
#  The fifth constraint is optional, but probably the most powerful. It's the concept of code on demand. The concept is
#  that when a client requests a resource, it also receives the code to act upon it. The real power is that the client
#  doesn't have to know what is in the code. It just has to understand how to execute the code. The primary benefit is
#  that the API can grow and extend itself without requiring the client applications to upgrade. We can get this new
#  functionality for free. At first glance, executing arbitrary third-party code sounds like a security nightmare, and
#  it could be, but can you think of anywhere on the web or anywhere in your application that's already doing this? Most
#  of the internet does this with JavaScript. When you load an application such as Gmail in your browser, it also
#  retrieves the JavaScript required to interact with that page. Your browser doesn't even need to know what's in the
#  JavaScript. It just needs to know how to execute it.

#      the final and probably the most important constraint of all, uniform interfaces. There are four key principles
# that make up a uniform interface. First, there's the concept of identifying our resources. Each resource should
# be uniquely addressable by a particular URL. Generally, there will be one and only one way to access this resource,
# but that is not a hard requirement. Think of the buildings on your street. They're also uniquely addressable. That's
# how they get mail. Next, you need to be able to manipulate or interact with those resources through those
# representations, through those URLs. Every interaction with a given resource should happen through the identifier we
# already gave it. It's worth noting that this isn't just adding an ID parameter at the end of the URL, but having the
# ID as part of the URL. It's a subtle but important distinction. The next principle of uniform interfaces is a concept
# of self-descriptive messages. We've already seen this a little bit with caching, but this is important because by
# making the messages standalone with their own processing and caching information, we can create and use different
# types of messages very simply. Our client only needs to know how to retrieve and execute those instructions like the
# JavaScript code on demand that we already covered. The final principle of uniform interfaces is called hypermedia as
# the engine of application state, also known as HATEOAS or HATEOAS, which is the worst name for a children's breakfast
# cereal ever.

#  At every point in the API, there are different things you can do with the API. And instead of having to go to the
#  documentation to figure out what's available, each and every link is available within the API.

#  Our client application doesn't have to remember how to create the user URL. It can simply ask the API for the URL
#  that is based on this name. If you think about it, that's how humans work too. We don't remember what the logon URLs
#  is for amazon.com. Instead, we go to amazon.com and we skim the page until we see a button labeled sign-in, login, or
#  something similar. APIs can work exactly the same way. Also, we don't have to memorize the link to get to the book
#  section of the site. Again, we visit the web page and skim for a link labeled books.

#  When our client applications don't have to remember the specific URLs for each and every action or link we want to
#  visit, our clients can be simpler, kind of dumber, and as a result, much more flexible. More importantly, as your API
#  adds additional functionality, you can just add it and our clients can update automatically.

# ************         Authentication and authorization         *************
# authn     Authentication
# authz     authorization

#  Authentication is establishing who you are. You do this every time you use a website with a username and password.

#  it's important to verify what you're allowed to do, or your authorization. Most people confuse the two, and they
#  design permission systems based on every user having one specific set of permissions.

# ********************      authorization  factors     ******************
# who you are               customer, employee
# your group membership     admin, teller, VIP
# subscription lvl          free, paid
# context                   time location device
# actions attempted         bulk unusual regular
#
# First, we have an API key. This is a long string issued by the API provider and either appended to the URL or included
# as a header in the request. This is by far the simplest and easiest way to deal with from any programming language,
# framework, or even curl on the command line. There are two downsides we have to consider though. First, if we include
# this key in the URL, it's convenient, but it's going to be captured and logged by every cache, router, and device
# between us and the API itself.  This is not secure. If we move the key to the headers, that's much better, but we're
# still stuck with the problem that this key can't be rotated easily if it's compromised. We may have to update all of
# our applications, which may require redeployment in a variety of different places.

#  The final and the most common of the API authentication approaches is OAuth. OAuth is actually an authorization
#  protocol. It doesn't define how you authenticate, just that you must authenticate with a trusted entity. The access
#  token you get back describes or internally maps to a description of what actions you are and are not allowed to do.
#  That's where the authorization comes in. At this point, OAuth 2.0 is the recommended approach for APIs. It's not
#  always well understood, but it's widely established and used by your favorite APIs. There's a massive ecosystem of
#  tools, libraries, documentation, and even training options around it.

# **************************        API versioning best practices       **************************

#  There are two primary schools of thought here, versioning in the URL or versioning via the accept header. First,
#  let's look at the accept header. When you make a request to an API, you should have the accept header, which tells
#  the API these are the data types and the formats I understand, please send one of them. This is called content
#  negotiation. At the first level, the data types could be as simple as XML versus JSON. That's where most APIs will
#  begin and end, and that's acceptable as long as you can parse the result. At the next level, that data type could be
#  a specific type or structure of JSON, or a media type.

#  the second form of versioning, in the URL. When you look at the URL of one of these requests we know exactly what
#  the developer's asking for and expecting, we can copy and paste the URL. And even if someone forgets to include the
#  headers, there's no question or additional effort required to figure out what data is involved. In practical terms,
#  this may look like a V1 in the URL, or even something like this from the Twilio API. The 2010-04-01 portion of the
#  URL is the version.

# ********************      Choosing media types and processing content         ***********************
#
#  In most cases, people will say, JSON and name value pairs are fine, and not worry about anything else. And I admit,
#  that the flat key value pair structure is incredibly easy to consume. The drawbacks are that it becomes harder to
#  extend and almost impossible to add detail about the data. Remember from earlier, one of the rest constraints is
#  uniform interfaces. And within that, our messages should be self descriptive. Therefore, we should do something more
#  expressive than simple JSON. So, let's talk media types. A media type allows us to use a commonly structured JSON
#  file to move data back and forth. The biggest benefit here, is that there's a growing ecosystem and usage patterns
#  around each of these formats. None of them have a huge following yet, but there are libraries, active discussions and
#  examples using all of them. Let's walk through three of the more popular media types, so you can start to understand
#  the trade-offs.

#  First, we have collection JSON from Mike Amundsen. This is designed specifically to handle, read, write operations,
#  to query a set of objects and manipulate them. This is what a typical collection JSON payload looks like. We have an
#  array of items here, data about those items and links to additional references on those items. While this is not
#  explicitly designed to represent a single item, it can, by rendering it as a collection of one. If you have a lot of
#  group operations, this may be an ideal media type for you. But usually it's not used alone.
#
#  Second, we have HAL, a hypertext application language, which is my favorite media type. It breaks the data payload
#  into two pieces. First, it represents the data structure of the resource that we're working with. Second, it has an
#  underscore links section, which then gives us references to other related resources and how to interact with those.
#  It's simple but effective.

#  Finally, we have the Ion Hypermedia Type. As a disclosure, this is led by a colleague of mine from my day job. And I
# have not personally used it in production like the other two, so feel free to be as critical as you like. This is what
# Ion looks like. While Ion feels similar to HAL, the big difference is that the context and the descriptive information
# are not separate from the data that it describes. Unlike HAL with a link section, the additional information is
# adjacent to the data. In terms of processing, this is likely a marginal improvement. But in terms of understanding,
# I think this is much better. That said, it's one of the new media types, so the community around it doesn't have the
# same tooling integrations, et cetera

# *******************       Hypermedia approaches       ********************

#  Hypermedia is a combination of two concepts, hyper and media. Let's explore the media part of that first.
# .The hyper part of hypermedia means that the media isn't linear. For a sporting event, you watch it beginning, middle,
# and end. And it doesn't have meaning in really any other order. Combine these concepts together, and you have the
# modern web experience.

# *******************     Advanced HTTP headers: Content negotiation and caching       *************

#  And then again in relation to versioning, but let's stop and really consider two more aspects, content negotiation,
#  and caching. First, content negotiation is the idea that an HTTP client, whether it's a browser or an application,
#  can make request to the server and together they can find a format they can both understand.

#  The best part of this content negotiation is that this happens implicitly behind the scenes as you navigate the web.
#  As we're building APIs, we need to be aware that that's happening and sometimes even do it ourselves. Luckily, there
#  are libraries and tools to help with that. The final header concept I want to cover is caching. Caching is vitally
#  important on the internet in general, and within your API specifically. Remember the fastest request you ever have to
#  handle is the one you don't have to. The specific header used here is ETag, which is generated by the server and
#  returned to the client. This is how it works. A client makes a request just like normal. The server generates the
#  response and generates an Etag to go along with it. Quite often, this is just a hash of the response. Now, before
#  the client makes its next request, it uses the head verb to just get the headers, including the ETag. If the data is
#  the same, the server returns the same ETag. The client recognizes this and the request is complete.

# . While this may initially seem like a lot of extra effort, you just reduced the work from retrieving and parsing the
# entire payload into a few dozen bites and zero work for the server. That's a win overall. Now, alternatively, if the
# data has changed, the server returns a new ETag, the client recognizes this, and then it makes a full request as
# expected. Now, in this path, you suffered a small delay in terms of the extra request, but for some data sets, you'll
# make that up in bandwidth and time-savings over and over again. If you're building mobile applications with
# potentially unstable connection, this is even more important.

# *******************           Documentation approaches          **************

#                 Documentation Don'ts
# Don't distribute PDF
# Don't use WordPress or other basic CMS
#
# What are our goals for our documentation? First, whatever tool we use needs to be code snippet friendly. These are API
# docs. They will have code and it must be simple and easy to copy/paste and experiment with the code. Syntax hiding is
# absolutely mandatory. Next, we need version control. This is helpful to our users, which I already noted, but it's
# also important to our team. As things change, improve, or expand, we need to put the same rigor into our documentation
# review as we do for our code reviews. If your API is revenue generating, remember that mistakes here will cost you
# money. Next, we need something that's easy to update. While some documentation writers are comfortable in an IDE or
# even just Vim, not all of them will be. We absolutely need things to be as simple and straightforward for them as
# possible. Finally, it needs to be searchable, not only internally on the site, but Google needs to be able to crawl it
# too. This is a core requirement for me personally, because of it's not findable it does not exist. Thinking about
# tools, a Wiki is actually a strong option here. Whether you're looking at MediaWiki, Confluence or something else
# entirely, most have syntax highlighting built in, or as a simple plugin. Obviously, since it's a Wiki, version control
# is built in, so that's covered. Even better, the skills required to maintain the site are very minimal. Overall, it's
# very good. In fact, search friendliness is very high for MediaWiki. For Confluence, we have to be a little bit more
# careful to make sure that this is an internal or an external site. The only real downside of a Wiki is that there
# usually isn't a staging or a review workflow. When you're launching a new component of your API, there's not an easy
# way to say don't publish this page or section, or even, just show it to these people for review.

#  But right now my favorite tool is called Slate. It recently spun off the company TripIt. It's Jekyll based, so you
#  have all the benefits as before, and some of the cons also, but they made some significant structural improvements.
#  First, they've made it very easy to configure and deploy. It can be done usually in under five minutes. Next, they've
#  added some simple JavaScript plugins and CSS to add tabbing for different programming languages and examples. So as
#  a result, you can have one text description and then display different snippets of different languages right there in
#  context with the text, and then you can toggle between them. More subtly, this is also done via URL in the
#  documentation, so you link someone directly to the Java or the PHP or the Golang example that they need. And just
#  remember that our goal here is that we want people to be successful with our API. That means that they can find what
#  they need, that it makes sense, and that it's complete and accurate.

# *****************         SDK design considerations           **************

#  The philosophy goes something like this. You shouldn't need an SDK or helper library to use your API. If you use the
#  HTTP verbs, and response codes properly, you use JSON for your payloads, and the common authentication method, a
#  simple HTTP library, and JSON parsing libraries should be enough.

#    While I'd love to go with that, most of us are doing something a little bit more complex with our API. In fact, if
# you're doing something more complex or you need to wrap larger components, workflows or advanced concepts, an SDK
# might make sense, but I don't recommend SDKs for everyone. You should only have an SDK if you can make your users
# lives easier in some tangible way. I use the acronym SPOIL to remember that we want to spoil our users with a great
# experience.

# S  -   succinct, "Concise but precise."  We want people using our SDK to write less code to accomplish the right thing
# P  -   purposeful,  We should do the same for our helper library because the SDK will be the primary interface for
# many of our users. In fact, we should make sure it helps them with the most common, and important scenarios, not just
# a simple wrapper over our API.
# O  -  it needs to be open-source. Odds are your SDK won't quite do everything that
# everyone needs all the time. By being open-source, people can pass back extensions, fixes, and clever ideas that you
# can accept or reject as appropriate.
# I  -  idiomatic or reflecting the language it was written in. That means a PHP SDK should have naming conventions,
# structures and patterns common to PHP. It shouldn't look and feel like Java. And finally,
# L  - logical. The SDK should be logical. That means understanding gained, and patterns used in one component should be
# reusable across all others. The more time and energy people have to spend to understand your code is less time they
# can spend solving their problem. This is also called the principle of least surprise.
#
# We want to surprise people in the smallest ways possible. All of this comes back to our goal. We want to make our
# users' lives easier in some tangible way. If providing an SDK can let them move faster, easier, or we can wrap complex
# concepts of workflows, we should definitely consider it. And the final thing to remember, before you start building
# SDKs, and your favorite languages, ask your existing users which ones they need? You could build the perfect react
# library, but if nobody uses it, what was the point? Your time would have been better spent elsewhere or sometimes the
# other side of it is even worse. You build a library that one tiny but vocal customer needs, and no one else cares
# about. Be very careful about the libraries you choose to build and support.