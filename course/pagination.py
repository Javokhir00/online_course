from rest_framework.pagination import LimitOffsetPagination


class MyPagination(LimitOffsetPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 10000
