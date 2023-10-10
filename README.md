# Airo.tech
HackUTA Repository. Website for Aerodynamics of different cars



Backend

Github-
 *Created a repository to share with teammates
 
MongoDB
  *Changed the IP from computer to Google Cloud(1)
  *Installed the driver for python for mongo DB. installed pymongo
  *Connected the Google cloud to MongoDB by creating a cluster() with !database and collections! connect

  Atlas-Mongo:
  Notes:SSL hanshakes wasn't working and had error. took 2 hours to figure out. changed AWS to GCS error. Created User with password.

  Notes: Atlas is a placeholder for a database tht we call


Google Cloud
    *Created VM instance to get the external IP from Google Cloud (1).
    *Created a bucket from Cloud Storage to connect to Streamlit
    *Connected repositiory from Google cloud to Github
    *Connected SSH

  Notes:
  In order to share the code to show what our live code is we connect it to google cloud


Streamlit
 

 Notes: A library to create a website faster with python


Matplotlib
*Downloaded
Beautiful Soup
*Downloaded
Scrape website for data
Panda
Requests
  *Installed

File to convert the Database to control the rows and colums of website


Inspiration
We watched an F1 race in the parking lot adjacent to the Social Work & Smart Hospital building before the opening cermony and we were talking about F1 racing for about an hour. This gave us the idea of comparing the aerodynamics of different cars and how that would be an interesting topic for our project.

What it does
The website allows users to select two vehicles from a vast selection of over 300 options. Upon selection, the site presents an interface featuring two dropdown menus, enabling users to specify the make, model, and year of their chosen vehicles. Subsequently, the website offers a comparison of the aerodynamics and drag coefficients of the selected cars. As an added visual aid, the site employs a color-coded diagram to illustrate the varying degrees of wind resistance experienced by each vehicle. Red areas signify the highest wind impact, while yellow areas indicate a significant but less extreme impact. Green regions represent minimal wind influence. These visualizations are derived from calculations involving the frontal surface area of the cars and their coefficient of aerodynamic drag. These statistics and visual representations collectively provide valuable insights and information to users through the website.

How we built it
We used GitHub and Google Cloud to link our project elements together and allow for our collaboration. We used MongoDB Atlas as our database to hold the aerodynamics statistics. We then used a CSV file to extract the information from MongoDB and utilize in the streamlit file. We then used a python-based streamlit program to build our website. We additionally used the Matplotlib python library to create data visualizations of our coefficient of aerodynamic drag.

Challenges we ran into
Getting started was quite difficult as we were all new to many of the softwares that we were working with such as streamlit, GCP, and MongoDB.

Accomplishments that we're proud of
We are proud that we were able to utilize the MongoDB database without any prior experience and successfully use it to extract data.

What we learned
We learned much about how to operate different git functions and GCP actions.

What's next for Airo Auto
We hope to further improve the quality of our data and allow for more complex functions






