from django.http import JsonResponse, HttpResponse

from http import HTTPStatus


class Response:
    def __new__(cls, detail="", payload={}, status=HTTPStatus.OK):
        if status.value >= 400:
            return HttpResponse(
                "<h1>({}) {}</h1>".format(status.value, status.phrase),
                status=status,
            )

        return JsonResponse(data={"detail": detail, "data": payload}, status=status)
