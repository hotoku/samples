chrome.extension.onMessage.addListener(function(request, sender, sendResponse) {
	if (request == "Action") {
		greyscale();
	}
});

function greyscale() {
	$("img").each(function(index) {
		$(this).css("-webkit-filter","grayscale(100%)");
	});
}