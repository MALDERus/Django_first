window.onload = function () {
    $('.basket_list').on( types:'click', selector: 'input[type="number"]', data: function () {
        let target_href = event.target;

        if (target_href) {
            $.ajax( url: {
                url: "/basket/edit/" + target_href.name + "/" + target_href.value + "/",

                success: function (data) {
                    $('.basket_list').html(data.result);
                    console.log('ajax done');
                },
            });

        }
        event.preventDefault();
    });

};