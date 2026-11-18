import logging
import time

logger = logging.getLogger('duration_time')

class RequestTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time
        response["X-Request-Time"] = str(duration)
        logger.info(
            f"{request.path} - {duration}"
        )
        return response
