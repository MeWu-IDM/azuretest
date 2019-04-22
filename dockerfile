FROM python:3.6
ADD . /app
WORKDIR /app
CMD ["python", "test.py", "-o", $outfolder, "-n", $filename]