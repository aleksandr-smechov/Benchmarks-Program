/* Tag a form field as valid or invalid */
const tagField = (elt, valid) => {
	if (valid) {
		elt.classList.remove('invalid');
		elt.parentElement.classList.remove('invalid');
		elt.classList.add('valid');
		elt.parentElement.classList.add('valid');
	}
	else {
		elt.classList.remove('valid');
		elt.parentElement.classList.remove('valid');
		elt.classList.add('invalid');
		elt.parentElement.classList.add('invalid');
	}
}

/* Validate a form element on the client side
	Has the side-effect of applying valid/invalid classes */
const clientSideValidateField = elt => {
	const 
		type = elt.getAttribute('customType'),
		value = elt.value;
	let valid = true;
	if (type == "key")
		valid = (value.length !== 0 && value.indexOf('-us') !== -1);
	else if (type == "email") {
		valid = (value.length !== 0 && 
			value.indexOf('@') !== -1 && value.indexOf('.') !== -1);
	}
	else
		valid = value.length !== 0;
	tagField(elt, valid);
	return valid;
}

/* Validates a form elements on the client side
	slightly inefficiently written so that the whole loop will execute
	and tag each input as valid or invalid as a side effect */
const clientSideValidateForm = form => {
	const elts = form.querySelectorAll('input');
	let valid = true;
	for (let i = 0; i < elts.length; ++i) {
		const validity = clientSideValidateField(elts[i])
		if (!validity)
			valid = false;
	}
	return valid;
}

/* Monitors form elements and automatically performs client-side validation
	whenever a user stops typing */
const formElts = document.querySelectorAll('.form-input-wrapper input');
for (let i = 0; i < formElts.length; ++i) {
	const elt = formElts[i];
	elt.addEventListener('keyup', e => clientSideValidateField(e.currentTarget));
}

/* Disables an elt or a nodelist of elts */
const disable = elts => {
	if (NodeList.prototype.isPrototypeOf(elts)) {
		for (let i = 0; i < elts.length; ++i)
			elts[i].classList.add('disabled-elt');
	}
	else
		elts.classList.add('disabled-elt');
}

/* Enables an elt or a nodelist of elts */
const enable = elts => {
	if (NodeList.prototype.isPrototypeOf(elts)) {
		for (let i = 0; i < elts.length; ++i)
			elts[i].classList.remove('disabled-elt');
	}
	else
		elts.classList.remove('disabled-elt');
}

/* Value of csrf token to protect against cross-site forgery attacks */
const csrfToken = document.querySelector('meta[name=csrf-token]').content;