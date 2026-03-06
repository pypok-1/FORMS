import getCookie from '../js/getCsrfToken.js'

$(document).ready(function() {
    const csrfToken = getCookie('csrftoken');
    const addCartUrl = $('.add-to-cart').data('url');
    const removeCartUrl = $('.remove-from-cart').data('url');

    const updateCart = (url, productId) => {
        $.ajax({
            url: url,
            method: 'POST',
            data: {
                product_id: productId,
                csrfmiddlewaretoken: csrfToken,
            },
            success: function(response) {
                $('#cart-count').text(response.cart_count);
            },
            error: function (jqXHR, textStatus, errorThrow) {
                console.log(textStatus, errorThrow);
            }
        });
    };

    $('.add-to-cart').click(function () {
        updateCart(addCartUrl, $(this).data('id'));
    });

    $('.remove-from-cart').click(function () {
        updateCart(removeCartUrl, $(this).data('id'));
    });
});