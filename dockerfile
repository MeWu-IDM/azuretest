FROM python:3.6
ADD . /app
WORKDIR /app
ENV outfolder=/app1
ENV filename=x.txt
CMD python test.py -o $outfolder -n $filename