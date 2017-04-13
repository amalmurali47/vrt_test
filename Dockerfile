FROM python:2.7
ADD validate-vrt.py /
ADD vrt.schema.json /
ADD vulnerability-rating-taxonomy.json /

RUN pip install jsonschema

CMD [ "python", "./validate-vrt.py" ]
