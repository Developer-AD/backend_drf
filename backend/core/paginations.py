from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class CustomPageNumPagination(PageNumberPagination):
    page_size = 2
    # page_query_param = 'p' # replace ?page=3 --> ?q=3

    # We can change per page size from client side.
    # page_size_query_param = 'size' 
    # http://localhost/api/accounts/?page=1&size=5

    # max_page_size = 5 # restrict page size from client.

    # http://localhost/api/accounts/?page=last # Last page.
    # last_page_strings = 'end' # change from last to end.