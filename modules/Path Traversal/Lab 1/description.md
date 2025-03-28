# Lab 1: File path traversal, simple case

The vulnerability exists in the `filename` parameter when retrieving images, allowing directory traversal by using `../`  sequence multiple times.\
The objective is to access the contents of `/etc/passwd`.

<p align="center"><img src="./../../../images/lab1.png" alt="Lab 1" width="70%" height="70%"></p>