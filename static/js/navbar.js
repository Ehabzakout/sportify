const links = document.querySelectorAll("nav ul a");
const userPhoto = document.getElementById("userPhoto");
const login = document.getElementById("login");
const logout = document.getElementById("logout");
const menu = document.getElementById("menu");
const list = document.getElementById("list");
const profile = document.getElementById("profile");
const mobileLogin = document.getElementById("mobileLogin");
const mobileLogout = document.getElementById("mobileLogout");
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
	mobileLogin.style.display = "none";
	profile.style.display = "block";
	mobileLogout.style.display = "block";
} else {
	userPhoto.style.display = "none";
	logout.style.display = "none";
	profile.style.display = "none";
	mobileLogout.style.display = "none";
}

logout.addEventListener("click", () => {
	localStorage.clear();
});

mobileLogout.addEventListener("click", () => {
	localStorage.clear();
});

window.addEventListener("click", (e) => {
	if (e.target == menu) {
		list.classList.toggle("hidden");
	} else {
		if (!list.classList.contains("hidden")) list.classList.add("hidden");
	}
});
