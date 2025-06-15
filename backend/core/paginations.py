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

class CustomLimitOffset(LimitOffsetPagination):
    # offset :- from which no count will start.
    default_limit = 2  # if limit not provide then limit
    limit_query_param = 'lim' # default limit
    offset_query_param = 'off' # default offset

    # http://localhost/api/accounts/?lim=4&off=4
    max_limit = 3 # maximum limit size.


class CustomCursor(CursorPagination):
    page_size = 3
    # cursor_query_param = 'cur'
    # ordering = '-created_at'
    ordering = 'name'