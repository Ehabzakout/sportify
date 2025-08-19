const bookButton = document.querySelectorAll("button.book");
const cancel = document.querySelectorAll("button.cancel");

// get data from search params
const userId = Number(
	new URLSearchParams(window.location.search).get("userId")
);
const playgroundId = Number(
	new URLSearchParams(window.location.search).get("courtId")
);

// book request
async function book(time) {
	try {
		const response = await fetch("http://127.0.0.1:5000/api/booking", {
			method: "POST",
			headers: { "content-type": "application/json" },
			body: JSON.stringify({ playgroundId, userId, time }),
		});
		const payload = await response.json();
		return payload;
	} catch (error) {
		console.log(error);
	}
}

// cancel book request
async function cancelBook(time) {
	try {
		const response = await fetch("http://127.0.0.1:5000/api/booking", {
			method: "DELETE",
			headers: { "content-type": "application/json" },
			body: JSON.stringify({ playgroundId, userId, time }),
		});
		const payload = await response.json();

		return payload;
	} catch (error) {
		console.log(error);
	}
}

// add event click on book button to book request
bookButton.forEach((el) => {
	el.addEventListener("click", () => {
		const day = el.getAttribute("data-day");
		const time = el.getAttribute("data-time");
		book(`${day} ${time}`).then((payload) => {
			if (payload.success) window.location.reload();
		});
	});
});

// add event click on cancel button to cancel book request
cancel.forEach((el) => {
	el.addEventListener("click", () => {
		const day = el.getAttribute("data-day");
		const time = el.getAttribute("data-time");
		cancelBook(`${day} ${time}`).then((payload) => {
			if (payload.success) window.location.reload();
		});
	});
});
