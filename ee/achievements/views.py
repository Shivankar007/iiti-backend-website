from rest_framework.views import APIView
from .serializer import BooksSerializer
from rest_framework.response import Response
from .models import Books

class GetBooksAPI(APIView):
    def get(self, request):
        if request.method == "GET":
            try:
                books = Books.objects.all()
            except books.DoesNotExist:
                return Response({"error": "No   books"}, status=404)
            books = BooksSerializer(books, many=True)
            return Response(books.data)
        return Response({"message": "{} method is not allowed".format(request.method)})
