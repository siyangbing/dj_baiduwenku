
import os

if __name__ == "__main__":
    os.system("gunicorn -c example_conf.py dj_baiduwenku.asgi:application -k uvicorn.workers.UvicornWorker")