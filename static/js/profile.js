const routes = document.querySelectorAll("a.link");
const userInfo = document.getElementById("user-info");
const pathname = new URL(window.location).pathname;
const userId = localStorage.getItem("userId");
const deleteUser = document.getElementById("delete");

const errorMessage = document.getElementById("error");
routes.forEach((el) => {
	if (pathname.includes(el.innerHTML.toLowerCase())) el.classList.add("active");
	else el.classList.remove("active");
});

if (userId && pathname.includes("info")) {
	async function getUserData() {
		try {
			const response = await fetch(
				`http://127.0.0.1:5000/api/user-info/${userId}`,
				{
					method: "GET",
					headers: { "content-type": "application/json" },
				}
			);
			const payload = await response.json();
			console.log(payload);
			return payload;
		} catch (error) {
			console.log(error);
		}
	}
	getUserData().then((payload) => {
		const user = payload.user;
		for (let i in user) {
			if (i == "id" || i == "password") continue;
			const div = document.createElement("div");
			div.className = "flex gap-8";
			const h2 = document.createElement("h2");
			h2.className = "font-semibold w-20 capitalize";
			h2.innerText = i;
			div.appendChild(h2);
			const p = document.createElement("p");
			p.innerText = user[i];
			div.appendChild(p);
			userInfo.appendChild(div);
		}
	});
}

async function updateForm(event) {
	event.preventDefault();
	try {
		const userId = localStorage.getItem("userId");
		if (!userId) throw new Error("Can't get id");
		const updateForm = document.getElementById("update-form");
		const form = new FormData(updateForm);
		const data = Object.fromEntries(form.entries());
		data.id = +userId;
		if (data.password.length < 6)
			throw new Error("You password should be at least 6 chars");

		if (data.confirm !== data.password)
			throw new Error("Your password doesn't match");
		delete data.confirm;
		const response = await fetch("http://127.0.0.1:5000/api/password/update", {
			method: "PATCH",
			headers: {
				"content-type": "application/json",
			},
			body: JSON.stringify(data),
		});
		const payload = await response.json();
		if (!payload.success)
			throw new Error(payload.message || "Can't Update password");
		localStorage.clear();
		window.location.href = "/login";
	} catch (error) {
		errorMessage.innerText = error.message;
		errorMessage.style.display = "block";
	}
}
if (userId && pathname.includes("update")) {
}

deleteUser.onclick = async () => {
	const accept = window.confirm("Are you sure you want to delete your account");
	if (accept) {
		try {
			const response = await fetch(
				`http://127.0.0.1:5000/api/delete-user/${userId}`,
				{
					method: "DELETE",
					headers: { "content-type": "application/json" },
				}
			);
			const payload = await response.json();
			localStorage.clear();
			window.location.href = "/";
			return payload;
		} catch (error) {
			console.log(error);
		}
	}
};
