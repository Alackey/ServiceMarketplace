# ServiceMarketplace
Service Marketplace website for ITC

http://alackey.pythonanywhere.com/

Search Service Requests
* We have a Service model (an object defined in our database), which will store all the service requests performed by users from our site.
* We have a function that receives keyword input query and filters the database based on such input. The results are based whether or not the keyword is present in the title of the service or in its description.
* This page also includes pagination. This allows 9 service requests to be displayed per page. A page system is included at the bottom, which lets the user search through the services without having to scroll down the page as much.

# ServiceMarketplace
Service Marketplace website for ITC


### Installation - Mac OSX

1. Install Python 3.5

####Simple
2. Open the Terminal.
3. Enter "sudo pip3 install django"
4. Navigate to the root of the ServiceMarketplace folder using ther terminal.
5. Enter "python3 manage.py runserver"
6. Go to this link in the browser: http://127.0.0.1:8000/


### Create account

•	We have a form that lets the user register for an account with a Cross Site Request Forgery (csrf) token for security. This helps protect against malicious websites from logging in with stolen credential. This applied on all our forms that include credentials.

•	We then have a simple line of code that we put above any url/view/route that we want to require a login for like creating a service, leaving a review, and taking any action, other than viewing, on a service. 

•	We use a function to determine if they are allowed to bid by checking if they are the owner of the service, which means they cannot bid on the service.

•	The creation of a User using the User model in the database is handled by our framework/language with fields for username, first name, last name, and password.

### Login

•	If you tried to go to a page that requires you to be logged in, you will be redirected to the login page and if the credentials are entered correctly, they will be redirected back to the page they tried to access while not logged in.

### Post and Update a service request

•	We have a model/table in our database for each service that uses a form to accept data from the client while using a csrf token when sending the data from the client to the backend to create and update the service.

### Close a service

•	We coded it so as long as the user is logged in and is the owner of the post, they are able to close any post of theirs, but it not able to reopen it.

### View Reviews to a Client/Provider
* Reviews is a model in our database that includes data such as rating, and comments.
* Reviews are listed in user profiles and are divided into two columns: comments from clients, and comments from providers. These comments are retrieved accordingly from the database based on certain filters.

### User Profile and My Account
* We have defined a page (user_profile.html, or /user/theusername/) as well as my_account page where users can see relevant information regarding given users.
* User profile pages include all the reviews that were given to these users.
* My account page includes all the reviews given to the logged in user, as well as services that this user has requested, both opened, and closed. Only two reviews from clients and from providers, as well as three services, both opened and closed, are displayed. To see all the reviews and services, the user has the option to click on a link that will redirect to a single page outputting necessary info.
* Average rating from both clients and providers are provided. This was done by retrieving all ratings to the given user from the database. A function gathers all this data and outputs an average result.

### Receive a bid from a provider

•	We use Firebase to handle the real time updates which allows for bidding without reloading the page. This was implemented and managed on the front end in javascript.

•	There is a countdown timer for the bidding and when it hits 0s the bidding ends by removing the bidding field and not allowing anyone to submit any more bids.

•	The bidding can also when the someone enters $0 (doing the service for free) which ends the bids and the countdown. We also verify the input if clean, good with error messages if it is not.


### Database

•	User – This was a model that our framework provides and which is connected to every other model we have.

•	Service – This model keeps track of every service that is created. The two fields client and service_provider are an instance of the User model, and service_provider only being assigned when the service’s bidding ends. 

•	Bid – The service_provider is an instance of the User model and service is an instance of the Service model. Having an instance of Service allows the us to access the service that the bid was placed on and the client of the service.

•	Review – user and author are an instance of the model User and keep track of them. 

![Alt text](ServiceMarketplace.png?raw=true "Database Design")


### Features not implemented:
•	View bid history


### Extra Features
•	Unit Tests – We added a small amount of tests that can be used in the future when code gets changed or added to verify other features didn’t break in the process of adding or changing.








