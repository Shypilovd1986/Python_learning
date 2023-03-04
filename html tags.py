# <!doctype html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport"
#           content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
#     <meta http-equiv="X-UA-Compatible" content="ie=edge">
#     <meta name="author" content="Dmitriy Shypilov">
#     <meta name="keywords" content="test, html">
#     <title>Document</title>
#     <!-- <style>
#         b {
#             background: pink
#         }
#     </style> -->
#       <link rel="stylesheet" href="static/css/main.css">
# </head>
# <body>
#     <div id="block-1">
#         <h2>Some interesting text</h2>
#     </div>
#     <!-- Headers -->
#     <h1>Big header</h1>
#     <h2>Header</h2>
#     <h3>Header</h3>
#     <h4>Header</h4>
#     <h5>Header</h5>
#     <h6 style="color: red">Header</h6>
#     <a href="#bottom">Go to bottom of page</a>
#     <p title="some text" class="p-info">  Lorem ipsum dolor sit <b> amet, </b> consectetur <i id="i-info"> adipisicing </i>elit. <strike> Aperiam
#         architecto </strike>
#         commodi culpa <strong> cumque dolores </strong>, ex non officiis <sup>perferendis</sup> <sub> sequi </sub>
#         tempora. </p>
#     <p> Lorem <small> ipsum dolor </small> sit amet, <big>una matina </big> adipisicing elit. Tempora, totam.</p>
#     <!-- show code without format -->
#     <pre>
#         def main():
#             x=10
#             return x
#     </pre>
#     <code>
#         def main(x):
#             return x*3
#     </code>
#     <ul id="navi" type="square">
#         <li>apple</li>
#         <li>pineapple</li>
#         <li>plum</li>
#     </ul>
#     <ol type="I" start="II" >
#         <li>apple</li>
#         <li>pineapple</li>
#     </ol>
#     <table border="1" width="200px">
#         <thead>
#             <tr>
#                 <th>Apple</th>
#                 <th>Plum</th>
#                 <th>Pear</th>
#             </tr>
#         </thead>
#         <tbody align="center">
#             <tr>
#                 <td>23</td>
#                 <td>354</td>
#                 <td>1111</td>
#             </tr>
#         </tbody>
#         <tfoot>
#
#         </tfoot>
#     </table>
#     <div class="div_info">
#         <a class="main_link" href="http:\\google.com" target="_blank">Go to Google</a><br>
#         <a href="list_of_item.html">Список товаров</a><br>
#         <a name="bottom"></a>
#         <!-- anchor link -->
#
#         <p class="p-info"></p>
#         <a href="mailto:shypilovd@gmail.com">Send to message</a><br>
#     </div>
#     <img src="images\house.jpg " width="500" alt="house" height="auto">
#     <script src="js/main.js"></script>
#     <div>Container</div>
#     <p>Lorem ipsum dolor sit amet, <span>consectetur adipisicing elit</span>. Cupiditate, quidem.</p>
#
#     <form action="" method="" name="user_information" id="1">
#         <label>Input your name</label><br>
#         <input type="text" placeholder="Dmitriy" value="some" maxlength="20" required> <br>
#
#         <input type="text" value="Your info" disabled><br>
#         <input type="url" value="google.com" readonly><br>
#
#         <label>Input your email</label><br>
#         <input type="email"><br>
#
#         <input type="button" value="click"><br>
#         <input type="date" value="click"><br>
#         <input type="color" value="click"><br>
#         <input type="radio" name="1">
#         <input type="radio" name="1"><br>
#         <input type="radio" name="1"><br>
#         <input type="checkbox"><br>
#         <input type="search"><br>
#         <input type="password"><br>
#         <input type="submit">
#     </form>
#
#     <form action="" method="" name="text">
#         <label>Input your text</label><br>
#         <textarea placeholder="your favorite poem" maxlength="200">
#         </textarea><br>
#         <button type="submit" >Send text</button>
#     </form>
#
#     <form action="" method="" name="categories">
#         <label>Choose your category</label><br>
#         <select>
#             <!--<select multiple size="2">  your can choose 2 position-->
#             <option>Electricity</option>
#             <option>Home</option>
#             <option >Plumbing</option>
#             <option selected disabled>-------</option>
#         </select>
#     </form>
#
#     <!-- html5 tags-->
#     <header></header>
#     <main></main>
#     <aside></aside>
#     <footer></footer>
#     <progress max="100" value="9">install in 9 percents</progress>
#     <details >
#         <summary>Your details</summary>
#         Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illum, vitae!
#     </details>
#
#     <div id="block-2"></div>
#     <div></div>
#
#     <a target="_blank" href="https://www.browserstack.com/?utm_source=google&utm_medium=cpc&utm_platform=paidads&utm_content=434390274153&utm_campaign=Search-Brand-Tier1-EMEA-CL&utm_campaigncode=BrowserStack-Alpha+1012866&utm_term=e+browserstack&gclid=Cj0KCQiAi8KfBhCuARIsADp-A54WSPR7ehUxB5mkdgKC7DU_fzDyvau6UoBgwFXr5oUQQaBdtL4xc6EaAgCvEALw_wcB">Testing your site</a>
# </body>
# </html>
#
#
#
#     ----------------------------       CSS     ------------------------------
#
# @import url('https://fonts.googleapis.com/css2?family=Gajraj+One&family=Gloock&family=Roboto:wght@300&display=swap');
#
#
# /* for all tags */
# * {
#     margin:10px;
# }
#
# body {
#     background-image: url('https://images.unsplash.com/photo-1513151233558-d860c5398176?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8ZnVuJTIwYmFja2dyb3VuZHxlbnwwfHwwfHw%3D&w=1000&q=80');
#     background-repeat: no-repeat;
#     background-position: center;
#     background-size: cover;
#     background-attachment: fixed;
#     text-transform: lowercase;
#     text-align: justify;
#     font-family: 'Gloock';
#     font-style: normal;
#     font-weight: 300;
#     word-spacing: 20px;
#     letter-spacing: 10px;
#     line-height: 20px;
#     cursor: auto;
#     padding: 0;
# }
#
# /* for all divs */
# div {
#     background-color: #2d3d80;
# }
#
# /* class  */
# .div_info {
#   background: #148785;
#   height: 50px;
#   width: 400px;
#   border-style: double;
#   border-color: #1b1b6b;
#   border-radius: 5px 10px;
#   margin: 20px;
#   border-bottom: 0;
#   opacity: 0.9;
#   display: block;
# }
#
#
# /* class p-info */
# .p-info {
#     /*background: pink;*/
#     color: purple;
# }
#
# /* identifier with name i-info */
# #i-info {
#     background: green;
#     color: blue;
# }
#
# /* all tags i in tag p in tag div  */
# div p i, div p b {
#     color: green;
# }
# /* class  */
# .main_link{
#     color: red;
#     text-decoration: none;
# }
#
# /*The pseudo-class:visited*/
# .main_link:visited {
#     color: blue;
#     text-decoration: underline;
#     text-decoration-color: purple;
# }
#
# /*The pseudo-class:visited*/
# .main_link:hover {
#     color: red;
#     text-decoration: underline;
#     text-decoration-color: purple;
# }
#
#
# /*The pseudo-class empty with pseudo-element after*/
# p.p-info:not:empty::after {
#     background:grey;
#     content: 'This paragraph is empty'
# }
#
# /*The pseudo-class empty with pseudo-element first-letter*/
# /*p.p-info::first-line { */
# p.p-info::first-letter {
#     background:grey;
#     color: green;
# }
#
# /*The pseudo-class with first h3 tag*/
# /*h3:last-of-type {*/
# h3:first-of-type {
#     color: green;
# }
#
# #block-1{
#     background: #333;
#     height: 50px;
#     color: white;
#     text-align: center;
#     width: 100%;
#     margin-left: -20px;
#     margin-bottom: 20px;
#     padding: 0;
#     position: fixed;
#     /* position: relative */
#     /* relative from current place ; bottom: -10px; left: 5px; right: 20px; top: 10px;  */
#     /* position: absolute */
#     /* absolute from screen ; bottom: -10px; left: 5px; right: 20px; top: 10px;  */
#     margin-top:-20px;
#     text-height:50px;
#     /* z-index:0 , z-ndex: 1; for different blocks , how this blocks display this their layer*/
# }
#
# #navi{
#     list-style: none;
#     display: block;
#     float: left;
#     width: 50%;
#     margin-left: 50%;
#     text-align: center;
#     margin-bottom: 20px;
# }
#
# #navi li{
#     display: inline;
#     background: #fafafa;
#     border: 1px solid silver;
#     padding: o 20px;
# }
#
# #navi li: hover{
#     background: #333;
#     color: #fafafa;
# }