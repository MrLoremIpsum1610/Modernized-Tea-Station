$ = document

 

$.addEventListener('DOMContentLoaded', function() {
    const hoverElements = $.querySelectorAll('.onHover');
    let timeoutId;
    
    hoverElements.forEach(element => {
        element.addEventListener('mouseenter', function() {
            clearTimeout(timeoutId); // هر تاخیر قبلی را لغو کن
            const underline = this.querySelector('.underLines');
            
            if (underline) {
                underline.classList.remove('w-7/12');
                underline.classList.add('w-11/12');
            }
        });
        
        element.addEventListener('mouseleave', function() {
            const underline = this.querySelector('.underLines');
            
            if (underline) {
                // تاخیر کوتاه قبل از بازگشت به حالت اولیه
                    underline.classList.remove('w-11/12');
                    underline.classList.add('w-7/12');
            }
        });
    });
});
