import os 
import shutil
class leandesk:
    def changing_path(self, UserName):
        downloads_path = os.path.join('C:\\', 'Users', f'{UserName}', 'Downloads')
        os.chdir(downloads_path)
        li = os.listdir()
        print(os.getcwd())
        # self.csv()
        # self.html()
        # self.image()
        # self.doc()
        # self.jpeg()
        # self.exe()
        # self.gif()
        # self.png()
        # self.zip()
        # self.ppt()
        # self.mp4()
        # self.notebook()
        # self.xslx()
        # self.webp()
        # self.text()
        # self.pdf()
        # for i in li:
        #     if '.pdf' in i:
        #         shutil.move(downloads_path+'\\PDF files\\',downloads_path+f'\\{i}\\')
        #         print(downloads_path+f'\\{i}')
        # print(type(li))
        # return li
        pdf_directory = os.path.join(downloads_path, 'PDF files')
        os.makedirs(pdf_directory, exist_ok=True)

        for i in li:
            if '.pdf' in i:
                # Move the PDF file into the 'PDF files' directory
                src_path = os.path.join(downloads_path, i)
                dst_path = os.path.join(pdf_directory, i)
                shutil.move(src_path, dst_path)
                print(dst_path)

        print(type(li))
    def pdf(self):
        os.mkdir('PDF files')
    # def html():
    #     os.mkdir("HTML files")
    # def image():
    #     os.mkdir("IMAGE files")
    # def doc():
    #     os.mkdir("DOCUMENT files")
    # def jpeg():
    #     os.mkdir("JPEG files")
    # def exe():
    #     os.mkdir("EXE files")
    # def gif():
    #     os.mkdir("GIF files")
    # def png():
    #     os.mkdir("PNG files")
    # def zip():
    #     os.mkdir("ZIP files")
    # def ppt():
    #     os.mkdir("PPT files")
    # def mp4():
    #     os.mkdir("MP4 files")
    # def text():
    #     os.mkdir("Text files")
    # def csv():
    #     os.mkdir("CSV files")
    # def xslx():
    #     os.mkdir("EXCEL files")
    # def notebook():
    #     os.mkdir("NOTEBOOK files")
    # def webp():
    #     os.mkdir("WEBP files")
    


a = leandesk()
b = a.changing_path(UserName='strin')
print(b)
print(os.getcwd())