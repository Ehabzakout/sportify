const path = window.location.pathname;
const links = document.querySelectorAll("nav a");
const loginForm = document.getElementById("login-form");

// add active class to link
links.forEach((link) => {
	if (path.includes(link.innerHTML.toLowerCase())) link.classList.add("active");
});

// function to submit register form
async function registerSubmit(event) {
	event.preventDefault();
	const registerForm = document.getElementById("register-form");
	const errorMessage = document.getElementById("error");
	try {
		// get form data and
		const formData = new FormData(registerForm);
		const data = Object.fromEntries(formData.entries());
		for (let i in data) {
			data[i] = data[i].trim();
		}
		if (data.username == "" || data.username.length < 3) {
			throw new Error("Invalid username");
		}
		if (
			data.phone.length != 11 ||
			data.phone.match(/[a-zA-Z]/) ||
			data.phone == ""
		)
			throw new Error("invalid phone number");
		// check if user enter valid password
		if (data.password.length < 6)
			throw new Error("Your password should be at least 6 char");
		if (data.password !== data.confirm)
			throw new Error("Your password doesn't match");

		// remove confirm password from data object
		delete data.confirm;

		// api request
		const response = await fetch("http://127.0.0.1:5000/api/auth/register", {
			method: "POST",
			headers: {
				"content-type": "application/json",
			},
			body: JSON.stringify(data),
		});

		// parse api response
		const payload = await response.json();
		if (!payload.success) throw new Error(payload.message || "Can't Register");

		// navigate user to login page
		window.location.href = "/login";
	} catch (error) {
		// display error message
		errorMessage.innerText = error.message;
		errorMessage.style.display = "block";
	}
}

// submit login form
async function loginSubmit(event) {
	event.preventDefault();

	const loginForm = document.getElementById("login-form");
	const errorMessage = document.getElementById("error");
	try {
		// get form data
		const formData = new FormData(loginForm);
		const data = Object.fromEntries(formData.entries());
		for (let i in data) {
			data[i] = data[i].trim();
		}
		if (data.password == "") {
			throw new Error("Invalid password");
		}

		// api request
		const response = await fetch("http://127.0.0.1:5000/api/auth/login", {
			method: "POST",
			headers: {
				"content-type": "application/json",
			},
			body: JSON.stringify(data),
		});

		// parse api response
		const payload = await response.json();
		if (!payload.success) throw new Error(payload.message || "Can't Register");

		// add username and id to localstorage
		localStorage.setItem("user", payload.data.username);
		localStorage.setItem("userId", payload.data.id);

		// navigate user to home page
		window.location.href = "/";
	} catch (error) {
		// display error message if it is exist
		errorMessage.innerText = error.message;
		errorMessage.style.display = "block";
	}
}
