from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI


OPENAI_API_KEY = ''
db = SQLDatabase.from_uri("sqlite:///sqlite-sakila.db") # replace with your db name
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", 
                 openai_api_key=OPENAI_API_KEY,
                 temperature=0)
chain = create_sql_query_chain(llm, db)


response = chain.invoke({"question": "name all movies of cameron streep?"}).replace("SQLQuery :",'').replace("SQLQuery:",'').strip() # these replace functions can be better handled with regex or need of them can be removed in full-time project
print(response) # the SQL Query from human language 
print(db.run(response)) # the result of running the SQL Query

