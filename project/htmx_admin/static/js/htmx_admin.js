function initHtmxAdmin(path) {
    document.addEventListener("DOMContentLoaded", function (event) {
        // Boost everything
        document.documentElement.setAttribute("hx-boost", "true");

        // If there is a searchbar, make it htmx
        const searchbar = document.getElementById("searchbar");
        if (searchbar) {
            searchbar.setAttribute("hx-get", path);
            searchbar.setAttribute("hx-target", "#changelist-form");
            searchbar.setAttribute("hx-select", "#changelist-form");
            searchbar.setAttribute("hx-push-url", "true");
            searchbar.setAttribute("hx-trigger", "keyup changed delay:500ms");
            searchbar.setAttribute("autocomplete", "off");
        }
    });

}
