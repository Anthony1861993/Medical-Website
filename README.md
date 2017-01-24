# Medical-Website

+	Created a web-based application dashboard UI to display info of prostate cancer patients
+	Enhanced the dashboard with user interactivity such as charts and graphs
+	Utilized Django framework for backend and Bootstrap, jQuery, and Highcharts for front-end
+	Implemented the project in Python, JavaScript, HTML, CSS (~1K lines)
+	Video demo: https://www.dropbox.com/s/9dl5aqr5moi524n/video.mp4?dl=0


Below is all the info about this assignment and how to run the website locally:

For this assignment, I use the Django framework and Python for backend.
This is the first time that I'm using this framework (I have 1 week so
I want to try something new!). For frontend, I use Bootstrap, jQuery
and Highcharts for the graphs and charts.
I actually wanted to add more to the website (3D interactive graph, etc.), but
I didn't want to compromise the performance of the page. The assignment is kinda
open-ended so I'm not sure if this is considered "interactive" enough, but I can
totally make it even more sophisticated. 


Instructions to run the website locally:

+ Open command line
+ cd to the outer "mysite" directory (where manage.py is located)

SET UP OUR DATABASE
+ Run 
	$ python manage.py makemigrations patients 
	(Explanation: to create migrations for any new model we create.
	If there's no changes in the models, it will say "No changes detected in app 'patients'")
	
	$ python manage.py migrate
	(Explanation: to apply those changes to the database
	If there's no changes, it will say "No migations to apply")
	
	$ python addExcelFile.py
	(if the data from the excel file is not in our database already)
	
(Optional) SET UP ADMIN PAGE
+ Run: $ python manage.py createsuperuser
	and then input username, email address, and password as prompted 

RUN THE USER PAGE
+ Run: $ python manage.py runserver
	then open this: http://127.0.0.1:8000/patients/ in your Web browser
	(I recommend Chrome for optimal result)
	
If you have any trouble with any of the above steps, please 
email me. 
