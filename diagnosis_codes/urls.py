from django.conf.urls import url
from . import views

urlpatterns = [
	url(
		r'^api/v1/diagnosis_codes/(?P<pk>[0-9]+)$',
		views.get_delete_update_diagnosis_code,
		name='get_delete_update_diagnosis_code'
		),
	url(
		r'^api/v1/diagnosis_codes/$',
		views.get_post_diagnosis,
		name='get_post_diagnosis'
		)
]