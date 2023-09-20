const navbar = document.querySelector('.navbar_custom')

navbar.querySelector('.toggle').addEventListener('click',()=>{
	
	navbar.classList.toggle('collapsed')
	
})

window.addEventListener('scroll',(e)=>{
	
	let windowY = window.pageYOffset
	
	let navbarHeight = document.querySelector('.navbar').offsetHeight
	
	if(windowY>navbarHeight) navbar.classList.add('sticky')
	else navbar.classList.remove('sticky')
	
})