let promo = document.querySelector('#promo h3')
let apply = document.querySelector('#promo p')
let close1 = document.querySelector('.close1')
console.log(promo)

promo.addEventListener('click',()=>{
    promo.style.display = 'none'
    promo.style.opacity = '0'
    apply.style.display = 'block'
    apply.style.opacity = '1'
})

close1.addEventListener('click',()=>{
    promo.style.display = 'block'
    promo.style.opacity = '1'
    apply.style.display = 'none'
    apply.style.opacity = '0'
})

let menu = document.querySelector('.menu')
let nav = document.querySelector('.nav-section')
let close = document.querySelector('.close')
let n = document.querySelector('nav .d')
let nav_sec = document.querySelector('.nav-section-parent')


console.log(close,menu,nav,n)
menu.addEventListener('click',()=>{
    console.log('Show')
    nav.classList.add('nav-show')
    nav.classList.remove('nav-hide')
    menu.style.opacity = '0'
    nav_sec.classList.add('nav-section-parent-show')
})
close.addEventListener('click',()=> {
    console.log('Close')
    nav.classList.remove('nav-show')
    nav.classList.add('nav-hide')
    menu.style.opacity = '1'
    nav_sec.classList.remove('nav-section-parent-show')
})
let s1 = document.querySelector('.search1')
let close2 = document.querySelector('.close-search')
let sec = document.querySelector('.search')

s1.addEventListener('click',()=>{
    sec.classList.add('animation')
    sec.classList.remove('no-anim')
    console.log('Yes')
})
close2.addEventListener('click',()=>{
    sec.classList.add('no-anim')
    sec.classList.remove('animation')
})