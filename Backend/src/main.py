from fastapi import FastAPI, Form, UploadFile, File
import uvicorn
from extractor import extractor
import uuid

app = FastAPI()

@app.post("/extract_from_doc")
def extract_from_doc(
        file_format: str = Form(...),
        file: UploadFile = File(...)
): # file format that you will get will be in binary so you have to generate
    content = file.file.read()
    filepath = "../uploads/" + str(uuid.uuid4()) + ".pdf"
    with open(filepath,'wb') as f:
        f.write(content)
    try:
        data = extractor(filepath,file_format)
    except Exception as e:
        data = {
            "error": str(e)
        }
    return data


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1",port=8000)

