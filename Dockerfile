FROM python:3.9-slim-bullseye

WORKDIR /MyGallery

RUN   python3 -m venv env 
RUN pip3 install --upgrade pip 

COPY  . .
 
RUN   chmod +x entrypoint.sh && \
    . env/bin/activate
        
      
EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]

