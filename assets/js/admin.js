const sideheight = document.querySelector('.sidenav').offsetHeight

function splitScroll(height='100%') {
    const controller = new ScrollMagic.Controller()

    new ScrollMagic.Scene({
        duration:height-sideheight,
        triggerElement:'.sidenav',
        triggerHook:0
    })
    .setPin('.sidenav')
    //.addIndicators()
    .addTo(controller)
}

splitScroll(document.querySelector('.dashboard-sec').height)

let menuItems = document.querySelectorAll('.opsec1')
let showItems = document.querySelectorAll('.menusec')
console.log(menuItems[0].children[0],showItems)

function removemenu() {
    menuItems.forEach(menu=>menu.children[0].classList.remove('active'))
}
function removeshow() {
    showItems.forEach(show=>{
        show.classList.remove('activesec')
    })
}

console.log(document.querySelector('.allproduct-sec'))

menuItems.forEach(menu=>menu.addEventListener('click',selectItem))

function selectItem(e) {
    removemenu()
    removeshow()
    const id = this.id
    const element = document.querySelector(`.${id}-sec`)
    this.children[0].classList.add('active')
    element.classList.add('activesec')
    const height = element.offsetHeight
    splitScroll(height.toString())
}