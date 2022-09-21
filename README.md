# Email-SMS-Spam-Classifier-Project

## Heroku link
### https://smsmailspamclassifier22.herokuapp.com/

**click this**<br>
[E-Mail/SMS Spam Classifier](https://smsmailspamclassifier22.herokuapp.com/)



### Docker Image

    FROM python:3.10
    COPY . /app
    WORKDIR /app
    RUN pip install -r requirements.txt
    EXPOSE $PORT
    CMD gunicore --workers=4 --bind 0.0.0.0:$PORT aap:app
    
    
### Procfile
    web gunicorn app:app

### Screenshot

![screenshoot](https://user-images.githubusercontent.com/84202477/191621781-1a0a05d7-cbe3-48fd-a8fe-2495aa27abde.PNG)
