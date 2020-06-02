#imagen base
FROM python:3.7

#COPY ./rutascuadriculadas.py /rutascuadriculadas.py
COPY ./tripenhex.py /tripenhex.py

#CMD ["python", "/rutascuadriculadas.py"] 
CMD ["python", "/tripenhex.py"]

#CMD ["python", "/covid19.py"] 
CMD ["python", "/tripenhex.py"]
