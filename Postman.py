#      Postman is a sort of graphical version of the cURL command line utility. cURL provides a rich structure for
# controlling most aspects of individual http requests. By comparison, Postman gives us a convenient graphical interface
# for issuing http requests against a website or API.

#    It truly is an API development environment. Like cURL, we use Postman to test our APIs in that we can construct
# requests, issue them, inspect results, and iterate as necessary. Postman is so similar to cURL that it even provides
# mechanisms for translating requests between the respective formats. As an API development environment, Postman allows
# us to save and organize requests, switch between environments, use variables to substitute information, and even
# collaborate with our team.

#     To add an account, open the profile menu and select the Add a New Account option. This is useful for keeping your
#  projects separated in the way best suited to your needs. For instance, if you're a consultant working for multiple
#  clients, using multiple accounts may be preferable to creating multiple workspaces within a single account.

#     Postman follows a fairly typical layout for desktop applications in that it's divided into four main areas: the
# header, the sidebar, the footer, and the request builder. Each area controls different aspects of Postman's behavior
# and how we interact with our API's.

#    The header, or main tool bar, contains controls for creating items, importing data, changing workspaces, inviting
#  other people to collaborate, accessing Postman settings, and managing your user profile.  In the middle of the header
# is a button that lets us manage our workspaces. This comes in handy when working on multiple projects or with multiple
# teams, since it provides a convenient way to surface only the requests you care about at the moment.

#   Most of the options in the drop-down are rather standard, but pay attention to the option labeled Trash. When you're
#   signed in with a Postman account, Postman keeps a copy of everything on it's servers. The Trash option gives you a
#   convenient way to recover any collections you may have accidentally deleted. Free accounts retain deleted
#   collections for a day, but upgraded accounts can retain the items for much longer. Now let's look at the footer.
#   Postman's footer provides easy access to several interesting features, including toggling the sidebar visibility,
#   rich searching capabilities within the workspace, the Postman debugging console, additional learning resources and
#   API development guides, toggling between build and browse modes, toggling between horizontal and vertical views, a
#   listing of keyboard shortcuts, and Postman documentation and other resources.

#    The sidebar on the left is divided into two tabs as well as a filter box. The first tab, History, shows us a log of
#  the requests we've made in Postman under the current workspace. This is useful for inspecting the requests you've
#  previously sent. We haven't made any requests yet so the history tab is empty. If we had any requests, they would be
#  organized in reverse chronological order and grouped by day. By default, Postman won't save the responses with the
#  requests in the request history but if you toggle the Save Responses setting here Postman will also capture the
#  responses so we can revisit them later or even compare responses for different requests.

#    The other tab, Collections, shows us a list of the collections, folders and requests defined in the workspace.

#    if you need more control over the search, be sure to try out the Find panel in the footer.
#   And finally, we reached the request builder. This is the area where you'll spend most of you time in Postman. The
#   request builder is further divided into two sections. On the top is where compose our requests. This is where we
#   control all aspects of crafting requests including the URL, the HTTP method, the authorization method, the request
#   body and much more. The bottom panel is where we inspect responses. The data presented here will include the
#   response status code, time, size, cookies, body and headers. We'll be touching on nearly every area in this section
#   throughout the rest of the course. So, let's leave it at that for now. Postman provides an alternative view for the
#   request builder. If a side-by-side view is more to your liking, you can toggle that on by clicking the Two Pane View
#   button in the footer. I generally find the default view most comfortable, so I'll switch back to that.

#  At a high level it is divided into four areas. Tickets which represent to do items, boards which provide a mechanism
#  for grouping tickets, users to manage boards and tickets, and authentication to establish user context.

# cURL is a command line utility useful for testing APIs
# npm nodejs package manager

# npm i        to make sure all of the dependencies are installed.

# npm run start-mac      or start-win if you are on windows machine
#
#     One of Postman's primary purposes is allowing us to craft requests to the APIs we use. Be they APIs we're actively
#  developing or third party APIs we need to consume.

# . We'll begin by entering the base URL. Our server is running locally, and listening on port 3,000 so we'll enter
# HTTP local host 3,000. (keys clacking) The base URL alone isn't enough. We also need to provide a route. Everything
# in the sample API is routed under the slash API route, so let's append slash API to the end of the URL. We also need
# to specify the HTTP method for the request. When you click the dropdown arrow, you can see a list of methods available
# for your request. The list includes standard methods like get, post, put, and delete. But also several additional
# verbs used by some APIs.

# http://localhost:3000/api

# cmd + enter    is equal press button send
#  Alternatively, we can click the dropdown arrow attached to the send button, and choose send and download. This
#  alternative provides a convenient way to immediately save any response to a file, which can be handy when trying to
#  capture a data set for later use.

#  The response body is presented under the body tab. There are three views for the response body. Pretty, raw, and
#  preview. Pretty tries to apply basic formatting to the content when that content has a known structure. Raw shows
#  the content exactly as it was received. And preview attempts to render the content. Preview is most useful when you
#  want to get an idea of what an HTML document would look like in the browser. Note that when the response is an image
#  or other non-text type, these options won't be available. Postman will simply attempt to render the content instead.
#  When the pretty option is selected, the dropdown list next to the three display options let's us select the content
#  type.

#  Postman can also display cookies returned from the server, and the full list of response headers.

#  we can also see the response status code, request time, and response size. In this case, the server responded with
#  status 200 indicating the request was successful. It took 12 milliseconds, and contains 296 bytes.

# cmd t    to create new request in postman


#                                   Manage query string parameters

# . Google for instance, appends our basic search terms to URL as the q parameter, along with some other parameters it
# uses to track how you're using the search.
#
#  Let's experiment with those parameters and observe how we can manage them. The first way to manage query string
#  parameters is to just append them to the URL. Since the JSON return shows only four items, we need to use a low
#  number. I'll be using one. The query string parameter for setting the page size is ps. Append that to the URL using
#  the standard format of question mark, ps, gets one. and send the request again.
# http://localhost:3000/api/boards/?ps=1

# Fortunately, you don't have to remember how to encode them, because Postman provides an easy way to do it through a
# context menu option. For instance, if I enter something silly, like, param, it's This & That, I'd need to encode this.
# I can select the This & That part, open the context menu, and choose the EncodeURIComponent. This replaces any of
# those characters with the appropriate character sequence. Conversely, choosing the DecodeURIComponent reverses the
# operation, and returns the unencoded string. What's really nice about these options is that they're available
# virtually everywhere throughout Postman, so you can use them whenever you need.

#  let's see how to manage multiple parameters within the editor. Just as we used the ps parameter to control the page
#  size, we can use the pn parameter to specify the page number. So add a new parameter in the editor, click on the Key
#  cell, and enter pn. We'll get page three, so tab or click over to the Value cell, and enter three. Notice how the URL
#  updated to reflect the new parameter. Now send the request with both parameters and observe the result.

#  Next, the key-value editor allows us to toggle parameters on or off, but still keep them associated with the request.
#  This is in contrast to editing the URL, which would remove them entirely.

# . The final way to manage query string parameters, is through the bulk editor. Click the Bulk Edit button on the right
# to see this applied to our two existing parameters. Like the key-value editor, the bulk editor lets us manage query
# string parameters for a request, but instead of a grid, it uses a JavaScript-like syntax where items are separated by
# new lines, and keys and values are separated by colons.

#                               Manage cookies
# I'll edit the lang cookie. In the editor you can control all aspects of the cookie including its name, value, path,
# domain, and expiration time. For fun, let's see what happens when we change the lang value. In the editor, find the
# string en-us. Replace it with es-mx. This will instruct LinkedIn to serve the Mexican Spanish version of the page.

#                               Manage request headers

#       Postman included a default User Agent header value that identifies it as PostmanRuntime/7.6.0. The second line
#  Accept is */* which indicates that Postman is willing to accept the response in whatever format the server deems
#  appropriate.

#  Similarly, we can control which format the server responds with, by specifying the Accept Header. The sample API can
#  respond to these status requests in plain text, HTML, and JSON formats. We've already seen that it responds in plain
#  text by default, so let's see what the JSON response looks like. First, add a new key, Accept, to the list. Then,
#  enter application/json for the value. Notice how Postman also provides guidance here by listing common content types.
#  Finally, send the request and observe the response. You'll see that the system has provided the same data, just in
#  a different format. Like the Query String Parameters Editor, we can check and uncheck boxes next to each header key
#  value pair to control whether the corresponding header is included with the request.

#                               Manage header presets
#  You can also select the preset from the presets menu. I generally take this approach only when I can't remember
#  the preset name. Most of the time I find typing it to be much faster. Sending the request now will result in the
#  response containing our custom user-agent string in JSON format. One important aspect to note here is that the values
#  from the preset are copied into the request, rather than merged. This has a few implications. One is that applying a
#  preset can result in duplicate headers, since existing headers are not replaced. The other is that any subsequent
#  changes to the preset will not be reflected in the request that it was applied to.

#                               Build a request body

#    Query string parameters, headers, and cookies are some of the ways that we can send data to an API, but we'll often
# find ourselves needing to send data via a request body as well. Let's look at building a request body to get specific
# results from our sample API.
#      To include a request body, we must also change the HTTP Method from GET to one that allows a body. In this case,
# the API specifies that we use POST. So just as the response body, we've seen so far, contains the response body, the
# request body tab is where we enter the request body. So click over to the request body tab. You'll see that the body
# is currently set to none. To provide a request body, we need to select the format that the server expects. Different
# APIs have different requirements. For instance, a simple email form or file upload might expect data as form fields.
# In those cases, we need to select the form data option. Our API doesn't use this approach but let's look at the
# options anyway. The form data editor should be very familiar by this point. One interesting difference for the form
# data grid is that when we add an item to the grid, we're asked to choose what type of data we're sending. By default,
# the text option is selected so we can enter some text in the value column But when we select the file option instead,
# something interesting happens. See how the value column changed and now includes a select file button? This provides
# us with an easy way to select a file to send to the server. This might be useful for user profile images or something
# like that.
#        Instead of form data, we'll be sending JSON data describing our search options. For that we need to select the
# Raw option. Rather than seeing the familiar grid, we now have only a text area where we enter the request body
# directly. Our search definition is pretty straightforward but it will require a little bit of typing. Before we begin
# though, there's one more thing we should do. and that is set the content type.

#       We could do that by switching over to the header's tab and defining the header directly, but Postman offers an
# easier way. Immediately to the right of the body options, is a dropdown list. The currently selected value is text,
# implying that we're sending raw text but we're not. We're sending JSON data. Choose the JSON option from the list.
# Now, let's switch over to the header's tab, and see that Postman has automatically set the value for us.

# The search criteria is just a basic JSON object with a few attributes. Here we have chosen JSON so the Beautify
# option appeared. Click that, and Postman will reformat the content to a more typical style.
#  This process of defining a request body is the same regardless of whether we're searching, creating new objects,
#  or modifying existing objects.

#                           Collections and folders
#       Collections and folders are how we organize saved requests within a workspace. Collections are the highest level
#  where we can store requests. Folders within a collection let us further organize those requests. Since many APIs
#  provide a mechanism for working with data from different parts of the system, we might use a collection to group all
#  requests related to that API and folders to further isolate requests for each area within that API. For instance, at
#  my company, we use a single collection for requests pertaining to our applications API. That collection then contains
#  folders for music, message requests, users, and client locations and so on.

#       I use the drop down option on the new menu and select collection. This opens a dialogue box where we can enter a
# collection name and set some other options. We'll set the name and leave the other things for later. I'll call this
# collection Postman Sample API and hit the create button. When the dialogue closes, the sidebar will automatically
# switch over to the collections tab if it wasn't there already. It will also open a secondary panel showing some
# details about the collection. The secondary panel is nice, but I hardly ever use it, since nearly everything is
# available elsewhere within Postman.

#  Collections and folders offer an additional way to create requests through the respective ellipsis menus. I almost
#  never use them, but let's do it once to see it in action. Click the ellipsis button on the Postman Sample API
#  collection and select add request to open the save requests dialogue. Here, we're asked to enter a name, optional
#  description, and select a collection or folder to hold the request. Our first save request will be the API status
#  request so API status seems like a good name.

# ctrl + s  save request

#       Folders let us group requests within a collection. Let's create a folder called boards. Hover over the Postman
#  Sample API collection and click the ellipsis icon. Now select add folder. You'll see a window similar to that shown
#  when creating a new collection. Enter boards for the folder name. Then press enter to create the folder and close the
#  dialogue. We previously added a request to the collection through the collection's add request option. This time,
#  we'll start with a new request in the request builder to show the workflow difference. Click the plus icon to create
#  a new request. For this request, we'll just get a list of boards from the sample API. The beginning URL should be
#  familiar. And we just want to go to the boards route. To make sure this is working correctly, send the request.

#    Many of the APIs we use require some form of authentication. Chances are that we need the same authentication data
#  on each of the requests to a particular API. Consider the case of boards on our sample API. When we're not
#  authenticated, the API returns only those boards marked as public. If we want to retrieve a particular user's private
#  boards, we need to authenticate the request. Let's create a new request to get an authentication token, which we can
#  attach to those subsequent requests. For this request, we'll be sending credentials to the API.

#       We'll be sending data in the request body, so we need to change the HTTP method to Post. The sample API uses the
#  slash auth route to handle authentication, so we'll enter that in the address bar. Now, we'll specify the request
#  body. Click over to the Body tab and select raw. The content type for this is application JSON. Finally, we'll enter
#  the JSON, defining the credentials. The username attribute is demouser, and the password is demopassword. We can now
#  send this request. The API gives us back a JSON web token for our subsequent requests. Select the token value and
#  copy it to the clipboard.

#    And finally, Postman injecting the Authorization header into the request doesn't change the request at all. So
# there's no need for us to save this whenever that token changes. And before we move on, there's just one more thing
# to do. Let's update the Authorization request to omit any authentication data. Return to the Authorization request
# and click on the Authorization tab. Just as we changed the Authorization type in the collection, we want to change
# this to No Auth.

#