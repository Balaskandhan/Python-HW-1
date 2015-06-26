import sqlite3
from wsgiref.simple_server import make_server

def get_form_vals(post_str):
    form_vals = {item.split("=")[0]: item.split("=")[1] for item in post_str.decode().split("&")}
    return form_vals

def hello_world_app(environ, start_response):
    message="<body>"
    status = '200 OK'
    headers = [('Content-type', 'html; charset=utf-8')]
    start_response(status, headers)
    if(environ['REQUEST_METHOD'] == 'POST'):
        message += "<br>Your data has been recorded:"
        request_body_size = int(environ['CONTENT_LENGTH'])
        request_body = environ['wsgi.input'].read(request_body_size)
        form_vals = get_form_vals(request_body)
        
        conn = sqlite3.connect("zoo.sqlite")
        cursor = conn.cursor()
        data_val = (form_vals["animal"], form_vals["count"])
        cursor.execute("create table IF NOT EXISTS animal_count (name text, count integer)") #execute the create table query
        cursor.execute("insert into animal_count(name, count) values(?, ?)", data_val)
        cursor.execute("select name,count from animal_count")
        
#         message +="<table>"
#         message +="<th><h1>ZOO DETAILS<h1><th>"
#         message +="<tr><td>Country</td><td>Total Area</td></tr>"
#         
#         for row in cursor.fetchall():
#             name,count = row
#             message +="<tr><td>"+name+"</td><td>"+str(count)+"</td></tr>"
# #             message += "<h3>"+name+"\t"+str(count)+"<h3>"
# #             print ('%s %s' % (name,count))
#         message += "</table>"
        conn.commit()
        conn.close()
        
        
        
        for values in form_vals.keys():
            message += "<br/>"+values + " = " + form_vals[values]

    message += "<h1>Welcome to the Zoo</h1>"
    message += "<form method='POST'><br>Animal:<input type=text name='animal'>"
    message += "<br><br>Count:<input type=text name='count'>"
    message += "<br><br><input type='submit' name='Submit' ></form></body>"
    return[bytes(message,'utf-8')]

httpd = make_server('', 8000, hello_world_app)
print("Serving on port 8000...")

httpd.serve_forever()