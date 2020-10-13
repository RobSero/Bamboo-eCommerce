# Bamboo - Sustainable Product Ecommerce

![database diagram](https://bamboostatic.s3.eu-west-2.amazonaws.com/static/img/homepage.png)
 
*Deployed Site:* https://bamboobits.herokuapp.com/

## Installation and Usage

- Clone or download the repo
- Within your virtual environment, ```run pip install -r requirements.txt```
- Run your Django server with ```python manage.py runserver```

 
## Brief: Ongoing Live eCommerce Site
Myself and a colleague wanted to create our own eCommerce platform which focused on promoting sustainability where I would build the site whilst they would focus on sourcing reliable products from suppliers. At the current stage, the site is live however the actual products have not been sourced yet and so features such as Stripe payment integration along with mailchimp emailing have been postponed until we can secure these.
 
Despite having well established options such as Shopify and Squarespace (which we may end up using in the future anyway), I wanted to build the site from scratch to improve my Django abilities and develop my understanding of specific areas of Django including the model manager and form validation.
For this project, I decided to use the Django templating engine rather than building a RESTful API to interface with a React frontend as this was a good chance to practice Django's sessions and messages feature.
 
 
***Note: As time goes on, there will be additional features added including Stripe Payments, Mailchimp emailing and analytics tools however these are not required at this time***
 
 
## **1.0 - Overview**
 
Bamboo is a full stack eCommerce platform promoting sustainable products built using Django’s in-built MVT architecture with a PostgreSQL database and image storage on AWS S3. The site will continue to be developed once the products are sourced and will aim to work alongside Shopify's API to handle various services such as stock management.
The Application offers typical eCommerce features including carts, watchlists and custom user models.
The application is responsive to all screen sizes and uses a combination of custom CSS animations along with imported CSS to create an engaging experience for users on every page.
 


![database diagram](https://bamboostatic.s3.eu-west-2.amazonaws.com/static/img/productpage.png)
 
## **2.0 Technology Summary**
 
### **2.1 - Client Side**
 
- Python 3+
- Django Templating Engine
- HTML
- Bulma
- CSS3
- Bootstrap
 
The client side is a combination of custom CSS and animation along with third party templates as the primary focus of the project was to ensure a robust server side within the timescale.
 
### **2.2 - Server Side -**
 
- Python 3+
- Django
- Postgres Database
- Amazon S3
 
 
The server side of the application has been built with various Django apps to handle the various eCommerce functionality including cart management and custom users. At this stage, most CRUD functionality is only enabled within the admin panel with the exception of users changing the delivery address details at the checkout page. All static files and media files are stored remotely on Amazon S3 and will be stored automatically when new products are added to the database.
 
 
## **3.0 - Database Structure**
 
![database diagram](https://bamboostatic.s3.eu-west-2.amazonaws.com/static/img/databasemodel.png)
 
PostgreSQL is used and is organized in a logical manner for storing different users and products but then building join tables between them with the cart feature. The relationships stored within the carts are all handled by Django's in-built ORM.
 
There are various pre-save and post-save signals set up to ensure that database entries are kept up to date based on changes in the user's cart (generally the cart totals are affected and will listen for these changes).
 
 


### **3.1 - The Cart Model**

![database diagram](https://bamboostatic.s3.eu-west-2.amazonaws.com/static/img/cartmodel.png)
 
The cart model is the foundation to the eCommerce platform as it establishes the relationships between the users and their associated products.
 
A cart can only be associated with one user and so a OneToOneField is used here and will Cascade delete the cart if the user account is deleted. The products have a ManyToMany relationship with the cart due to multiple products sharing this relationship with other user's carts too.
 
The receivers in this model are constantly watching for changes in the product relationships so if a product is added or removed, the new subtotal will be calculated along with the new total.
 
The cart feeds into the order model which will be updated post-save of the cart. When a cart is saved into the database, an order will either be created or updated so that when payment will be taken, there is a model containing all the latest information required including shipping cost and other variables if needed.
 
### **3.2 - Model Managers**
 
This was a great opportunity to dive deeper into Django models and start building my own custom manager options which allow for DRY code particularly in the view files. There are many occasions when a cart needs to be either created, updated, or assigned to a user based on different circumstances. If a user is not signed in then a cart is created for the guest but when they sign in, they need to be assigned that cart so they can proceed with their order.
 
The 'new_cart_or_get' method to the Cart model allows for all this logic to be handled with the models file as this method is called frequently throughout the app and provides the important functionality detailed above.
 
![database diagram](https://bamboostatic.s3.eu-west-2.amazonaws.com/static/img/cartmanager.png)
 
### **3.3 - Custom User Model**
 
This project used Django's robust authentication system along with sessions to determine user authentication and authorization. There were a few unnecessary user fields such as username which served no purpose in an eCommerce site and so it was necessary to create a custom user model to omit these details.
 
In order to keep the registration and sign up as simple as possible (to encourage users to sign up), the only fields required were the email and password. Throughout the checkout process, there is the requirement to input the user's address for billing and delivery. At this stage, the user must be signed in to proceed with checkout however I may include a guest checkout option where there is no need to sign up or keep the guest details on the database.
 
 
## **6.0 - Personal Reflection**
 
The project so far has been a great experience to dive deeper into many of Django's features more specifically the sessions, and custom user models.
 
I have learnt to appreciate the power of altering the standard model methods through custom built model managers which can really help to keep code DRY throughout the rest of the application.
 
Amazon S3 is a solid gateway into AWS services and I was considering using Elastic Beanstalk however Heroku's accessibility and free-tier seemed more appropriate at this time.  I am excited to start exploring more areas of AWS and looking to see what features I can integrate into this project as time and requirements move forward.
 
### **6.1 - Key Learning Points**
 
- This project was good exposure to using many of python's in-built functions as there were quite a lot of customization of Django's standard features including models and users.
- Becoming more comfortable with sessions and passing requests around was key for me as I wanted to understand how Django can be used to extract more useful data from the HTTP requests.
- I prefer using Django as a RESTful API and building a React App to interface with it largely because I enjoy handling some of the logic on the frontend at times rather than solely doing it all on the server. In particular, areas like sorting products and filtering, I personally preferred React for handling this rather than making separate HTTP requests to the server to collect new product datasets based on a search query.
 
### **6.2 - Pro’s**
 
- Lots of experience reading and understanding documentation from Django's website. As Django is so large and robust, I enjoy starting a new project using it as everytime there is a new feature I can pick up and I can always refine my current knowledge of it
- I am excited about the options which I can take on this project and continue to add further systems to it such as the stripe payments and emailing.
- I am improving my ability to write DRY code particularly by customizing existing django features with the managers.
 
### **6.3 - Cons**
 
- I much prefer using React to handle processes such as sorting and filtering arrays of products rather than making many HTTP requests on change. While it is not necessarily a bad thing that I have used the templates on this project, I now know that I prefer using a frontend framework to handle this kind of logic.
 
### **6.3 - Future Features / Improvements**
 
- Stripe Payment integration will be required at some point
- Integrating with Shopify API services may be something we consider as they are already pre-built, robust and have good community support.
- Mailchimp email features
- Stock management will need to be implemented, TBC how this will be addressed at this stage
 
 
## Hope you have fun!

