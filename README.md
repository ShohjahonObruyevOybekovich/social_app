<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram Clone App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #4267B2;
            color: white;
            padding: 10px 20px;
            text-align: center;
        }
        section {
            padding: 20px;
        }
        h2 {
            color: #333;
        }
        nav {
            background-color: #333;
            padding: 10px;
            text-align: center;
        }
        nav a {
            color: white;
            margin: 0 10px;
            text-decoration: none;
            font-weight: bold;
        }
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 10px 0;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
    </style>
</head>
<body>

<header>
    <h1>Instagram Clone App</h1>
    <p>Under Development</p>
    <p>Back-end Developer: Shohjahon Obruyev</p>
</header>

<nav>
    <a href="#about">About</a>
    <a href="#builtwith">Built With</a>
    <a href="#features">Features</a>
    <a href="#gettingstarted">Getting Started</a>
    <a href="#license">License</a>
    <a href="#contact">Contact</a>
</nav>

<section id="about">
    <h2>About The Project</h2>
    <p>This is a clone application project of Instagram that aims to develop using the technologies that Instagram uses. We tried to add as much detail as we could, from security to user experience.</p>
</section>

<section id="builtwith">
    <h2>Built With</h2>
    <ul>
        <li>Python</li>
        <li>Django</li>
        <li>Rest Framework</li>
        <li>PostgreSQL</li>
    </ul>
</section>

<section id="features">
    <h2>Features</h2>
    <h3>Back-end Features</h3>
    <ul>
        <li>User Login, Registration, and Authentication (JWT Token)</li>
        <li>Throttle System for Security</li>
        <li>Post Create, Like, Delete, Update</li>
        <li>Comment Create, Like, Delete</li>
        <li>Follow Request, Follow System (Private/Public Accounts)</li>
        <li>Notification System</li>
        <li>Saved Post System</li>
        <li>Stories System (24 Hour Expiry)</li>
    </ul>

    <h3>Front-end Features</h3>
    <ul>
        <li>Responsive Design</li>
        <li>Login System</li>
        <li>Store Access Keys in Encrypted Storage</li>
        <li>Navigation System</li>
        <li>Infinite Scroll</li>
        <li>Optimized Scroll Via Flatlist</li>
    </ul>
</section>

<section id="gettingstarted">
    <h2>Getting Started</h2>
    <p>To run the server, use the following commands while in the same directory as the manage.py file:</p>
    <h3>For Windows</h3>
    <pre><code>python manage.py runserver</code></pre>
    <h3>For Linux</h3>
    <pre><code>python3 manage.py runserver</code></pre>

    <p>If you want to connect from different devices in your local network, open the settings.py file and edit the <strong>ALLOWED_HOSTS</strong> list:</p>
    <pre><code>ALLOWED_HOSTS = ["*"]</code></pre>
</section>

<section id="license">
    <h2>License</h2>
    <p>Distributed under the MIT License. See LICENSE.txt for more information.</p>
</section>

<section id="contact">
    <h2>Contact</h2>
    <p>Back-end Developer: Shohjahon Obruyev</p>
    <p>Email: shohjahonobruyev3@gmail.com</p>
</section>

<footer>
    <p>&copy; 2024 Instagram Clone App | All rights reserved</p>
</footer>

</body>
</html>
