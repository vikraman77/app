var typed = new Typed(".multiple-text", {
    strings : ['Web Developer', 'Python Developer', 'Health Inspector', 'Gamer'],
    typespeed: 5,
    backspeed: 80,
    backDelay: 2000,
    loop: true
})


const toggleBtn = document.querySelector('.toggle_btn')
const toggleBtnIcon = document.querySelector('.toggle_btn i')
const dropDownMenu = document.querySelector('.dropdown_menu')

toggleBtn.onclick = function () {
    dropDownMenu.classList.toggle('open')
}


