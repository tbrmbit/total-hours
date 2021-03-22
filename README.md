# Total-Hours

## :blush: **Why?**
Sometimes we use text files to writing a scope or listing some things to do and our file finishes pretty big. How I've received and writing that's files, made this class to help get total hours them.

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

