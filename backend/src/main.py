# from uvicorn import run
# import setup
# if __name__ == "__main__":
#     # setup.setupall()
#     # run("src.routes.api:asgi_app", port=8000, reload=True)
#     run("routes.api:asgi_app", host="0.0.0.0", port=80, reload=True)

# import time

# # Wait for 24hrs
# time.sleep(24 * 60 * 60)

from uvicorn import run
import setup
if __name__ == "__main__":
    setup.setupall()
    # run("src.routes.api:asgi_app", port=8000, reload=True)
    run("routes.api:asgi_app", host="0.0.0.0", port=80, reload=True)