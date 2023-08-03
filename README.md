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

# Questions and Next Steps
1. How would you deploy this application in production?
    - To deploy this pipeline in to production, I would integrate either regular or event driven sheduling, whichever is most suitable for it's use case, through cloud services such as AWS Data Pipeline or similar frameworks. When deployed, I would also integrate CI/CD pipelines to ensure the pipeline is continuously being tested and upgraded in its early stages. Finally I would write the pipeline in a more object oriented way to be more easily implemented with other processes.
2. What other components would you want to add to make this production ready?
    - A big aspect to add to make it production ready is edge case testing, or unit tests. I caught a couple errors simply through running it multiple times over the same training data. Ideally each aspect of the pipeline is tested on a large amount of simulated production data so that edge cases are caught and fixes can be implemented before it is released to full production. I would also implement a logging system to monitor performance and errors. 
3. How can this application scale with a growing dataset?
    - Implementing event-driven scheduling where data is ingested when it hits a certain file size or other metric can help maintain a similar workload on the pipeline when data increases. We can also use services such as Kubernetes or AWS Lambda to better allocate resources and scale both horizontally (multiple processes) and vertically (increasing memory of processing machine).
4. How can PII be recovered later on?
    - The SHA256 algorithm, used to hash the PII in my implementation, is irreversible and therefore the original IP and Device ID cannot be later recovered. A solution to this would be to store the original IP and Device ID information in an alternative database that has strict access requirements, with a corresponding metric (such as create_date) that can later be matched with the original hashed database information.
5. What are the assumptions you made?
    - One big assumption I made in this implementation is assuming the user_logins table already exists. I would ideally make this implementation more robust by adding a "CREATE IF NOT EXISTS" or similar statement for the edge case where the table may not exist or a new table is being created. Another assumption I made was that the original IP and Device ID data would not need to be later recovered, as as mentioned before, hashing it is irreversible. I also assumed that the port locations remain constant throughout locatoins as they are hardcoded in to the `docker-compose.yml` file.