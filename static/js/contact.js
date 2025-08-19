const errorMessage = document.getElementById("errorMessage");
const successMessage = document.getElementById("successMessage");

async function submitContactForm(event) {
	try {
		event.preventDefault();
		const contactForm = document.getElementById("contactForm");
		const form = new FormData(contactForm);
		const data = Object.fromEntries(form.entries());

		if (data.message.length < 3) throw new Error("Your message is too short");

		const response = await fetch("http://127.0.0.1:5000/api/contact", {
			method: "POST",
			headers: { "content-type": "application/json" },
			body: JSON.stringify(data),
		});
		const payload = await response.json();
		successMessage.innerText = payload.message;

		successMessage.style.display = "block";

		return payload;
	} catch (error) {
		// display error message
		errorMessage.innerText = error.message;
		errorMessage.style.display = "block";
	}
}
