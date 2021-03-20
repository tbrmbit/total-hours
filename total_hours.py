import docx

class TotalHours:
    def __init__(self, total_str, decimal=2):
        self.content = []
        self.totalStr = total_str
        self.decimal = decimal

    def __sumTotal(self, listArray=[]):
        total = 0
        for item in listArray:
            total += item
        return total

    def __getNumber(self, n):                 
        length = len(self.totalStr) 
        nStr = n[length:length + self.decimal]
        final = ""
        for s in nStr.strip():
            if s.isnumeric():
                final += s
        return final

    def openTxt(self, path_file):
        try:
            file = open(path_file, 'r')
            for item in file:
                self.content.append(item)
            file.close()
        except error:
            print(error, 'Txt opening error')

    def openDocx(self, path_file):
        try:
            doc = docx.Document(path_file)
            for item in doc.paragraphs:
                self.content.append(item.text)
        except error:
            print(error, 'Docx opening error')

    def getTotal(self):
        listStr = []
        for line in self.content:
            if self.totalStr in line:
                strg = self.__getNumber(line)
                listStr.append(int(strg))
        print(self.__sumTotal(listStr))

   
