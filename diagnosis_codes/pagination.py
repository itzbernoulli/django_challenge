from rest_framework.pagination import (
	LimitOffsetPagination,
	PageNumberPagination
	)


class DiagnosisCodeLimitOffsetPagination(LimitOffsetPagination):
	default_limit = 3
	max_limit = 20