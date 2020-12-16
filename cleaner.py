import os

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}") 

if __name__ == "__main__":
        
    files = os.listdir()
    files.remove("cleaner.py")

    createIfNotExist('Images')
    createIfNotExist('Docs')
    createIfNotExist('Media')
    createIfNotExist('Zip')
    createIfNotExist('FrontEnd')
    createIfNotExist('BackEnd')
    createIfNotExist('ShortCut')
    createIfNotExist('WindowApplications')
    createIfNotExist('Others')

    imgExts = [".png", ".jpg", ".jpeg", ".wav"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts ]

    docExts = [".txt", ".docx", "doc", ".pdf", ".ppt"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

    mediaExts = [".mp4", ".mp3", ".flv"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

    zipExts = [".rar", ".zip"]
    zips = [file for file in files if os.path.splitext(file)[1].lower() in zipExts]

    frontEndExts = [".html", ".css", ".js", ".ts", ".elm.gz", ".elm"]
    frontEnd = [file for file in files if os.path.splitext(file)[1].lower() in frontEndExts]

    backEndExts = [".sql", ".php", ".js", ".py", ".java", ".elm", ".rb", ".sc", ".scala"]
    backEnd = [file for file in files if os.path.splitext(file)[1].lower() in backEndExts]

    shortcutExts = [".Ink", ".ink"]
    shortCuts = [file for file in files if os.path.splitext(file)[1].lower() in shortcutExts]

    windowExts = [".exe"]
    windowApp = [file for file in files if os.path.splitext(file)[1].lower() in windowExts]

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and (ext not in imgExts) and (ext not in frontEndExts) and (ext not in backEndExts) and os.path.isfile(file):
            others.append(file)

    move("Images", images)
    move("Docs", docs)
    move("Media", medias)
    move("Zip", zips)
    move("FrontEnd", frontEnd)
    move("BackEnd", backEnd)
    move("ShortCut", shortCuts)
    move("WindowApplications", windowApp)
    move("Others", others)
