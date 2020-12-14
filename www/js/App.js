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