const path = window.location.pathname;
const links = document.querySelectorAll("nav a");
const loginForm = document.getElementById("login-form");

links.forEach((link) => {
	if (path.includes(link.innerHTML.toLowerCase())) link.classList.add("active");
});

async function registerSubmit(event) {
	event.preventDefault();
	const registerForm = document.getElementById("register-form");
	const errorMessage = document.getElementById("error");
	try {
		const formData = new FormData(registerForm);
		const data = Object.fromEntries(formData.entries());
		const response = await fetch("http://127.0.0.1:5000/api/auth/register", {
			method: "POST",
			headers: {
				"content-type": "application/json",
			},
			body: JSON.stringify(data),
		});
		const payload = await response.json();
		if (!payload.success) throw new Error(payload.message || "Can't Register");

		window.location.href = "/login";
	} catch (error) {
		errorMessage.innerText = error.message;
		errorMessage.style.display = "block";
	}
}

async function loginSubmit(event) {
	event.preventDefault();
	const loginForm = document.getElementById("login-form");
	const errorMessage = document.getElementById("error");
	try {
		const formData = new FormData(loginForm);
		const data = Object.fromEntries(formData.entries());
		const response = await fetch("http://127.0.0.1:5000/api/auth/login", {
			method: "POST",
			headers: {
				"content-type": "application/json",
			},
			body: JSON.stringify(data),
		});
		const payload = await response.json();
		if (!payload.success) throw new Error(payload.message || "Can't Register");

		localStorage.setItem("user", payload.data.username);
		localStorage.setItem("userId", payload.data.id);
		window.location.href = "/";
	} catch (error) {
		errorMessage.innerText = error.message;
		errorMessage.style.display = "block";
	}
}
