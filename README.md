# File-sharing-site-with-Python-using-Flask-
It`s simply file sharing site with python using framework Flask,database SQL with registration,authorization and your own files folder 
for saving and sharing files .
In the folder "files" you have all folders of registered users, which includes their own files.
In the folder "templates" you can find all the html site pages.
file "base.db" is the SQL file, which holds all data about this site users.

So how works this site?
Whe you starting the app.py you need to open 127.0.0.1:4000 in your web browser and than you can sign up or log in.
With signing up automaticly creates your own folder with your user`s name in the folder "files".
Than you can manage your own page profile with uploading files, changing your own folder`s password (which is none by default), downloading fliles.
If you want to download file from other user`s directory you need to get folder`s pasword from this user to open his dicrectory and download files from here.
But because of the server is your computer, downloading and uploading files will be undertaken only on your computer`s directory.
