# Total-Hours

## :blush: **Why?**
Sometimes using text files to writing scope or listing some things to do and our file finally pretty big. How I've receive and writting thats files, make this class to help the get total hours them.

## ✨ Features

- [x] Open files txt and Docx
- [x] The total sum of string following a pattern

## 🔨 Usage
Just install <a href="https://www.python.org/downloads/">🔗 python</a> and then install <a href="https://github.com/python-openxml/python-docx"> python-docx</a>:

```py
pip install python-docx
```
Run the following commands on python command line:

``` py
myClass = TotalHours('TOTAL: ', 3)
myClass.openTxt('files/scope.txt') or myClass.openDocx('files/scope.docx')
myClass.getTotal()
```

