# Lab 5: File path traversal, validation of start of path

The vulnerability exists in the `filename` parameter when retrieving images. However, the application expects the filename to start with the base folder `/var/www/images`. We can bypass this restriction by prepending the required path to our payload.\
The objective is to retrieve the contents of `/etc/passwd`.

<p align="center"><img src="./../../../images/Path Traversal/lab5.png" alt="Lab 5" width="70%" height="70%"></p>