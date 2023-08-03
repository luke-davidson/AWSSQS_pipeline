# Fetch - DE Take Home Assignment
This repo holds all files created to create a small data pipeline, reading from an AWS SQS Queue and writing to a Postgres DB.

author: Luke Davidson - davidson.luked@gmail.com - (978) 201-2693

# HOW TO RUN
1. Clone repo locally and ensure docker and docker-compose are installed
2. Navigate to the cloned repo folder via the terminal
3. Run `pip install -r requirements.txt` on the command line
4. Run the command `docker-compose up` on the command line
5. Run the main python file using the command `python3 main.py`
    * Enter the number of messages to request, transform and push to the Postgres DB when prompted

# Design considerations
1. How will you read messages from the queue?
    - 
2. What type of data structures should be used?
    - 
3. How will you mask the PII data so that duplicate values can be identified?
    - 
4. What will be your strategy for connecting and writing to Postgres?
    - 
5. Where and how will your application run?
    - 

# Questions
1. How would you deploy this application in production?
    - 
2. What other components would you want to add to make this production ready?
    - 
3. How can this application scale with a growing dataset?
    - 
4. How can PII be recovered later on?
    - 
5. What are the assumptions you made?
    - 