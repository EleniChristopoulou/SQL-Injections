In this python file we are going to simulate an environment vulnerable to sql injections. 

In sql_injection.py is succesully working as a login form where email and password need to match in order to
login succesfully.
However, knowing how sql commands work we can take manipulate the form into eventually letting us enter with
no need to know any email nor password.

The trick is done on to the following command
"SELECT * FROM users WHERE email='"+email+"' AND password='"+password+"'"

where email and password are taken straight from the user 

One way is to enter is the following:

email: any
password: any' OR 1=1--


second python file with the name of parameterized queries prevents sql injections form succeding by simply replacing
with the following:
"SELECT * FROM users WHERE email=? AND password=?",(email,password)

 ? acts as a placeholder for the actual values. The actual values are provided separately when executing the query.






