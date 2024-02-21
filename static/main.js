//random
function rd(min, max) {
    return Math.random() * (max - min) + min
}
//


//animateCSS
const animateCSS = (obj, animation, prefix = '') =>

  // We create a Promise and return it
    new Promise((resolve, reject) => {
        const animationName = `${prefix}${animation}`;
        const node = obj;
        console.log(node)
        node.classList.add(`${prefix}animate__animated`, animationName);

        // When the animation ends, we clean the classes and resolve the Promise
        function handleAnimationEnd(event) {
            event.stopPropagation();
            node.classList.remove(`${prefix}animated`, animationName);
            resolve('Animation ended');
        }

        node.addEventListener('animationend', handleAnimationEnd, {once: true});
});
//

//moveable element
var DragAndMoveObjs = document.querySelectorAll(".drag-move");
var offsets = []

DragAndMoveObjs.forEach(function (obj, index) {
    

    offsets.push([0, 0])
    var isDown = false;
    
    obj.addEventListener('mousedown', function(e) {
    isDown = true;
    offsets[index] = [
        obj.offsetLeft - e.clientX,
        obj.offsetTop - e.clientY
     ];
    }, true);
    
    document.addEventListener('mouseup', function() {
       isDown = false;
    }, true);
    
    document.addEventListener('mousemove', function(e) {
        e.preventDefault();
        if (isDown) {
            obj.style.left = (e.clientX + offsets[index][0]) + 'px';
            obj.style.top  = (e.clientY + offsets[index][1]) + 'px';
       }
    }, true);

})

//


//cloud

var Clouds = document.querySelectorAll(".drag-move");
var Cloud_Data = []

Clouds.forEach(function (obj, index) {
    d_x = rd(0.4, 2)
    d_y = rd(0.4, 2)
    t_x = rd(10, 20)
    t_y = rd(10, 20)
    Cloud_Data.push([d_x, d_y, 0, 0, t_x, t_y])

    // obj.style.left = rd(20, innerWidth - 400) + 'px'
    // obj.style.top = rd(20, innerHeight - 180) + 'px'

    obj.addEventListener('click', ()=>{
        animateCSS(obj, 'animate__swing')
    })

})

setInterval(() => {
    Clouds.forEach(function (obj, index) {
        
        x = Number(obj.style.left.replace("px", ""));
        y = Number(obj.style.top.replace("px", ""));
        
        x = x - Cloud_Data[index][0]
        y = y - Cloud_Data[index][1]

        Cloud_Data[index][2] += 1
        Cloud_Data[index][3] += 1

        if(Cloud_Data[index][2] >= Cloud_Data[index][4]) {
            Cloud_Data[index][2] = 0
            Cloud_Data[index][0] *= -1
        }
        if(Cloud_Data[index][3] >= Cloud_Data[index][5]) {
            Cloud_Data[index][3] = 0
            Cloud_Data[index][1] *= -1
        }

        obj.style.left = x + 'px'
        obj.style.top = y + 'px'
        
    })
}, (100));

//