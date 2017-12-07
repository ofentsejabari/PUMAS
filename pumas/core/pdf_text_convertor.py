from pyPdf2 import PdfFileReader


class pdf_text():

    def getPDFContent(path):

        content = ""

        pdf = PdfFileReader(path, "rb")

        for i in range(0, pdf.getNumPages()):
            f=open("xxx.txt",'a')
            content= pdf.getPage(i).extractText() + "\n"
            import string
            c=content.split()
            for a in c:
                f.write(" ")
                f.write(a)
            f.write('\n')
            f.close()

        return content


    def getPDFContents(path):
        # content = ""
        # # Load PDF into pyPDF
        # pdf = pyPdf.PdfFileReader(file(path, "rb"))
        # # Iterate pages
        # for i in range(0, pdf.getNumPages()):
        #     # Extract text from page and add to content
        #     content += pdf.getPage(i).extractText() + "\n"
        # # Collapse whitespace
        # content = " ".join(content.replace(u"\xa0", " ").strip().split())
        # return content.encode("ascii", "ignore")

        pass


