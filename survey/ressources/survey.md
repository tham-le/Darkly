# Survey page vulnerability report

Location: ***http://192.168.56.3/index.php?page=survey***

## Description:

The main issue stems from the ability to modify the values of the select dropdown through clent-side manipulation.

```
<select name="valeur" onchange="javascript:this.form.submit();">
	<option value="1">1</option>
	<option value="2">2</option>
	<option value="3">3</option>
	...
	</select>
```

The ```<select>``` element allows direct value submission via the _onchange_ event. Any value entered in the dropdown will trigger an immediate form submission.

It potentially affects survey results or database entries and triggers unexpected behavior or errors in the backend.

## Recommendations:

1. Impliment server-side validation to ensure only valid values within the expected range are accepted.

2. Add client-side JavaScript validation of input before submission.

3. Before submitting the form, prompt the user to confirm their selection.