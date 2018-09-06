FROM python:3.6-alpine
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev jpeg-dev \
    zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev harfbuzz-dev fribidi-dev
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["gunicorn", "wsgi"]