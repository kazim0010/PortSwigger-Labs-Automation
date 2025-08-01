# Lab 6: File path traversal, validation of file extension with null byte bypass

The vulnerability exists in the `filename` parameter when retrieving images. However, the application validates that the filename ends with a specific `extension`. To bypass this restriction, we can append a null byte `%00` to the filename.\
The objective is to retrieve the contents of `/etc/passwd`.

<p align="center"><img src="./../../../images/Path Traversal/lab6.png" alt="Lab 6" width="70%" height="70%"></p>