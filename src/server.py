import io

import uvicorn
from PIL import Image

from fastapi import FastAPI, UploadFile, File

from img_with_name_dataloader import transform

app = FastAPI()


@app.post('/upload/')
async def upload_file(file: UploadFile = File(...)):
    image = await file.read()
    image = Image.open(io.BytesIO(image))
    image = image.convert('RGB')
    image = transform(image)

    return {
        'filename': file.filename
    }


def main():
    uvicorn.run(
        'src.server:app',
        host='0.0.0.0',
        port=8000,
        reload=True,
    )


if __name__ == '__main__':
    main()
