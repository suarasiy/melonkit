eel.refresh();

function nav_scroll_grab() {
    const nav = document.querySelector("nav");
    const flex_nav = nav.querySelector(".flex-row.flex-row-overflow-x");
    let isDown = false;
    let startX;
    let scrollLeft;
    
    nav.addEventListener("mousedown", (e) => {
        isDown = true;
        flex_nav.classList.add("active");
        startX = e.pageX - flex_nav.offsetLeft;
        scrollLeft = flex_nav.scrollLeft;
    });
    nav.addEventListener("mouseup", () => {
        isDown = false;
        flex_nav.classList.remove("active");
    })
    nav.addEventListener("mouseleave", () => {
        isDown = false;
        flex_nav.classList.remove("active");
    });
    nav.addEventListener("mousemove", (e) => {
        if ( !isDown ) return;
        e.preventDefault();
        const x = e.pageX - flex_nav.offsetLeft;
        const walk = ( x - startX ) * 1.105;
        flex_nav.scrollLeft = scrollLeft - walk;
        // console.log(walk);
    })
}

nav_scroll_grab();

function panel_scroll_grab() {
    const panel = document.querySelector(".panel");
    let isDown = false;
    let startY;
    let scrollTop;

    panel.addEventListener("mousedown", (e) => {
        if ( e.target.getAttribute("action-float") != null || e.target.parentNode.getAttribute("action-float") != null ) {
            isDown = false;
            return;
        }

        isDown = true;
        panel.classList.add("active");
        startY = e.pageY - panel.offsetTop;
        scrollTop = panel.scrollTop;
    });
    panel.addEventListener("mouseup", () => {
        isDown = false;
        panel.classList.remove("active");
    });
    panel.addEventListener("mouseleave", () => {
        isDown = false;
        panel.classList.remove("active");
    });
    panel.addEventListener("mousemove", (e) => {
        if ( !isDown ) return;
        e.preventDefault();
        const y = e.pageY - panel.offsetTop;
        const walk = ( y - startY ) * 1.105;
        panel.scrollTop = scrollTop - walk;
        // console.log(walk);
    })
}

panel_scroll_grab();

var text_search = document.querySelector("#search");
text_search.focus();

function hotkeys() {
    const text_search = document.querySelector("#search");
    document.onkeydown = function(event) {
        if (event.ctrlKey && event.key == "f") {
            event.preventDefault();
            text_search.focus();
        }
    }
}

hotkeys();

eel.expose(clear_code)
function clear_code() {
    const panel = document.querySelector("#panel");
    panel.innerHTML = "";
    console.log("asd");
}

eel.expose(code_list)
function code_list(id, lang, title, description, date_created_at, time_created_at, url) {
    const panel = document.querySelector("#panel");

    const div_wrapper = document.createElement("DIV");
    div_wrapper.setAttribute("item-id", id);
    div_wrapper.classList.add("wrapper");
    panel.appendChild(div_wrapper);
    
    const content = document.createElement("DIV");
    content.classList.add("content");
    div_wrapper.appendChild(content);

    const img_container = document.createElement("DIV");
    img_container.classList.add("img-container");
    img_container.classList.add(`color-${lang}`);
    content.appendChild(img_container);
    
    const img_icon = document.createElement("IMG");
    img_icon.setAttribute("src", `resources/icons/${lang}_127px.png`);
    img_icon.setAttribute("alt", "");
    img_icon.setAttribute("draggable", false);
    img_container.appendChild(img_icon);

    const txt_container = document.createElement("DIV");
    txt_container.classList.add("txt-container");
    txt_container.classList.add(`color-${lang}`);
    content.appendChild(txt_container);
    
    const span_title = document.createElement("SPAN");
    span_title.classList.add("title");
    span_title.innerText = title;
    txt_container.appendChild(span_title);

    const div_detail = document.createElement("DIV");
    div_detail.classList.add("detail");
    txt_container.appendChild(div_detail);

    const span_info_date = document.createElement("SPAN");
    span_info_date.classList.add("info");
    span_info_date.classList.add("info-date");
    span_info_date.innerText = date_created_at;
    div_detail.appendChild(span_info_date);

    const span_info_time = document.createElement("SPAN");
    span_info_time.classList.add("info");
    span_info_time.classList.add("info-time");
    span_info_time.innerText = time_created_at;
    div_detail.appendChild(span_info_time);
    

    const span_info_url = document.createElement("SPAN");
    span_info_url.classList.add("info");
    span_info_url.classList.add("info-url");
    span_info_url.innerText = url;
    div_detail.appendChild(span_info_url);
}

eel.get_list();

eel.expose(filter_code_list)
function filter_code_list(elem) {
    const lang = elem.getAttribute("data-filter-code");
    eel.get_list_filter(lang);
}

function search_get_list() {
    const text_search = document.querySelector("#search");
    text_search.onkeyup = function(event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            eel.get_list_search(text_search.value);
        }
    }
}

search_get_list();