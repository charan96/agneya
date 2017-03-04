from crispy_forms.bootstrap import PrependedText, FormActions, Field
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, HTML, Div, Fieldset
from django import forms
import datetime
import helpers


class submit_form(forms.Form):
	list_to_twentyfour = [(str(x).zfill(2), str(x).zfill(2)) for x in range(0, 24)]
	list_to_sixty = [(str(x).zfill(2), str(x).zfill(2)) for x in range(0, 60)]

	sunrise_hour = forms.ChoiceField(choices=list_to_twentyfour, required=True, label='sunrise-hour',
						   initial=str(datetime.datetime.now().hour).zfill(2))
	sunrise_min = forms.ChoiceField(choices=list_to_sixty, required=True, label='sunrise-min',
						  initial=str(datetime.datetime.now().minute).zfill(2))
	sunrise_sec = forms.ChoiceField(choices=list_to_sixty, required=True, label='sunrise-sec',
						  initial=0)

	sunset_hour = forms.ChoiceField(choices=list_to_twentyfour, required=True, label='sunset-hour',
						  initial=str((datetime.datetime.now().hour + 12) % 24).zfill(2))
	sunset_min = forms.ChoiceField(choices=list_to_sixty, required=True, label='sunset-min',
						 initial=str(datetime.datetime.now().minute).zfill(2))
	sunset_sec = forms.ChoiceField(choices=list_to_sixty, required=True, label='sunset-sec',
						 initial=0)

	def __init__(self, *args, **kwargs):
		super(submit_form, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_class = 'form-inline'
		self.helper.form_method = 'post'
		self.helper.form_action = ""
		self.helper.form_show_labels = False
		self.helper.layout = Layout(
			HTML("<br><br>"),
			HTML("<br>"),
			Fieldset(
				"Sunrise: ",
				Div('sunrise_hour', 'sunrise_min', 'sunrise_sec', css_class="col-md-8 col-md-offset-2"),
				HTML("<br><br><br>")
			),
			HTML("<br><br>"),
			Fieldset(
				"Sunset: ",
				Div('sunset_hour', 'sunset_min', 'sunset_sec', css_class="col-md-8 col-md-offset-2"),
				HTML("<br><br><br>")
			),
			HTML("<br><br>"),
			Div('submit', css_class="col-md-6 col-lg-offset-4"),
			FormActions(
				Submit('submit', 'Submit', css_class="btn btn-success")
			)
		)
