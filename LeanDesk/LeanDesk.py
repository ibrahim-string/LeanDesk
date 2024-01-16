import os 
import shutil
class LeanDesk:
    def cleaning_dir(self, path):
        # downloads_path = os.path.join('C:\\', 'Users', f'{UserName}', 'Downloads')
        downloads_path = os.path.join(path)
        os.chdir(downloads_path)
        li = os.listdir()

        pdf_directory = os.path.join(downloads_path, 'PDF files')
        os.makedirs(pdf_directory, exist_ok=True)
        for i in li:
            if '.pdf' in i:
              
                source_path = os.path.join(downloads_path, i)
                destination_path = os.path.join(pdf_directory, i)
                shutil.move(source_path, destination_path)


        py_dir = os.path.join(downloads_path,"Python files")
        os.makedirs(py_dir,exist_ok=True)
        for i in li: 
            if ".py" in i: 
                source_path_py = os.path.join(downloads_path,i)
                destination_path_py = os.path.join(py_dir,i)
                shutil.move(source_path_py,destination_path_py)

                
        docx_directory = os.path.join(downloads_path,' documents files')
        os.makedirs(docx_directory,exist_ok=True)
        for i in os.listdir():
            if '.docx' in i or '.doc' in i:
                source_path_docx = os.path.join(downloads_path,i)
                destination_path_docx = os.path.join(docx_directory,i)
                shutil.move(source_path_docx,destination_path_docx)
                

        
        mp3_directory = os.path.join(downloads_path,'mp3 files')
        os.makedirs(mp3_directory,exist_ok=True)
        for i in os.listdir():
            if '.mp3' in i or 'mp4' in i:
                source_path_mp3 = os.path.join(downloads_path,i)
                destination_path_mp3 = os.path.join(mp3_directory,i)
                shutil.move(source_path_mp3,destination_path_mp3)
        
        excel_dir = os.path.join(downloads_path,'Excel files')
        os.makedirs(excel_dir,exist_ok=True)
        for i in os.listdir():
            if '.xlsx' in i or '.xls' in i:
                source_path_excel = os.path.join(downloads_path,i)
                destination_path_excel = os.path.join(excel_dir,i)
                shutil.move(source_path_excel,destination_path_excel)
        
        zip_dir = os.path.join(downloads_path,'Zip files')
        os.makedirs(zip_dir,exist_ok=True)
        for i in os.listdir():
            if '.zip' in i or '.ZIP' in i:
                source_path_zip = os.path.join(downloads_path,i)
                destination_path_zip = os.path.join(zip_dir,i)
                shutil.move(source_path_zip,destination_path_zip)

        exe_dir = os.path.join(downloads_path,"Exe files")
        os.makedirs(exe_dir,exist_ok=True)
        for i in os.listdir():
            if '.exe' in i:
                source_path_exe = os.path.join(downloads_path,i)
                destination_path_exe = os.path.join(exe_dir,i)
                shutil.move(source_path_exe,destination_path_exe)
        
        text_dir = os.path.join(downloads_path,'Text files')
        os.makedirs(text_dir,exist_ok=True)
        for i in os.listdir():
            if '.txt' in i:
                source_path_text = os.path.join(downloads_path,i)
                destination_path_text = os.path.join(text_dir,i)
                shutil.move(source_path_text,destination_path_text)
        png_dir = os.path.join(downloads_path,'PNG files')
        os.makedirs(png_dir,exist_ok=True)
        for i in os.listdir():
            if '.png' in i or '.PNG' in i:
                source_path_png = os.path.join(downloads_path,i)
                destination_path_png = os.path.join(png_dir,i)
                shutil.move(source_path_png,destination_path_png)

        csv_dir = os.path.join(downloads_path,'CSV files')
        os.makedirs(csv_dir,exist_ok=True)
        for i in os.listdir():
            if '.csv' in i:
                source_path_csv = os.path.join(downloads_path,i)
                destination_path_csv = os.path.join(csv_dir,i)
                shutil.move(source_path_csv,destination_path_csv)
        gif_dir =os.path.join(downloads_path,'GIF files')
        os.makedirs(gif_dir,exist_ok=True)
        for i in os.listdir():
            if '.gif' in i: 
                source_path_gif = os.path.join(downloads_path,i)
                destination_path_gif = os.path.join(gif_dir,i)
                shutil.move(source_path_gif,destination_path_gif)

        jpeg_dir = os.path.join(downloads_path,'JPG files')
        os.makedirs(jpeg_dir,exist_ok=True)
        for i in os.listdir():
            if '.jpeg' in i or '.jpg' in i:
                source_path_jpeg = os.path.join(downloads_path,i)
                destination_path_jpeg = os.path.join(jpeg_dir,i)
                shutil.move(source_path_jpeg,destination_path_jpeg)

        html_dir = os.path.join(downloads_path,"HTML files")
        os.makedirs(html_dir,exist_ok=True)
        for i in os.listdir():
            if '.html' in i: 
                source_path_html = os.path.join(downloads_path,i)
                destination_path_html = os.path.join(html_dir,i)
                shutil.move(source_path_html,destination_path_html)
        notebook_dir = os.path.join(downloads_path,"Notebook files")
        os.makedirs(notebook_dir,exist_ok=True)
        for i in os.listdir():
            if '.ipynb' in i:
                source_path_notebook = os.path.join(downloads_path,i)
                destination_path_notebook = os.path.join(notebook_dir,i)
                shutil.move(source_path_notebook,destination_path_notebook)
        ppt_dir = os.path.join(downloads_path,"PPT flies")
        os.makedirs(ppt_dir,exist_ok=True)
        for i in os.listdir():
            if '.pptx' in i or '.ppt' in i:
                source_path_ppt = os.path.join(downloads_path,i)
                destination_path_ppt = os.path.join(ppt_dir,i)
                shutil.move(source_path_ppt,destination_path_ppt)


        svg_dir = os.path.join(downloads_path,'SVG files')
        os.makedirs(svg_dir,exist_ok=True)
        for i in os.listdir():
            if '.svg' in i or '.SVG' in i:
                source_path_svg = os.path.join(downloads_path,i)
                destination_path_svg = os.path.join(svg_dir,i)
                shutil.move(source_path_svg,destination_path_svg)

        mov_dir = os.path.join(downloads_path,'MOV files')
        os.makedirs(mov_dir,exist_ok=True)
        for i in os.listdir():
            if '.mov' in i or '.MOV' in i:
                source_path_mov = os.path.join(downloads_path,i)
                destination_path_mov = os.path.join(mov_dir,i)
                shutil.move(source_path_mov,destination_path_mov)

        json_dir = os.path.join(downloads_path,'JSON files')
        os.makedirs(json_dir,exist_ok=True)
        for i in os.listdir():
            if '.json' in i or '.JSON' in i:
                source_path_json = os.path.join(downloads_path,i)
                destination_path_json = os.path.join(json_dir,i)
                shutil.move(source_path_json,destination_path_json)

        webp_dir = os.path.join(downloads_path,'webp files')
        os.makedirs(webp_dir,exist_ok=True)
        for i in os.listdir():
            if '.webp' in i or '.WEBP' in i: 
                source_path_webp = os.path.join(downloads_path,i)
                destination_path_webp = os.path.join(webp_dir,i)
                shutil.move(source_path_webp,destination_path_webp)
   




