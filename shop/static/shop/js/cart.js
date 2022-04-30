var updateBtns = document.getElementsByClassName('update-cart')

var ID = function () {
    return '_' + Math.random().toString(36).substr(2, 9);
};

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'Action', action)

        console.log('Session:', ID)
    })
}