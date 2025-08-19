const links = document.querySelectorAll("nav ul a");
const userPhoto = document.getElementById("userPhoto");
const login = document.getElementById("login");
const logout = document.getElementById("logout");

const storage = localStorage.getItem("user");
const path =
	window.location.pathname == "/" ? "home" : window.location.pathname;

// add active class to active link
links.forEach((link) => {
	if (path.includes(link.innerHTML.toLowerCase())) {
		link.classList.add("active");
	} else {
		link.classList.remove("active");
	}
});

if (storage) {
	userPhoto.innerText = storage[0].toUpperCase();
	login.style.display = "none";
	logout.style.display = "block";
} else {
	userPhoto.style.display = "none";
	logout.style.display = "none";
}

logout.addEventListener("click", () => {
	localStorage.clear();
});
