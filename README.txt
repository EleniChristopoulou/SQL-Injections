In this python file we are going to simulate an environment vulnerable to sql injections. 

In sql_injection.py is succesully working as a login form where email and password need to match in order to
login succesfully.
However, knowing how sql commands work we can manipulate the form into eventually letting us enter without the
need of knowing any email nor password.

The trick is done on to the following command:
"SELECT * FROM users WHERE email='"+email+"' AND password='"+password+"'"

where email and password are taken straight from the user 
One way is to enter is the following:

email: any
password: any' OR 1=1--


second python file with the name of 'parameterized_queries.py' prevents sql injections from succeding by simply replacing
the above with the following:
"SELECT * FROM users WHERE email=? AND password=?",(email,password)

Here "?" acts as a placeholder for the actual values. The actual values are provided separately when executing the query.






