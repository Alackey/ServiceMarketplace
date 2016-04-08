# ServiceMarketplace
Service Marketplace website for ITC


Search Service Requests
* We have a Service model (an object defined in our database), which will store all the service requests performed by users from our site.
* We have a function that receives keyword input query and filters the database based on such input. The results are based whether or not the keyword is present in the title of the service or in its description.
* This page also includes pagination. This allows 9 service requests to be displayed per page. A page system is included at the bottom, which lets the user search through the services without having to scroll down the page as much.

Create account
*	We have a form that lets the user register for an account with a Cross Site Request Forgery (csrf) token for security. We then have a simple line of code that we could put above any url/view/route that we want to require a login for like creating a service, leaving a review, and taking any action, other than viewing, on a service. 
*	We use a function to determine if they are allowed to bid by checking if they are the owner of the service, which means they cannot bid on the service.
*	The creation of a User using the User model in the database is handled by our framework/language.

View Reviews to a Client/Provider
* Reviews is a model in our database that includes data such as rating, and comments.
* Reviews are listed in user profiles and are divided into two columns: comments from clients, and comments from providers. These comments are retrieved accordingly from the database based on certain filters.

User Profile and My Account
* We have defined a page (user_profile.html, or /user/theusername/) as well as my_account page where users can see relevant information regarding given users.
* User profile pages include all the reviews that were given to these users.
* My account page includes all the reviews given to the logged in user, as well as services that this user has requested, both opened, and closed. Only two reviews from clients and from providers, as well as three services, both opened and closed, are displayed. To see all the reviews and services, the user has the option to click on a link that will redirect to a single page outputting necessary info.
* Average rating from both clients and providers are provided. This was done by retrieving all ratings to the given user from the database. A function gathers all this data and outputs an average result.




