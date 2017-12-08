# Neural-Art-UCSC
Creating unique art using A.I.

# Using This Web App
This web app uses https://docs.floydhub.com/examples/style_transfer/ for the style transfer algorithm, and floydhub has a service to host the model as a REST API.

Once you clone this repository there are a few steps to getting everything to work.

1. You need to have a floydhub account, it is free and you can use up to 2 hours of GPU
and 20 hours of CPU for free.

2. You are going to want to create a virtual environment.

3. now install all of the requirements with:
pip install -r requirements.txt

4. At this point you will need to init the folder with floydhub using
floyd init fast-style-transfer

5. Now you can serve the model using:
floyd run --env tensorflow-0.12:py2 --data narenst/datasets/neural-style-transfer-pre-trained-models/1:input --mode serve

6. 5. will give the the endpoint, you will need this when completing the form.

7. Now you can run:
python routes.py

This is start the webapp on the local host.

8. Now you can fill out the form and use the endpoint that was given when you served the model. And you will now be able to test out creating new art!

9. Remember after you are done to turn off the served model under jobs in your floydhub account, then when you want to use it again, you serve it again and use the new endpoint.


# Definition of Done:  <br />
Code reviewed <br />
Acceptance criteria met <br />
Functional Tests passed <br />
Non-Functional requirements met <br />
Product Owner accepts the User Story <br />


# Style Guildlines: <br />
Python: https://www.python.org/dev/peps/pep-0008/ <br />
HTML: https://www.w3schools.com/html/html5_syntax.asp <br />
